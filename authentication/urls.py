from django import views
from django.urls import path
from .views import LoginView, Register
from . import views
urlpatterns = [
    path('', Register.as_view(), name='register'),
    path('login/', LoginView.as_view() , name='login'),
    path('logout/', views.Logout, name='logout')
]