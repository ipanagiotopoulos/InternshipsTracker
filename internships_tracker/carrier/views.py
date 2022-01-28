from braces.views import GroupRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, ListView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from dal import autocomplete as auto
from django.urls import reverse
from .forms import *
from .models import *
from internships_app.models import CarrierNode


# Create your views here.


class CreateAssignemtView(GroupRequiredMixin, CreateView):
    model = Assignment
    form_class = CreateAssignmentForm
    template_name = "assignment_create.html"
    success_url = "/"
    group_required = u"carrier_node"


class AssignmentListView(GroupRequiredMixin, DetailView):
    model = Assignment
    template_name = "assignments.html"

    def get_queryset(self):
        queryset = CarrierNode.objects.filter(Q(carrier=self.object.carrier))
        return queryset


class CreateCarrierConsentView(GroupRequiredMixin, CreateView):
    model = CarrierConsentForm
    form_class = CarrierConsentForm
    template_name = "carrier_consent_create.html"
    success_url = "/"
    group_required = u"carrier_node"


class TraineePositionListView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    model = TraineePosition
    group_required = u"carrier_node"
    template_name = "trainee_positions.html"
    context_object_name = "tps"

    def get_queryset(self):
        carrier_node = CarrierNode.objects.get(id=self.request.user.id)
        return TraineePosition.objects.filter(
            carrier_assignment__carrier=carrier_node.carrier
        )


class TraineePositionCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    model = TraineePosition
    form_class = CreateTraineePositionForm
    template_name = "trainee_position_create.html"
    success_url = "/carrier/traineepositions/list"
    group_required = u"carrier_node"

    # def get_test_func(self):
    #     traineePosition = self
    #     user = self.request.user
    #     carrier_node = CarrierNode.objects.filter(user=user)
    #     if traineePosition.carrier == carrier_node.carrier:
    #         return True
    #     return False

    def form_valid(self, form):
        carrier_node = CarrierNode.objects.get(id=self.request.user.id)
        ca = CarrierAssignmentPeriod.objects.get(carrier=carrier_node.carrier)
        a_p = ApplicationPeriod.objects.get(carrier=carrier_node.carrier)
        form.instance.carrier_assignment = ca
        form.instance.application_period = a_p
        return super().form_valid(form)


class TraineePositionDetailView(LoginRequiredMixin, DetailView):
    model = TraineePosition
    template_name = "trainee_positions.html"

    # def get_test_func(self):
    #     traineePosition = self
    #     user = self.request.user
    #     carrier_node = CarrierNode.objects.filter(user=user)
    #     if traineePosition.carrier == carrier_node.carrier:
    #         return True
    #     return False

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(TraineePosition, pk=pk_)


class TraineePositionDeleteView(LoginRequiredMixin, DeleteView):
    model = TraineePosition
    template_name = "trainee_position_delete.html"
    context_object_name = "/carrier/traineepositions/list"

    def get_test_func(self):
        traineePosition = self
        user = self.request.user
        carrier_node = CarrierNode.objects.filter(user=user)
        if traineePosition.carrier == carrier_node.carrier:
            return True
        return False

    def get_success_url(self):
        return reverse("carrier:traineeposition_list")


class TraineePositionUpdateView(GroupRequiredMixin, UpdateView):
    model = TraineePosition
    form_class = UpdateTraineePositionForm
    template_name = "trainee_position_update.html"
    success_url = "/carrier/traineepositions/list"
    group_required = u"carrier_node"

    # def test_func(self, request):
    #     traineePosition = self
    #     user = request.user
    #     if traineePosition.user == user:
    #         return True
    #     return False

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields["title"].initial = self.object.title
        form.fields["description"].initial = self.object.description
        # form.fields["description"].widget = forms.Textarea
        # form.fields["carrier_assignment"].widget = forms.HiddenInput()
        # form.fields["application_period"].widget = forms.HiddenInput()
        return form

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(TraineePosition, pk=pk_)


class TraineePositionAutocomplete(auto.Select2QuerySetView):
    def get_queryset(self):
        print(self.forwarded)
        tr1 = self.forwarded.get("trainee_position_1", None)
        tr2 = self.forwarded.get("trainee_position_2", None)
        tr3 = self.forwarded.get("trainee_position_3", None)
        tr4 = self.forwarded.get("trainee_position_4", None)
        tr5 = self.forwarded.get("trainee_position_5", None)
        qs = TraineePosition.objects.all().exclude(id=tr1)
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs
