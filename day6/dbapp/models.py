from django.db import models

# Create your models here.
class client(models.Model):
    client_id = models.BigIntegerField(primary_key=True)
    client_name = models.CharField(max_length=100)
    client_company = models.CharField(max_length=100)
    
def __str__(self):
    return self.client
    
class member(models.Model):
    member_id = models.BigIntegerField(primary_key=True)
    member_name = models.CharField(max_length=100)
    member_company = models.CharField(max_length=100)

def __str__(self):
    return self.member


class company(models.Model):
    company_id = models.BigIntegerField(primary_key=True)
    company_name = models.CharField(max_length=100)
    company_company = models.CharField(max_length=100)
    
def __str__(self):
    return self.company

