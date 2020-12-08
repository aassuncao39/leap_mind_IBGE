import json
import os
import math
import requests
from datetime import datetime
from flask import Flask
from flask_restful import Api, Resource


#create API
app = Flask(__name__)
api = Api(app)



# GET the information through HTTP protocol
r=requests.get('https://servicodados.ibge.gov.br/api/v1/projecoes/populacao')

#read and store the json info from HTML
g=r.json()

#convert string to datetime
datetime_object = datetime.strptime(g["horario"], '%d/%m/%Y %H:%M:%S')

#read the increase rate

projection_set=g["projecao"]
periodoMedio_set=projection_set["periodoMedio"]
population_increment=periodoMedio_set["incrementoPopulacional"]
population=projection_set["populacao"]

#input date
#verificar como faz para inserir data num HTML
year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
future_date=datetime(year, month, day)

#population increment between dates

diff_between_dates=(future_date-datetime_object)

seconds_difference=(diff_between_dates.days*86400)+diff_between_dates.seconds
print("A diferença de tempo entre datas e equivalente a " + str(seconds_difference) + " segundos...")

population_increase=math.floor(float((seconds_difference/(float(population_increment)/1000))))

#population prediction

population_date=int(population+population_increase)


#retrieve location
local=g["localidade"]

#print the result
pop1='{:,}'.format(population)
pop2='{:,}'.format(population_date)



#query days, months and years
query_day = datetime_object.strftime('%d')
query_month = datetime_object.strftime('%m')
query_year = datetime_object.strftime('%Y')
date=str(query_day) + "/" + str(query_month) + "/" + str(query_year)


print("No dia de hoje, " + date + ", a população brasileira é equivalente a " + pop1 + " habitantes. Com um incremento populacional previsto de " + str(float(population_increment)/1000) + " habitantes/segundo, para a data de " + str(day) + "/" + str(month) + "/" + str(year) + " espera-se uma população equivalente a " + str(pop2) + " habitantes") 

#write to TXT file

txt=("[log: " + str(datetime_object) + "] -> No dia de hoje, " + date + ", a população brasileira é equivalente a " + pop1 +
     " habitantes. Com um incremento populacional previsto de " +
     str(float(population_increment)/1000) + " habitantes/segundo, para a data de " + str(day) + "/" + str(month) + "/" + str(year) +
     " espera-se uma população equivalente a " + str(pop2) + " habitantes.")


with open('output.txt', 'r+') as json_file:
    json_file.seek(0)
    data = json_file.read()
    if len(data) > 0 and len(data) < 2770:
        json_file=open('output.txt', 'ab')
        json_file.write('\n'+txt)
    else:
        json_file=open('output.txt', 'wb')
        json_file.write(txt)
    json_file.close()



