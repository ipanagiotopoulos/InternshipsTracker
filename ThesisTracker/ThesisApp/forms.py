from django import forms
from django.forms import ModelForm
from django.forms.widgets import DateInput, EmailInput, NumberInput, PasswordInput, TextInput
from .models import Profile


class RegisterForm(ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=PasswordInput)
    birth_day = forms.DateField(widget=DateInput)
    email = forms.EmailField(widget=EmailInput)
    father_name = forms.CharField(widget=TextInput)
    mother_name = forms.CharField(widget=TextInput)
    registerno = forms.IntegerField(widget=NumberInput)
    tel_no1 = forms.IntegerField(widget=NumberInput)
    tel_no2 = forms.IntegerField(widget=NumberInput)
    class Meta:
        model = Profile
        fields = ["username", "password", "birth_day", "email", "msisdn", "tel_no2"]    