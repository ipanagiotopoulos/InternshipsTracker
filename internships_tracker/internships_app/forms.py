from django import forms
from django.forms.widgets import (
    DateInput,
    EmailInput,
    HiddenInput,
    NumberInput,
    PasswordInput,
    TextInput,
)
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from utils.validators import alphanumeric
from .models import *
import datetime as date


class UndergraduateStudentForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, help_text="Required", required=True)
    country = forms.CharField(max_length=30, required=True)
    city = forms.CharField(max_length=40, required=True)
    street_name = forms.CharField(max_length=100, required=True)
    msisdn = PhoneNumberField()
    tel_no2 = PhoneNumberField()
    street_no = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)], required=True
    )
    postal_code = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)], required=True
    )
    register_date = forms.DateTimeField()
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
            "register_number",
        )
        widgets = {
            "register_date": DateInput(),
            "birth_day": forms.TextInput(attrs={"class": "datetime-input"}),
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
    country = forms.CharField(max_length=30, required=True)
    city = forms.CharField(max_length=40, required=True)
    street_name = forms.CharField(max_length=100, required=True)
    street_no = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)], required=True
    )
    postal_code = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)], required=True
    )
    register_number = forms.CharField(max_length=6, min_length=3, required=True)

    class Meta:
        model = UndergraduateStudent
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "msisdn",
            "tel_no2",
            "country",
            "city",
            "street_name",
            "street_no",
            "postal_code",
            "register_number",
        )


class SupervisorForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, validators=[alphanumeric])
    last_name = forms.CharField(max_length=100, validators=[alphanumeric])
    email = forms.EmailField(max_length=100, help_text="Required", required=True)
    country = forms.CharField(max_length=30, required=True)
    city = forms.CharField(max_length=40, required=True)
    street_name = forms.CharField(max_length=100, required=True)
    street_no = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)], required=True
    )
    msisdn = PhoneNumberField()
    tel_no2 = PhoneNumberField()
    postal_code = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)], required=True
    )
    register_date = forms.DateField(
        label=("Register Date"),
        required=True,
        widget=forms.TextInput(attrs={"type": "date"}),
    )
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
        widgets = {
            "register_date": DateInput(),
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
    country = forms.CharField(max_length=30, required=True)
    city = forms.CharField(max_length=40, required=True)
    street_name = forms.CharField(max_length=100, required=True)
    street_no = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)], required=True
    )
    postal_code = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)], required=True
    )
    register_number = forms.CharField(max_length=6, min_length=3, required=True)

    class Meta:
        model = Supervisor
        fields = (
            "first_name",
            "last_name",
            "username",
            "msisdn",
            "tel_no2",
            "country",
            "city",
            "street_name",
            "street_no",
            "postal_code",
            "register_number",
        )


class CarrierNodeForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, validators=[alphanumeric])
    last_name = forms.CharField(max_length=100, validators=[alphanumeric])
    email = forms.EmailField(max_length=100, help_text="Required", required=True)
    country = forms.CharField(max_length=30, required=True)
    city = forms.CharField(max_length=40, required=True)
    street_name = forms.CharField(max_length=100, required=True)
    msisdn = PhoneNumberField()
    tel_no2 = PhoneNumberField()
    street_no = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)], required=True
    )
    postal_code = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)], required=True
    )
    carrrier = forms.ModelChoiceField(queryset=Carrier.objects.all())

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
        widgets = {
            "register_date": DateInput(),
            "birth_day": forms.DateTimeInput(
                attrs={
                    "class": "form-control datetimepicker-input",
                    "data-target": "#datetimepicker1",
                }
            ),
        }


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
            "first_name",
            "last_name",
            "username",
            "msisdn",
            "tel_no2",
            "country",
            "city",
            "street_name",
            "street_no",
            "postal_code",
        )
