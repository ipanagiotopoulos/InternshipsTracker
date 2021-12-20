from django import forms
from .models import *


class CreateTraineePositionForm(forms.ModelForm):
    class Meta:
        model = TraineePosition
        fields = ("title", "carrier", "description", "application_period")


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
