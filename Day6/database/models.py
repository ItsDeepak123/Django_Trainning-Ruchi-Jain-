from django.db import models
# Create your models here.
class Client(models.Model):
    cno=models.IntegerField()
    cname=models.CharField(max_length=30)
    c_company=models.CharField(max_length=30)
def __str__(self):
    return self.Client


class Subject(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=30)
    sbranch=models.CharField(max_length=30)
def __str__(self):
    return self.subject

class Product(models.Model):
    pno=models.IntegerField()
    pname=models.CharField(max_length=30)
    p_price=models.FloatField(default=0)
def __str__(self):
    return self.Product
