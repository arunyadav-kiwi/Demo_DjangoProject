from atexit import register
from django.shortcuts import render, redirect
from .models import Student
from django.views import View
from .forms import StudentForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.



def student_add(request):
    if request.method == 'POST':
        register_no = request.POST.get('register_no')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        father_name = request.POST.get('father_name')
        birth_date = request.POST.get('birth_date')
        mobile_no = request.POST.get('mobile_no')
        address = request.POST.get('address')
        stud = Student(register_no=register_no, full_name=full_name, email=email, father_name=father_name, birth_date=birth_date,
        mobile_no=mobile_no, address=address)
        stud.save()
        return redirect('student')
    else:

        return render(request,'add_student.html')



def delete_student(request, student_register_no):
    student_delete = Student.objects.get(pk=student_register_no)
    student_delete.delete()
    messages.error(request, ("You have deteted student data succussfully! "))
    return redirect('student')



class Student_view(View):
    def get(self, request):
        student_data = Student.objects.filter()
        paginator = Paginator(student_data, 8)
        page = request.GET.get('pg')
        student_data = paginator.get_page(page)
        return render (request, 'student.html',{'student_data': student_data})    



def edit_student(request, student_register_no):
    if request.method == "POST":
        student_obj = Student.objects.get(pk=student_register_no)
        form = StudentForm(request.POST, instance=student_obj)
        if form.is_valid():
            form.save()
        messages.success(request, ("Task Edited !"))
        return redirect('student')
    else:
        student_obj = Student.objects.get(pk=student_register_no)
        return render(request, 'student_edit.html', {'student_obj': student_obj})
