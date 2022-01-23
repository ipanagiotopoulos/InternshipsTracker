import datetime
from InternshipsTracker.supervisor.models import SupervisorAssesment
from django import forms


class SupervisorAssesmentForm(forms.ModelForm):
    date = forms.DateField(initial=datetime.datetime.now(), widget=forms.HiddenInput())
    trainee_position = forms.CharField(max_length=100, required=True)
    comments = forms.CharField(max_length=5000, required=True)
    grade = forms.IntegerField(min=0, max=10)
    supervisor = forms.CharField(max_length=100)

    class Meta:
        model = SupervisorAssesment
        fields = ("date", "supervisor", "trainee_position", "comments", "grade")
