from urllib import request
from django.shortcuts import render, redirect , get_object_or_404
from braces.views import GroupRequiredMixin, LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.http import Http404
from django.urls import reverse_lazy
from django.urls import reverse
from .models import *
from .forms import *
from .utils import *


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

def redirect_based_on_user(request):
    dep_students_roles = {
        "hs",
        "it",
        "ds",
        "gs"
    }
    user = request.user
    print("here is my user", user.username)
    if user.is_superuser == True:
        return redirect('/admin', request=request)
    if user.username.endswith("@hua.gr") :
        if user.username[0:2] in dep_students_roles:  
            if UndergraduateStudent.objects.filter(username=user.username).exists():
                 return redirect('/')
            return redirect('/accounts/register/undergraduate_student')
        if Supervisor.objects.filter(username=user.username).exists(): #he is not a student , so he is a supervisor
           return reverse('home')
        return redirect('/accounts/register/supervisor', request=request)
    return redirect('home', request=request)
    # we also have to check for secreatary

       
    

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "../templates/change_password.html"
    success_url = reverse_lazy("home")


class UserCreateView(CreateView):
    template_name = "../templates/register.html"

    def get_form_class(self):
        my_model = self.kwargs.get("type", None)
        my_model = map_model_name(my_model)
        return eval("%sForm" % my_model)
    
    def get_form(self, *args, **kwargs):
        user = User.objects.filter(id=self.request.user.id).first()
        print(user.__dict__)
        username = user.username
        form = super().get_form(*args, **kwargs)
        form.fields['first_name'] = user.first_name
        form.fields['last_name'] = user.last_name
        form.fields["uni_department"].initial = str(user.uni_department)
        form.fields["email"].initial = username
        form.fields["register_number"].initial = username_to_register_number(username)
        print("here is your form fields", form.fields)
        return form

    def form_valid(self, form):
        print("detail about form", form)
        us = form.save(commit=False)
        ad = Address.objects.create(
            country=form.cleaned_data["country"],
            city=form.cleaned_data["city"],
            street_name=form.cleaned_data["street_name"],
            street_number=form.cleaned_data["street_number"],
            postal_code=form.cleaned_data["postal_code"],
        )
        us.address = ad
        if self.request.user:
            request_user = self.request.user
            user_to_new = get_object_or_404(User, pk=request_user.id)
            us.user_ptr_id = user_to_new.pk
            us.__dict__.update(user_to_new.__dict__)
            us.save() 
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context["type"] = self.kwargs.get("type").replace("_", " ")
        return context

    def get_success_url(self):
        if self.request.user:
            return reverse('home')
        else:
            return redirect('/accounts/login')
class UnderGraduateStudentUpdateView(
    LoginRequiredMixin, GroupRequiredMixin, UpdateView
):
    model = UndergraduateStudent
    form_class = StudentUpdateForm
    template_name = "student_update.html"
    success_url = "/accounts/student/detail"
    group_required = "student"

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields["country"].initial = self.object.address.country
        form.fields["city"].initial = self.object.address.city
        form.fields["street_name"].initial = self.object.address.street_name
        form.fields["street_number"].initial = self.object.address.street_number
        form.fields["postal_code"].initial = self.object.address.postal_code
        form.fields["password"].widget = forms.HiddenInput()

        return form

    def form_valid(self, form):
        us = form.save(commit=False)
        Address.objects.update(
            country=form.cleaned_data["country"],
            city=form.cleaned_data["city"],
            street_name=form.cleaned_data["street_name"],
            street_number=form.cleaned_data["street_number"],
            postal_code=form.cleaned_data["postal_code"],
        )
        us.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return UndergraduateStudent.objects.get(user_ptr_id=self.request.user.id)


class UnderGraduateStudentDetailView(
    LoginRequiredMixin, GroupRequiredMixin, DetailView
):
    model = UndergraduateStudent
    context_object_name = "student"
    template_name = "student.html"
    group_required = "student"

    def get_object(self, queryset=None):
        return UndergraduateStudent.objects.get(user_ptr_id=self.request.user.id)


class SupervisorUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = Supervisor
    form_class = SupervisorUpdateForm
    template_name = "supervisor_update.html"
    success_url = "/account/supervisor/detail"
    group_required = "supervisor"

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields["country"].initial = self.object.address.country
        form.fields["city"].initial = self.object.address.city
        form.fields["street_name"].initial = self.object.address.street_name
        form.fields["street_number"].initial = self.object.address.street_number
        form.fields["postal_code"].initial = self.object.address.postal_code
        form.fields["password"].widget = forms.HiddenInput()
        return form

    def form_valid(self, form):
        us = form.save(commit=False)
        Address.objects.update(
            country=form.cleaned_data["country"],
            city=form.cleaned_data["city"],
            street_name=form.cleaned_data["street_name"],
            street_number=form.cleaned_data["street_number"],
            postal_code=form.cleaned_data["postal_code"],
        )
        us.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return Supervisor.objects.get(id=self.request.user.id)


class SupervisorDetailView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    model = Supervisor
    context_object_name = "supervisor"
    template_name = "supervisor.html"
    group_required = "supervisor"

    def get_object(self, queryset=None):
        return Supervisor.objects.get(id=self.request.user.id)


class CarrierNodeUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = UndergraduateStudent
    form_class = CarrierUpdateForm
    template_name = "carrier_node_update.html"
    success_url = "/accounts/carrier_node/detail"
    group_required = "carrier_node"

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields["country"].initial = self.object.address.country
        form.fields["city"].initial = self.object.address.city
        form.fields["street_name"].initial = self.object.address.street_name
        form.fields["street_number"].initial = self.object.address.street_number
        form.fields["postal_code"].initial = self.object.address.postal_code
        form.fields["password"].widget = forms.HiddenInput()
        return form

    def form_valid(self, form):
        us = form.save(commit=False)
        Address.objects.update(
            country=form.cleaned_data["country"],
            city=form.cleaned_data["city"],
            street_name=form.cleaned_data["street_name"],
            street_number=form.cleaned_data["street_number"],
            postal_code=form.cleaned_data["postal_code"],
        )
        us.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return CarrierNode.objects.get(user_ptr_id=self.request.user.id)


class CarrierNodeDetaillView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    model = CarrierNode
    context_object_name = "carrier_node"
    template_name = "carrier_node.html"
    group_required = "carrier_node"

    def get_object(self, queryset=None):
        return CarrierNode.objects.get(user_ptr_id=self.request.user.id)


class CarrierNodeCarrierDetailView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    model = Carrier
    context_object_name = "carrier"
    template_name = "carrier_node_carrier.html"
    group_required = "carrier_node"

    def get_object(self, queryset=None):
        carrier_node = CarrierNode.objects.get(user_ptr_id=self.request.user.id)
        return carrier_node.carrier


def handler404(request, *args, **kwargs):
    return render(request, "404.html", status=404)


def handler500(request, *args, **kwargs):
    return render(request, "500.html", status=500)
