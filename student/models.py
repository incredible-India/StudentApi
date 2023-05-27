from django.db import models

# Create your models here.
class Student(models.Model):
    
    studentName = models.CharField(max_length=200,null=False)
    age = models.IntegerField(null=False)
    studentid = models.CharField( max_length=50 , null=False)
    gender =models.CharField(max_length=10,null=False)
    marks = models.IntegerField(null=False)
   