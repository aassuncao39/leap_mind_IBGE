# Generated by Django 3.1.4 on 2020-12-08 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IBGE_pop_projection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
