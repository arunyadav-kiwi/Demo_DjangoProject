from django import forms
from .models import CustomUser
class CustomRegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'mobile_no']



class LoginForm(forms.Form):
    # user log in form
    email  = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
