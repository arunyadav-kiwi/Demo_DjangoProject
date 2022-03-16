from django.contrib import admin
from .models import Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['register_no', 'full_name', 'email', 'father_name', 'mobile_no']



admin.site.register(Student, StudentAdmin)