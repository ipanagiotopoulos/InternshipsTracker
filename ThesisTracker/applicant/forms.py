from django import forms
from applicant.models import Preference
from carrier.models import TraineePosition
from dal import autocomplete


class PreferenceCreateForm(forms.ModelForm):
    trainee_position_1 = forms.ModelChoiceField(
        required=True,
        queryset=TraineePosition.objects.all(),
        widget=autocomplete.ModelSelect2(
            url="carrier:traineeposition_autocomple",
            forward=[
                "trainee_position_2",
                "trainee_position_3",
                "trainee_position_4",
                "trainee_position_5",
            ],
        ),
    )
    trainee_position_2 = forms.ModelChoiceField(
        queryset=TraineePosition.objects.all(),
        widget=autocomplete.ModelSelect2(
            url="carrier:traineeposition_autocomple",
            forward=[
                "trainee_position_1",
                "trainee_position_3",
                "trainee_position_4",
                "trainee_position_5",
            ],
        ),
    )
    trainee_position_3 = forms.ModelChoiceField(
        queryset=TraineePosition.objects.all(),
        widget=autocomplete.ModelSelect2(
            url="carrier:traineeposition_autocomple",
            forward=[
                "trainee_position_2",
                "trainee_position_1",
                "trainee_position_4",
                "trainee_position_5",
            ],
        ),
    )
    trainee_position_4 = forms.ModelChoiceField(
        queryset=TraineePosition.objects.all(),
        widget=autocomplete.ModelSelect2(
            url="carrier:traineeposition_autocomple",
            forward=[
                "trainee_position_2",
                "trainee_position_3",
                "trainee_position_1",
                "trainee_position_5",
            ],
        ),
    )
    trainee_position_5 = forms.ModelChoiceField(
        queryset=TraineePosition.objects.all(),
        widget=autocomplete.ModelSelect2(
            url="/carrier/traineepositions/autocomplete",
            forward=[
                "trainee_position_2",
                "trainee_position_3",
                "trainee_position_4",
                "trainee_position_1",
            ],
        ),
    )

    class Meta:
        model = Preference
        fields = (
            "trainee_position_1",
            "trainee_position_2",
            "trainee_position_3",
            "trainee_position_4",
            "trainee_position_5",
        )
