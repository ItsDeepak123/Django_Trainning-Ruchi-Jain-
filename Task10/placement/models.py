from django.db import models

# Create your models here.

class registration(models.Model):
    sname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    sid=models.IntegerField()
    scontact=models.IntegerField()
    semail=models.EmailField(max_length=20)

    def __str__(self):
        return self.sname

    