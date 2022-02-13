from django import forms
from django.forms.widgets import (
    TextInput,
)
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from utils.validators import alphabetic,alphanumeric
from .models import *
import datetime as date


class UndergraduateStudentForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,validators=[alphabetic],required=True)
    last_name = forms.CharField(max_length=100,validators=[alphabetic],required=True)
    email = forms.EmailField(max_length=100,help_text="Required", required=True)
    country = forms.CharField(max_length=30,validators=[alphabetic], required=True)
    city = forms.CharField(max_length=40,validators=[alphabetic], required=True)
    street_name = forms.CharField(max_length=100,validators=[alphabetic], required=True)
    mobile_phone = PhoneNumberField()
    home_phone = PhoneNumberField()
    street_number = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)], required=True
    )
    postal_code = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)], required=True
    )
    birth_day = forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={"type": "date"}),
    )
    register_number = forms.CharField(max_length=6, min_length=3,validators=[alphanumeric], required=True)

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
            "mobile_phone",
            "home_phone",
            "department",
            "country",
            "city",
            "street_name",
            "street_number",
            "postal_code",
            "register_number",
        )
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "autocomplete": "off",
                    "pattern": "[A-Za-z ]+",
                    "title": "Enter Characters Only ",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "autocomplete": "off",
                    "pattern": "[A-Za-z ]+",
                    "title": "Enter Characters Only ",
                }
            ),
        }


class StudentUpdateForm(UserChangeForm):
    first_name = forms.CharField(
        max_length=30, required=True, widget=TextInput(attrs={"readonly": "readonly"})
    )
    last_name = forms.CharField(
        max_length=30, required=True, widget=TextInput(attrs={"readonly": "readonly"})
    )
    username = forms.CharField(
        max_length=30, required=True, widget=TextInput(attrs={"readonly": "readonly"})
    )
    email = forms.EmailField(max_length=100, help_text="Required", required=True)
    country = forms.CharField(max_length=30,validators=[alphabetic], required=True)
    city = forms.CharField(max_length=40,validators=[alphabetic], required=True)
    street_name = forms.CharField(max_length=100,validators=[alphabetic],required=True)
    street_number = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)], required=True
    )
    postal_code = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)], required=True
    )
    register_number = forms.CharField(max_length=6, min_length=3,validators=[alphanumeric], required=True)

    class Meta:
        model = UndergraduateStudent
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "mobile_phone",
            "home_phone",
            "country",
            "city",
            "street_name",
            "street_number",
            "postal_code",
            "register_number",
        )


class SupervisorForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, validators=[alphabetic])
    last_name = forms.CharField(max_length=100, validators=[alphabetic])
    email = forms.EmailField(max_length=100, help_text="Required", required=True)
    country = forms.CharField(max_length=30,validators=[alphabetic], required=True)
    city = forms.CharField(max_length=40,validators=[alphabetic], required=True)
    street_name = forms.CharField(max_length=100,validators=[alphabetic], required=True)
    street_number = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)], required=True
    )
    mobile_phone = PhoneNumberField()
    home_phone = PhoneNumberField()
    postal_code = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)], required=True
    )
    birth_day = forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={"type": "date"}),
    )
    register_number = forms.CharField(max_length=6, min_length=3,validators=[alphanumeric], required=True)

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
            "mobile_phone",
            "home_phone",
            "department",
            "country",
            "city",
            "street_name",
            "street_number",
            "postal_code",
        )
        widgets = {
            "birth_day": forms.TextInput(attrs={"class": "datetime-input"}),
        }


class SupervisorUpdateForm(UserChangeForm):
    first_name = forms.CharField(
        max_length=30, required=True, widget=TextInput(attrs={"readonly": "readonly"})
    )
    last_name = forms.CharField(
        max_length=30, required=True, widget=TextInput(attrs={"readonly": "readonly"})
    )
    username = forms.CharField(
        max_length=30, required=True, widget=TextInput(attrs={"readonly": "readonly"})
    )
    email = forms.EmailField(max_length=100, help_text="Required", required=True)
    country = forms.CharField(max_length=30,validators=[alphabetic], required=True)
    city = forms.CharField(max_length=40,validators=[alphabetic], required=True)
    street_name = forms.CharField(max_length=100,validators=[alphabetic], required=True)
    street_number = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)], required=True
    )
    postal_code = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)], required=True
    )
    register_number = forms.CharField(max_length=6, min_length=3,validators=[alphanumeric], required=True)

    class Meta:
        model = Supervisor
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "mobile_phone",
            "home_phone",
            "country",
            "city",
            "street_name",
            "street_number",
            "postal_code",
            "register_number",
        )


class CarrierNodeForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, validators=[alphabetic])
    last_name = forms.CharField(max_length=100, validators=[alphabetic])
    email = forms.EmailField(max_length=100, help_text="Required", required=True)
    mobile_phone = PhoneNumberField()
    country = forms.CharField(max_length=30,validators=[alphabetic],required=True)
    home_phone = PhoneNumberField()
    city = forms.CharField(max_length=40,validators=[alphabetic],required=True)
    street_name = forms.CharField(max_length=100,validators=[alphabetic], required=True)
    street_number = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)], required=True
    )
    postal_code = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)], required=True
    )
    birth_day = forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={"type": "date"}),
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
            "mobile_phone",
            "home_phone",
            "department",
            "carrier",
            "country",
            "city",
            "street_name",
            "street_number",
            "postal_code",
        )


class CarrierUpdateForm(UserChangeForm):
    first_name = forms.CharField(
        max_length=30, required=True, widget=TextInput(attrs={"readonly": "readonly"})
    )
    last_name = forms.CharField(
        max_length=30, required=True, widget=TextInput(attrs={"readonly": "readonly"})
    )
    username = forms.CharField(
        max_length=30, required=True, widget=TextInput(attrs={"readonly": "readonly"})
    )
    # email = forms.EmailField(max_length=100, help_text="Required", required=True)
    country = forms.CharField(max_length=30,validators=[alphabetic], required=True)
    city = forms.CharField(max_length=40,validators=[alphabetic], required=True)
    street_name = forms.CharField(max_length=100,validators=[alphabetic], required=True)
    street_number = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)], required=True
    )
    postal_code = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)], required=True
    )

    class Meta:
        model = CarrierNode
        fields = (
            "first_name",
            "last_name",
            "username",
            "mobile_phone",
            "home_phone",
            "country",
            "city",
            "street_name",
            "street_number",
            "postal_code",
        )
