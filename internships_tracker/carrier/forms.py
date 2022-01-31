from django import forms
from .models import *
from internships_app.models import Carrier


class TraineePositionForm(forms.ModelForm):
    title = forms.CharField(required=True, max_length=200, min_length=5)
    description = forms.CharField(
        required=True, max_length=1500, min_length=10, widget=forms.Textarea
    )
    class Meta:
        model = TraineePosition
        fields = (
            "title",
            "description",
        )

class CreateCarrierAssementForm(forms.ModelForm):
    class Meta:
        model = CarrierAssesement
        fields = (
            "assignement_upon",
            "comments",
            "grade",
        )

class CarrierUpdateForm(forms.ModelForm):
    country = forms.CharField(max_length=30, required=True)
    city = forms.CharField(max_length=40, required=True)
    street_name = forms.CharField(max_length=100, required=True)
    street_number = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)], required=True
    )
    postal_code = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)], required=True
    )
    class Meta:
        model = Carrier
        fields = (
            "official_name",
            "description",
            "department",
        )