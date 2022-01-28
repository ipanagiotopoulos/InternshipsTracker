from django import forms
from .models import *


class CreateTraineePositionForm(forms.ModelForm):
    class Meta:
        model = TraineePosition
        fields = ("title", "description", "carrier_assignment", "application_period")


class UpdateTraineePositionForm(forms.ModelForm):
    title = forms.CharField(required=True, max_length=200, min_length=5)
    description = forms.CharField(
        required=True, max_length=1500, min_length=10, widget=forms.Textarea
    )

    class Meta:
        model = TraineePosition
        fields = ("title", "description")


class CarrierConsentForm(forms.ModelForm):
    class Meta:
        model = CarrierConsent
        fields = ("carrier", "consent", "assignement_upon", "date")


class CreateAssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = (
            "trainee",
            "trainee_position",
            "supervisor",
            "assignment_period",
            "date",
        )
