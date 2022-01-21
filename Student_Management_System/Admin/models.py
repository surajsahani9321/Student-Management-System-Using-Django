from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=70)
    fatherName=models.CharField(max_length=70)
    age=models.IntegerField()
    dob=models.DateField()
    rollNumber=models.IntegerField()
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
