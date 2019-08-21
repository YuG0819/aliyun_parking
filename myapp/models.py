from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=20)
# Create your models here.

class test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False,max_length=20)