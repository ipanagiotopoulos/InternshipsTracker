from django.views.generic.edit import UpdateView
from utils.decorators import group_required
from .forms import *
from .models import *
from django.views.generic import CreateView
from django.shortcuts import render
from dal import autocomplete as auto
from braces.views import GroupRequiredMixin


# Create your views here.


class CreateAssignemtView(GroupRequiredMixin, CreateView):
    model = Assignment
    form_class = CreateAssignmentForm
    template_name = "assignment_create.html"
    success_url = "/"
    group_required = u"carrier_node"


class CreateCarrierConsentView(GroupRequiredMixin, CreateView):
    model = CarrierConsentForm
    form_class = CarrierConsentForm
    template_name = "carrier_consent_create.html"
    success_url = "/"
    group_required = u"carrier_node"


class CreateTraineePositionView(GroupRequiredMixin, CreateView):
    model = TraineePosition
    form_class = CreateTraineePositionForm
    template_name = "trainee_position_create.html"
    success_url = "/"
    group_required = u"carrier_node"


# class UpdateTraineePositionView(GroupRequiredMixin, UpdateView):
#     model = TraineePosition
#     form_class = UpdateTraineePositionForm
#     template_name = "trainee_position_create.html"
#     success_url = "/"
#     group_required = u"carrier_node"


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
