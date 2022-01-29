from carrier.models import CarrierAssignmentPeriod
from internships_app.models import (
    UndergraduateStudent,
)
from carrier.models import TraineePosition
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from braces.views import GroupRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from .forms import PreferenceCreateForm
from .models import Preference
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from .mixins import ApplicationExistsRequiredMixin

# Create your views here.
class CreatePreferenceView(
    GroupRequiredMixin, LoginRequiredMixin, ApplicationExistsRequiredMixin, CreateView
):
    model = Preference
    form_class = PreferenceCreateForm
    template_name = "preference_create.html"
    success_url = "/"
    group_required = "student"

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        student = UndergraduateStudent.objects.get(user=self.request.user)
        for i in range(1, 5):
            form.fields[
                "trainee_position_" + str(i)
            ].queryset = TraineePosition.objects.filter(
                carrier_assignment__carrier__department=student.department
            )
        return form

    def form_valid(self, form):
        student = UndergraduateStudent.objects.get(pk=self.request.user.id)
        form.instance.applicant = student
        return super().form_valid(form)

    # def get_form_kwargs(self):
    #     """Passes the request object to the form class.
    #     This is necessary to only display members that belong to a given user"""
    #     print(self.__dict__)
    #     kwargs = super(CreatePreferenceView, self).get_form_kwargs()
    #     #kwargs["request"] = self
    #     return kwargs


class PreferenceUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = Preference
    context_object_name = "preference"
    template_name = "preference_update.html"
    group_required = "student"
    form_class = PreferenceCreateForm
    success_url = "/"

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        student = UndergraduateStudent.objects.get(user=self.request.user)
        for i in range(1, 5):
            form.fields[
                "trainee_position_" + str(i)
            ].queryset = TraineePosition.objects.filter(
                carrier_assignment__carrier__department=student.department
            )
        return form

    def get_object(self):
        student = UndergraduateStudent.objects.get(user=self.request.user)
        return Preference.objects.get(applicant=student)


class PreferenceDetailView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    model = Preference
    context_object_name = "preference"
    template_name = "preference_detail.html"
    group_required = "student"

    def get_object(self):
        student = UndergraduateStudent.objects.get(user=self.request.user)
        return Preference.objects.get(applicant=student)


class TraineePositionStudentListView(GroupRequiredMixin, ListView):
    model = TraineePosition
    context_object_name = "tps"
    template_name = "student_trainee_positions.html"
    group_required = u"student"

    def get_queryset(self):
        student = UndergraduateStudent.objects.get(id=self.request.user.id)
        trainee_pos = TraineePosition.objects.all()
        tps = []
        for trainee in trainee_pos:
            ca = CarrierAssignmentPeriod.objects.get(id=trainee.carrier_assignment_id)
            if ca.carrier.department == student.department:
                tps.append(trainee)

        print(tps)
        return tps
