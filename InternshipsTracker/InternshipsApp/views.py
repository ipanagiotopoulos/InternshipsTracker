from django.contrib.auth.models import User
from django.shortcuts import render
from braces.views import GroupRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect, request
from .forms import *
from django.views.generic import CreateView, UpdateView, DetailView
from .models import *
import datetime as date
from django.http import Http404


def map_model_name(model_type):
    model_dict = {
        "": "",
        "undergraduate_student": "UndergraduateStudent",
        "carrier_node": "CarrierNode",
        "supervisor": "Supervisor",
    }
    model_name = model_dict.get(model_type)
    if model_name:
        return model_name
    else:
        raise Http404


class UserCreateView(CreateView):
    paginate_by = 5
    template_name = "../templates/register.html"
    success_url = "/users/login"

    def get_form_class(self):
        my_model = self.kwargs.get("type", None)
        my_model = map_model_name(my_model)
        print(my_model)
        return eval("%sForm" % my_model)

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

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context["type"] = self.kwargs.get("type").replace("_", " ")
        return context


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


def handler404(request, *args, **kwargs):
    return render(request, "404.html", status=404)


def handler500(request, *args, **kwargs):
    return render(request, "500.html", status=500)
