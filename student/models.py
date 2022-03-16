from django.db import models
# Create your models here.


class Student(models.Model):
    
    register_no = models.CharField(max_length=10, primary_key=True)
    full_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    birth_date = models.DateField(auto_now=())
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


