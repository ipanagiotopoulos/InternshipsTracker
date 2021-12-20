from django import forms
from django.forms import ModelForm
from django.forms.widgets import (
    DateInput,
    EmailInput,
    HiddenInput,
    NumberInput,
    PasswordInput,
    TextInput,
)
from .models import *
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
import datetime as date


class StudentCreateForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text="Required", required=True)
    country = forms.CharField(max_length=30, required=True)
    city = forms.CharField(max_length=40, required=True)
    street_name = forms.CharField(max_length=100, required=True)
    street_no = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)], required=True
    )
    postal_code = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)], required=True
    )
    register_date = forms.DateTimeField(initial=date.datetime.now(), disabled=True)
    register_number = forms.CharField(max_length=6, min_length=3, required=True)

    class Meta:
        model = UndergraduateStudent
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "title",
            "father_name",
            "mother_name",
            "birth_day",
            "msisdn",
            "tel_no2",
            "department",
            "country",
            "city",
            "street_name",
            "street_no",
            "postal_code",
            "register_date",
        )
        widgets = {"register_date": DateInput()}


class StudentUpdateForm(UserChangeForm):
    # email = forms.EmailField(max_length=100, help_text="Required", required=True)
    country = forms.CharField(max_length=30, required=True)
    city = forms.CharField(max_length=40, required=True)
    street_name = forms.CharField(max_length=100, required=True)
    street_no = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)], required=True
    )
    postal_code = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)], required=True
    )
    register_date = models.DateTimeField(auto_now_add=True, blank=True)
    register_number = forms.CharField(max_length=6, min_length=3, required=True)

    class Meta:
        model = UndergraduateStudent
        fields = (
            "msisdn",
            "tel_no2",
            "country",
            "city",
            "street_name",
            "street_no",
            "postal_code",
        )


class SupervisorCreateForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text="Required", required=True)
    country = forms.CharField(max_length=30, required=True)
    city = forms.CharField(max_length=40, required=True)
    street_name = forms.CharField(max_length=100, required=True)
    street_no = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)], required=True
    )
    postal_code = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)], required=True
    )
    register_date = models.DateTimeField(auto_now_add=True, blank=True)
    register_number = forms.CharField(max_length=6, min_length=3, required=True)

    class Meta:
        model = Supervisor
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "title",
            "father_name",
            "mother_name",
            "birth_day",
            "msisdn",
            "tel_no2",
            "department",
            "country",
            "city",
            "street_name",
            "street_no",
            "postal_code",
        )
        widgets = {"register_date": DateInput()}


class CarrierNodeCreateForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text="Required", required=True)
    country = forms.CharField(max_length=30, required=True)
    city = forms.CharField(max_length=40, required=True)
    street_name = forms.CharField(max_length=100, required=True)
    street_no = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)], required=True
    )
    postal_code = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)], required=True
    )

    class Meta:
        model = CarrierNode
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "title",
            "father_name",
            "mother_name",
            "birth_day",
            "msisdn",
            "tel_no2",
            "carrier",
            "department",
            "country",
            "city",
            "street_name",
            "street_no",
            "postal_code",
        )
