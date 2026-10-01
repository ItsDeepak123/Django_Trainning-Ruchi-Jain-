from django.db import models


# Create your models here.
class Paper(models.Model):
    Sname=models.CharField(max_length=30)
    Username=models.CharField(max_length=30)
    Pass=models.CharField(max_length=30)
    contact=models.IntegerField()
    def __str__(self):
        return self.Sname