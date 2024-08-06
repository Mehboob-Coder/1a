from django.core import validators
from django import forms


class StudentForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    # agree=forms.BooleanField(label_suffix=' ',label='i agree')
   
    