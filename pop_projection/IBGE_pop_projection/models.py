from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Datas(models.Model):
    data = models.DateField()
