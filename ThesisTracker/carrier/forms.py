from django import forms
from .models import *


class CreateTraineePositionForm(forms.ModelForm):
    class Meta:
        model = TraineePosition
        fields = ("title", "carrier", "description", "application_period")


# class CarrierConsentForm(forms.ModelForm):
#     class Meta:
#         model = CarrierConsent
#         fields = ()  # to be done


# class CreateAssignmentForm(models.Model):
#     class Meta:
#         model = Assignment
#         fields = ()  # to be done
