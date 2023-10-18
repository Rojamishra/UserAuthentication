from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class SignupForm(UserCreationForm):
    password2 = forms.CharField(label='Re-Type Password:',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'username':'User Name:','first_name':'First Name:','last_name':'Last Name:','email':'Email:'}