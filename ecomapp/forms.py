from django import forms
from django.forms import ModelForm
# from .models import Customer

class loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class SigninForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    email = forms.EmailField()
    # class Meta:
    #     model = Customer
    #     fields = '__all__'
    #     widgets = {'password': forms.PasswordInput()}