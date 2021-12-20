from utils.decorators import group_required
from carrier.forms import (
    CreateTraineePositionForm,
    CarrierConsentForm,
    CreateAssignmentForm,
)
from carrier.models import TraineePosition, Assignment
from django.views.generic.edit import CreateView
from django.shortcuts import render
from dal import autocomplete as auto

# Create your views here.


class CreateAssignemtView(CreateView):
    model = Assignment
    form_class = CreateAssignmentForm
    template_name = "assignment_create.html"
    success_url = "/"
    group_required = "admin"

    def form_valid(self, form):
        # Preference.objects.create(
        #     user=User.objects.first(), slug="landing", flow_chatbot=f
        # )
        pref = form.save(commit=False)
        pref.save()
        return super().form_valid(form)


class CreateCarrierConsentView(CreateView):
    model = CarrierConsentForm
    form_class = CarrierConsentForm
    template_name = "carrier_consent_create.html"
    success_url = "/"
    group_required = "ThesisApp"

    def form_valid(self, form):
        # Preference.objects.create(
        #     user=User.objects.first(), slug="landing", flow_chatbot=f
        # )
        pref = form.save(commit=False)
        pref.save()
        return super().form_valid(form)


class CreateTraineePositionView(CreateView):
    model = TraineePosition
    form_class = CreateTraineePositionForm
    template_name = "trainee_position_create.html"
    success_url = "/"
    group_required = "ThesisApp"
    permission_required = ("ThesisApp.change_undergraduatestudent",)

    def form_valid(self, form):
        pref = form.save(commit=False)
        pref.save()
        return super().form_valid(form)


class TraineePositionAutocomplete(auto.Select2QuerySetView):
    def get_queryset(self):
        tr1 = self.forwarded.get("trainee_position_1", None)
        tr2 = self.forwarded.get("trainee_position_2", None)
        tr3 = self.forwarded.get("trainee_position_3", None)
        tr4 = self.forwarded.get("trainee_position_4", None)
        tr5 = self.forwarded.get("trainee_position_5", None)
        qs = TraineePosition.objects.all().exclude(id=tr1)
        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


auto.Select2QuerySetView
