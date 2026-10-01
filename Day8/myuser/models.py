from django.db import models

# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=30,primary_key=True)
    password=models.CharField(max_length=30 )
    name=models.CharField(max_length=30)
    contact=models.IntegerField()
    def __str__(self):
        return self.name