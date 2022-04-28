from django.db import models
from django.forms import CharField


#this is where we will be primarily pulling data from to show on our frontend
class Cable(models.Model):
    time_stamp = models.CharField(max_length=200)
    minimum = models.FloatField()
    average = models.FloatField()
    maximum = models.FloatField()


#this table is essentially here so we don't lose data
class Backup_Data(models.Model):
    time_stamp = models.CharField(max_length=200)
    minimum = models.FloatField()
    average = models.FloatField()
    maximum = models.FloatField()