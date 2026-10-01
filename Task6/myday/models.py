from django.db import models

# Create your models here.
class Product(models.Model):
    pid=models.IntegerField()
    pname=models.CharField(max_length=30)
    pprice=models.FloatField()
    p_offer=models.FloatField()
    def __str__(self):
        return self.pname