from django.db import models

# Create your models here.
class UserInf(models.Model):
    user = models.CharField(max_length=100)
    pwd = models.CharField(max_length=32)
class CityInf(models.Model):
    CityName = models.CharField(max_length=100)
    CityAdd = models.CharField(max_length=100)
class Employee(models.Model):
    name = models.CharField(max_length=255)


