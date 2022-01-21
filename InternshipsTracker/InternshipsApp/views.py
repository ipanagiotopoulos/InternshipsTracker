from django.contrib.auth.models import User
from django.shortcuts import render
from braces.views import GroupRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect, request
from .forms import *
from django.views.generic import CreateView, UpdateView, DetailView
from .models import *
import datetime as date


class UnderGraduateStudentCreateView(CreateView):
    form_class = StudentCreateForm
    template_name = "student_create.html"
    success_url = "/users/login"

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


class UnderGraduateStudentUpdateView(
    LoginRequiredMixin, GroupRequiredMixin, UpdateView
):
    model = UndergraduateStudent
    form_class = StudentUpdateForm
    template_name = "student_update.html"
    success_url = "/users/login"
    group_required = "student"

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields["country"].initial = self.object.address.country
        form.fields["city"].initial = self.object.address.city
        form.fields["street_name"].initial = self.object.address.street_name
        form.fields["street_no"].initial = self.object.address.street_no
        form.fields["postal_code"].initial = self.object.address.postal_code
        form.fields["password"].widget = forms.HiddenInput()

        return form

    def form_valid(self, form):
        us = form.save(commit=False)
        us.address.country = (form.cleaned_data["country"],)
        us.address.city = (form.cleaned_data["city"],)
        us.address.street_name = (form.cleaned_data["street_name"],)
        us.address.street_no = (form.cleaned_data["street_no"],)
        us.address.postal_code = (form.cleaned_data["postal_code"],)
        us.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return UndergraduateStudent.objects.get(id=self.request.user.id)


class SupervisorCreateView(CreateView):
    form_class = SupervisorCreateForm
    template_name = "supervisor_create.html"
    success_url = "/users/login"

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


class SupervisorUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = UndergraduateStudent
    form_class = SupervisorUpdateForm
    template_name = "student_update.html"
    success_url = "/users/login"
    group_required = "student"

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields["country"].initial = self.object.address.country
        form.fields["city"].initial = self.object.address.city
        form.fields["street_name"].initial = self.object.address.street_name
        form.fields["street_no"].initial = self.object.address.street_no
        form.fields["postal_code"].initial = self.object.address.postal_code
        form.fields["password"].widget = forms.HiddenInput()
        return form

    def form_valid(self, form):
        us = form.save(commit=False)
        us.address.country = (form.cleaned_data["country"],)
        us.address.city = (form.cleaned_data["city"],)
        us.address.street_name = (form.cleaned_data["street_name"],)
        us.address.street_no = (form.cleaned_data["street_no"],)
        us.address.postal_code = (form.cleaned_data["postal_code"],)
        us.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return UndergraduateStudent.objects.get(id=self.request.user.id)


class CarrierNodeCreateView(CreateView):
    form_class = CarrierNodeCreateForm
    template_name = "carrier_node_create.html"
    success_url = "/users/login"

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


class CarrierNodeUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = UndergraduateStudent
    form_class = SupervisorUpdateForm
    template_name = "student_update.html"
    success_url = "/users/login"
    group_required = "student"

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields["country"].initial = self.object.address.country
        form.fields["city"].initial = self.object.address.city
        form.fields["street_name"].initial = self.object.address.street_name
        form.fields["street_no"].initial = self.object.address.street_no
        form.fields["postal_code"].initial = self.object.address.postal_code
        form.fields["password"].widget = forms.HiddenInput()
        return form

    def form_valid(self, form):
        us = form.save(commit=False)
        us.address.country = (form.cleaned_data["country"],)
        us.address.city = (form.cleaned_data["city"],)
        us.address.street_name = (form.cleaned_data["street_name"],)
        us.address.street_no = (form.cleaned_data["street_no"],)
        us.address.postal_code = (form.cleaned_data["postal_code"],)
        us.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return UndergraduateStudent.objects.get(id=self.request.user.id)
