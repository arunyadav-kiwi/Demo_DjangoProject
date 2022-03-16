from django import forms
from .models import BookData

class BookForm(forms.ModelForm):
    class Meta:
        model = BookData
        fields = '__all__'