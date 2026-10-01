from django.db import models


class Employee(models.Model):
    E_no=models.IntegerField()
    E_name=models.CharField(max_length=30)
    E_sal=models.FloatField()
# Create your models here.

def __str__(self):
    return self.E_name


