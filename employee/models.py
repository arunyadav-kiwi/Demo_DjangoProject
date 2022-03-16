from django.db import models

# Create your models here.


class Employee_details(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    emp_code = models.CharField(max_length=15)
    dept = models.CharField(max_length=50)
    date_birth = models.DateField(auto_now=())
    mobile_no = models.CharField(max_length=10)
    email  = models.EmailField(unique=True, null=False)
    adhar_no = models.CharField(max_length=20, unique=True)
    pan_no = models.CharField(max_length=20, unique=True)
    