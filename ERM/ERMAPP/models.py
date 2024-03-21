from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.CharField(max_length=100,primary_key=True)
    empname = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    DOJ = models.CharField(max_length=100, default=0)
    email= models.CharField(max_length=100)

class Attendance(models.Model):
    current_date=models.CharField(max_length=100,primary_key=True)
    empid = models.IntegerField()
    empname = models.CharField(max_length=100)
    login_time=models.CharField(max_length=100)
    logout_time=models.CharField(max_length=100,default="0")
