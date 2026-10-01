from django.db import models

class product(models.Model):
    p_id=models.IntegerField()
    p_name=models.CharField()
    p_price=models.FloatField()
    p_offer=models.FloatField()
    def __str__(self):
        return self.p_name

# Create your models here.
