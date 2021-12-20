from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.http import HttpResponseRedirect, request
from django.views.generic.detail import DetailView
from .forms import (
    CarrierNodeCreateForm,
    StudentCreateForm,
    StudentUpdateForm,
    SupervisorCreateForm,
)
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView
from .models import *
import datetime as date


class UnderGraduateStudentCreateView(CreateView):
    form_class = StudentCreateForm
    template_name = "student_create.html"
    success_url = "/login"

    def form_valid(self, form):
        us = form.save(commit=False)
        ad = Address.objects.create(
            country=form.cleaned_data["country"],
            city=form.cleaned_data["city"],
            street_name=form.cleaned_data["street_name"],
            street_no=form.cleaned_data["street_no"],
            postal_code=form.cleaned_data["postal_code"],
        )
        us.address = ad
        us.save()
        return super().form_valid(form)


# class UnderGraduateStudentDetailView(DetailView):
#     template_name = "student_detail.html"
#     queryset = UndergraduateStudent.objects.filter(self.)
#     def get_slug_field(self):
#         return 'user__username'


class UnderGraduateStudentUpdateView(PermissionRequiredMixin, UpdateView):
    model = UndergraduateStudent
    form_class = StudentUpdateForm
    template_name = "student_update.html"
    success_url = "/login"
    permission_required = ("ThesisApp.change_undergraduatestudent",)

    def form_valid(self, form):
        us = form.save(commit=False)
        ad = Address.objects.create(
            country=form.cleaned_data["country"],
            city=form.cleaned_data["city"],
            street_name=form.cleaned_data["street_name"],
            street_no=form.cleaned_data["street_no"],
            postal_code=form.cleaned_data["postal_code"],
        )
        us.address = ad
        us.save()
        return super().form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UnderGraduateStudentUpdateView, self).dispatch(*args, **kwargs)


class SupervisorCreateView(CreateView):
    form_class = SupervisorCreateForm
    template_name = "supervisor_create.html"
    success_url = "/login"

    def form_valid(self, form):
        sv = form.save(commit=False)
        ad = Address.objects.create(
            country=form.cleaned_data["country"],
            city=form.cleaned_data["city"],
            street_name=form.cleaned_data["street_name"],
            street_no=form.cleaned_data["street_no"],
            postal_code=form.cleaned_data["postal_code"],
        )
        sv.address = ad
        sv.save()
        return super().form_valid(form)


class CarrierNodeCreateView(CreateView):
    form_class = CarrierNodeCreateForm
    template_name = "carrier_node_create.html"
    success_url = "/login"

    def form_valid(self, form):
        cn = form.save(commit=False)
        ad = Address.objects.create(
            country=form.cleaned_data["country"],
            city=form.cleaned_data["city"],
            street_name=form.cleaned_data["street_name"],
            street_no=form.cleaned_data["street_no"],
            postal_code=form.cleaned_data["postal_code"],
        )
        cn.address = ad
        cn.save()
        return super().form_valid(form)
