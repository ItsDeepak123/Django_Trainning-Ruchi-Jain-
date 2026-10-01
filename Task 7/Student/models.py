from django.db import models

# Create your models here.
class Student(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=30)
    sbranch=models.CharField(max_length=30)
    def __str__(self):
        return self.sname