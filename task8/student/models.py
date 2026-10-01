from django.db import models

class newuser(models.Model):
    username=models.CharField(max_length=30,primary_key=True)
    password=models.CharField(max_length=40)
    name=models.CharField(max_length=30)
    def __str__(self):
        return  self.name
    
    
class srs(models.Model):
    s_id=models.CharField(max_length=30,primary_key=True)
    s_name=models.CharField(max_length=30)
    s_branch=models.CharField(max_length=30)
    def __str__(self):
        return self.s_name
