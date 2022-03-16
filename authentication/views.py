from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import LoginForm
from .models import CustomUser
# Create your views here.


class Register(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self,request):
        if request.method == 'POST':
            #get form values
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            mobile_no = request.POST['mobile_no']
            password = request.POST['password']
            password1 = request.POST['password1']
    
            #check if passwords match
            if password == password1:
                        # check username
                    if CustomUser.objects.filter(username=username).exists():
                        messages.error(request, 'That username is taken')
                        return redirect('register')
                    else:
                        if CustomUser.objects.filter(email=email).exists(): 
                            messages.error(request,'That email is being used')
                            return redirect('register')
                        else:
                            user = CustomUser.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name, mobile_no=mobile_no)
                            user.save()
                            messages.success(request, 'you are registered')
                        return redirect('login')
                        #looks good
            else:       
                messages.error(request,'Passwords do not match')
                return redirect('register')
        else:
            return render(request, 'register.html')

class LoginView(FormView):
    # """login view"""

    form_class = LoginForm
    success_url = reverse_lazy('student')
    template_name = 'login.html'

    def form_valid(self, form):
        """ process user login"""
        credentials = form.cleaned_data
        user = authenticate(username=credentials['email'],
                            password=credentials['password'])
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)
        else:
            return HttpResponseRedirect(reverse_lazy('authentication:login'))

def Logout(request):
    """logout logged in user"""
    logout(request)
    return redirect('register')