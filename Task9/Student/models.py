from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class newuser(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=30)
    sbranch=models.CharField(max_length=30)
    def __str__(self):
        return self.sname