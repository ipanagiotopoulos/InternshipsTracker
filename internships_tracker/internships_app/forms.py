from django import forms
from django.forms.widgets import (
    TextInput,
)
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from utils.validators import alphabetic, alphanumeric
from .models import *
from .enums import *
import datetime as date


class UndergraduateStudentForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=TextInput(attrs={"readonly": "readonly"}))
    last_name = forms.CharField(
        widget=TextInput(attrs={"readonly": "readonly"}))
    email = forms.EmailField(max_length=100, required=True, widget=TextInput(
        attrs={"readonly": "readonly"}))
    register_number = forms.CharField(
        widget=TextInput(attrs={"readonly": "readonly"}))
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES, required=False)
    uni_department = forms.CharField(
        max_length=100, min_length=3, required=True, widget=TextInput(attrs={"readonly": "readonly"}))
    country = forms.CharField(max_length=30, validators=[
                              alphabetic], required=True)
    city = forms.CharField(max_length=40, validators=[
                           alphabetic], required=True)
    street_name = forms.CharField(max_length=100, validators=[
                                  alphabetic], required=True)
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

    class Meta:
        model = UndergraduateStudent
        exclude = ['email']
        fields = (
            "first_name",
            "last_name",
            "email",
            "register_number",
            "uni_department",
            "department",
            "father_name",
            "mother_name",
            "birth_day",
            "mobile_phone",
            "home_phone",
            "country",
            "city",
            "street_name",
            "street_number",
            "postal_code",
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
    email = forms.EmailField(max_length=100, required=True, widget=TextInput(
        attrs={"readonly": "readonly"}))
    register_number = forms.CharField(max_length=6, min_length=3, validators=[
                                      alphanumeric], required=True, widget=TextInput(attrs={"readonly": "readonly"}))
    country = forms.CharField(max_length=30, validators=[
                              alphabetic], required=True)
    city = forms.CharField(max_length=40, validators=[
                           alphabetic], required=True)
    street_name = forms.CharField(max_length=100, validators=[
                                  alphabetic], required=True)
    street_number = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)], required=True
    )
    postal_code = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)], required=True
    )

    class Meta:
        model = UndergraduateStudent
        fields = (
            "first_name",
            "last_name",
            "email",
            "register_number",
            "mobile_phone",
            "home_phone",
            "country",
            "city",
            "street_name",
            "street_number",
            "postal_code",
        )


class SupervisorForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30, required=True, widget=TextInput(attrs={"readonly": "readonly"})
    )
    last_name = forms.CharField(
        max_length=30, required=True, widget=TextInput(attrs={"readonly": "readonly"})
    )
    email = forms.EmailField(max_length=100, required=True, widget=TextInput(
        attrs={"readonly": "readonly"}))
    register_number = forms.CharField(max_length=6, min_length=3, validators=[
                                      alphanumeric], required=True, widget=TextInput(attrs={"readonly": "readonly"}))
    country = forms.CharField(max_length=30, validators=[
                              alphabetic], required=True)
    city = forms.CharField(max_length=40, validators=[
                           alphabetic], required=True)
    street_name = forms.CharField(max_length=100, validators=[
                                  alphabetic], required=True)
    uni_department = forms.CharField(
        max_length=100, min_length=3, required=True, widget=TextInput(attrs={"readonly": "readonly"}))
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

    class Meta:
        model = Supervisor
        fields = (
            "first_name",
            "last_name",
            "email",
            "register_number",
            "uni_department",
            "father_name",
            "mother_name",
            "birth_day",
            "mobile_phone",
            "home_phone",
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
    register_number = forms.IntegerField(
        widget=TextInput(attrs={"readonly": "readonly"}))
    email = forms.EmailField(
        max_length=100, help_text="Required", required=True)
    country = forms.CharField(max_length=30, validators=[
                              alphabetic], required=True)
    city = forms.CharField(max_length=40, validators=[
                           alphabetic], required=True)
    street_name = forms.CharField(max_length=100, validators=[
                                  alphabetic], required=True)
    street_number = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)], required=True
    )
    postal_code = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)], required=True
    )

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


class SecratarianUpdateForm(UserChangeForm):
    password = None
    first_name = forms.CharField(
        max_length=30, required=True, widget=TextInput(attrs={"readonly": "readonly"})
    )
    last_name = forms.CharField(
        max_length=30, required=True, widget=TextInput(attrs={"readonly": "readonly"})
    )
    email = forms.EmailField(
        max_length=100, help_text="Required", required=True)
    country = forms.CharField(max_length=30, validators=[
                              alphabetic], required=True)
    city = forms.CharField(max_length=40, validators=[
                           alphabetic], required=True)
    street_name = forms.CharField(max_length=100, validators=[
                                  alphabetic], required=True)
    street_number = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)], required=True
    )
    postal_code = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)], required=True
    )

    class Meta:

        model = Secratarian
        fields = (
            "first_name",
            "last_name",
            "email",
            "mobile_phone",
            "home_phone",
            "country",
            "city",
            "street_name",
            "street_number",
            "postal_code",
        )


class CarrierNodeForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, validators=[alphabetic])
    last_name = forms.CharField(max_length=100, validators=[alphabetic])
    email = forms.EmailField(
        max_length=100, help_text="Required", required=True)
    uni_department = forms.CharField(
        max_length=100, min_length=3, required=True, widget=TextInput(attrs={"readonly": "readonly"}))
    mobile_phone = PhoneNumberField()
    country = forms.CharField(max_length=30, validators=[
                              alphabetic], required=True)
    home_phone = PhoneNumberField()
    city = forms.CharField(max_length=40, validators=[
                           alphabetic], required=True)
    street_name = forms.CharField(max_length=100, validators=[
                                  alphabetic], required=True)
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
    official_name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=2000)
    carrier_country = forms.CharField(max_length=30, validators=[
                                      alphabetic], required=True)
    carrier_city = forms.CharField(max_length=40, validators=[
                                   alphabetic], required=True)
    carrier_street_name = forms.CharField(
        max_length=100, validators=[alphabetic], required=True)
    carrier_street_number = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)], required=True
    )
    carrier_postal_code = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)], required=True
    )
    department_1 = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    department_2 = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    department_3 = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    department_4 = forms.ChoiceField(choices=DEPARTMENT_CHOICES)

    class Meta:
        model = CarrierNode
        fields = (
            "uni_department",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
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
            "official_name",
            "carrier_country",
            "carrier_city",
            "carrier_street_name",
            "carrier_street_number",
            "carrier_postal_code",
            "description",
            "department_1",
            "department_2",
            "department_3",
            "department_4"
        )


class CarrierNodeUpdateForm(UserChangeForm):
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
    country = forms.CharField(max_length=30, validators=[
                              alphabetic], required=True)
    city = forms.CharField(max_length=40, validators=[
                           alphabetic], required=True)
    street_name = forms.CharField(max_length=100, validators=[
                                  alphabetic], required=True)
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
            "postal_code"
        )
