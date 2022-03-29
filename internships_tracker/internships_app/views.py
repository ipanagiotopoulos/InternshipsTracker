from django.shortcuts import render, redirect , get_object_or_404
from braces.views import GroupRequiredMixin, LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.urls import reverse
from .models import *
from .forms import *
from .utils import *
from .mixins import *


def redirect_based_on_user(request):
    dep_students_roles = {
        "hs",
        "it",
        "ds",
        "gs"
    }
    user = request.user
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
    return redirect('/', request=request)


       
    

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "../templates/change_password.html"
    success_url = reverse_lazy("home")


class UndergraduateStudentCreateView(LoginRequiredMixin,StudentExistsMixin,CreateView):
    template_name = "../templates/student_register.html"
    model = UndergraduateStudent
    form_class = UndergraduateStudentForm
    
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        user = User.objects.filter(id=self.request.user.id).first()
        if user:
                username = user.username
                form.fields['first_name'].initial = user.first_name
                form.fields['last_name'].initial = user.last_name
                form.fields["uni_department"].initial = user.uni_department
                form.fields["email"].initial = username
                form.fields["department"].initial = translate_uni_departments(user.uni_department)
                form.fields["department"].widget.attrs['disabled'] =True
                form.fields["register_number"].initial = username_to_register_number(username)
        return form

    def form_valid(self, form):
        undergraduate_student = form.save(commit=False)
        undergraduate_student.department = translate_uni_departments(self.request.user.uni_department)

        ad = Address.objects.create(
        country=form.cleaned_data["country"],
        city=form.cleaned_data["city"],
        street_name=form.cleaned_data["street_name"],
        street_number=form.cleaned_data["street_number"],
        postal_code=form.cleaned_data["postal_code"],
        )
        undergraduate_student.address = ad
        
        if self.request.user:
            request_user = self.request.user
            user_to_new = get_object_or_404(User, pk=request_user.id)
            undergraduate_student.user_ptr_id = user_to_new.pk
            undergraduate_student.__dict__.update(user_to_new.__dict__)
            undergraduate_student.save() 

        return super().form_valid(form)

    def get_success_url(self):
        if self.request.user:
            return '/accounts/logout'
        else:
            return '/'

class SupervisorCreateView(LoginRequiredMixin,SupervisorMixin,CreateView):
    template_name = "../templates/supervisor_register.html"
    model_name = Supervisor
    form_class = SupervisorForm

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        user = User.objects.filter(id=self.request.user.id).first()
        if user:
            username = user.username
            form.fields['first_name'].initial = user.first_name
            form.fields['last_name'].initial = user.last_name
            form.fields["uni_department"].initial = str(user.uni_department)
            form.fields["email"].initial = username
            form.fields["register_number"].initial = username_to_register_number(username)
        return form

    def form_valid(self, form):
        supervisor = form.save(commit=False)
        ad = Address.objects.create(
            country=form.cleaned_data["country"],
            city=form.cleaned_data["city"],
            street_name=form.cleaned_data["street_name"],
            street_number=form.cleaned_data["street_number"],
            postal_code=form.cleaned_data["postal_code"],
        )
        supervisor.address = ad
        if self.request.user:
            request_user = self.request.user
            user_to_new = get_object_or_404(User, pk=request_user.id)
            supervisor.user_ptr_id = user_to_new.pk
            supervisor.__dict__.update(user_to_new.__dict__)
            supervisor.save() 
        return super().form_valid(form)

    def get_success_url(self):
        if self.request.user:
            return '/accounts/logout'
        else:
            return '/'


class CarrierNodeCreateView(CarrierNodeMixin,CreateView):
    template_name = "../templates/carrier_node_register.html"
    model_name = CarrierNode
    form_class = CarrierNodeForm
    success_url ="/"
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields["uni_department"].initial = "NΟΝ"
        return form

    def form_valid(self, form):
        carrier_node = form.save(commit=False)
        user = User.objects.create(
          username = form.cleaned_data["email"],
          email = form.cleaned_data["email"],
          title = "Representative of "+form.cleaned_data["official_name"],
          uni_department = form.cleaned_data["uni_department"],
          first_name = form.cleaned_data["first_name"],
          last_name = form.cleaned_data["last_name"]
        )
        ad = Address.objects.create(
            country=form.cleaned_data["country"],
            city=form.cleaned_data["city"],
            street_name=form.cleaned_data["street_name"],
            street_number=form.cleaned_data["street_number"],
            postal_code=form.cleaned_data["postal_code"],
        )
        carrier_address =Address.objects.create(
          country=form.cleaned_data["carrier_country"],
          city=form.cleaned_data["carrier_city"],
          street_name=form.cleaned_data["carrier_street_name"],
          street_number=form.cleaned_data["carrier_street_number"],
          postal_code=form.cleaned_data["carrier_postal_code"],
        )
        carrier = Carrier.objects.create(
              official_name = form.cleaned_data["official_name"],
              description =  form.cleaned_data["description"],
              department_1 = form.cleaned_data["department_1"],
              department_2 = form.cleaned_data["department_2"],
              department_3 = form.cleaned_data["department_3"],
              department_4 = form.cleaned_data["department_3"],
              full_address = carrier_address
        )
        carrier_node.user_ptr_id = user.pk
        carrier_node.__dict__.update(user.__dict__)
        carrier_node.user_ptr_id = user.pk
        carrier_node.carrier = carrier
        carrier_node.address = ad
        carrier_node.save() 
        return super().form_valid(form)


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
        return Supervisor.objects.get(user_ptr_id=self.request.user.id)


class SupervisorDetailView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    model = Supervisor
    context_object_name = "supervisor"
    template_name = "supervisor.html"
    group_required = "supervisor"

    def get_object(self, queryset=None):
        return Supervisor.objects.get(user_ptr_id=self.request.user.id)


class CarrierNodeUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = CarrierNode
    form_class = CarrierNodeUpdateForm
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

class SecretarianDetailView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    model = Secratarian
    context_object_name = "secretarian"
    template_name = "secretarian.html"
    group_required = "secretarian"

    def get_object(self, queryset=None):
        secretarian = Secratarian.objects.get(user_ptr_id=self.request.user.id)
        return secretarian

class SecretarianUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = Secratarian
    form_class = SecratarianUpdateForm
    template_name = "secretarian_update.html"
    success_url = "/accounts/secretarian/detail"
    group_required = "secretarian"

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        return form
    
    def form_valid(self, form):
        sec = form.save(commit=False)
        Address.objects.update(
            country=form.cleaned_data["country"],
            city=form.cleaned_data["city"],
            street_name=form.cleaned_data["street_name"],
            street_number=form.cleaned_data["street_number"],
            postal_code=form.cleaned_data["postal_code"],
        )
        sec.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return Secratarian.objects.get(user_ptr_id=self.request.user.id)