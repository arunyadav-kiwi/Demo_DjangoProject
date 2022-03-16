from  django.urls import path
from .views import Student_view
from . import views


urlpatterns = [
    path('stud', Student_view.as_view(), name='student'),
    path('stud_add',views.student_add, name='s_add'),
    path('delete/<student_register_no>', views.delete_student, name='delete_student'),
    path('edit/<student_register_no>', views.edit_student, name='edit_student'),

]