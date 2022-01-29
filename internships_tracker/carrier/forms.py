from django import forms
from .models import *
from internships_app.models import Carrier


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


class CarrierConsentCreateForm(forms.ModelForm):
    class Meta:
        model = CarrierConsent
        fields = ("carrier", "assignement_upon", "date")


class CarrierConsentAcceptRejectForm(forms.ModelForm):
    # carrier = forms.ModelChoiceField(
    #     queryset=Carrier.objects.all(),
    #     required=True,
    #     widget=forms.TextInput(attrs={"readonly": "readonly"}),
    # )
    # assignement_upon = forms.ModelChoiceField(
    #     queryset=CarrierConsent.objects.all(),
    #     required=True,
    #     widget=forms.TextInput(attrs={"readonly": "readonly"}),
    # )
    consent = forms.TypedChoiceField(
        required=True,
        choices=((True, "Accept"), (False, "Reject")),
        widget=forms.RadioSelect,
    )

    class Meta:
        model = CarrierConsent
        fields = ("consent",)


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


class CreateCarrierAssementForm(forms.ModelForm):
    class Meta:
        model = CarrierAssesement
        fields = (
            "date",
            "assignement_upon",
            "comments",
            "grade",
        )


class SearchCarrierConsentsForms(forms.ModelForm):

    search = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Looking For ..."}), required=False
    )
    date = forms.ModelMultipleChoiceField(
        queryset=CarrierConsent.objects.values_list("date", flat=True).distinct(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )
    carrier = forms.ModelMultipleChoiceField(
        queryset=CarrierConsent.objects.values_list("date", flat=True).distinct(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    class Meta:
        fields = "__all__"

    def __init__(self, *args, request_data=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["search"].initial = request_data.GET.get("search", "")


class SearchCarrierAssesmentsForm(forms.ModelForm):

    search = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Looking For ..."}), required=False
    )
    date = forms.ModelMultipleChoiceField(
        queryset=CarrierConsent.objects.values_list("date", flat=True).distinct(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    class Meta:
        fields = "__all__"

    def __init__(self, *args, request_data=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["search"].initial = request_data.GET.get("search", "")
