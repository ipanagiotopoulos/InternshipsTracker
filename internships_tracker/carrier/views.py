from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
from dal import autocomplete as auto
from django.urls import reverse
from .forms import *
from .models import *
from internships_app.models import CarrierNode
from django.db.models import Q
from .mixins import CarrierAssignmentRequiredMixin
from applicant.models import InternshipReport

# Create your views here.

def carrier_assignment_not_found(request):
    return render(request, 'carrier_assignment_not_found.html')

class TraineePositionListView(CarrierAssignmentRequiredMixin, ListView):
    model = TraineePosition
    template_name = "trainee_positions.html"
    context_object_name = "tps"

    def get_queryset(self):
        carrier_node = CarrierNode.objects.get(id=self.request.user.id)
        return TraineePosition.objects.filter(
            carrier_assignment__department=carrier_node.carrier.department
        )


class TraineePositionCreateView(CarrierAssignmentRequiredMixin, CreateView):
    model = TraineePosition
    form_class = TraineePositionForm
    template_name = "trainee_position_create.html"
    success_url = "/carrier/traineepositions/list"

    def form_valid(self, form):
        carrier_node = CarrierNode.objects.get(id=self.request.user.id)
        ca = CarrierAssignmentPeriod.objects.get(
            department=carrier_node.carrier.department
        )
        form.instance.carrier = carrier_node.carrier
        form.instance.carrier_assignment = ca
        return super().form_valid(form)


class TraineePositionDetailView(CarrierAssignmentRequiredMixin, DetailView):
    model = TraineePosition
    template_name = "trainee_positions.html"

class TraineePositionDeleteView(UserPassesTestMixin,CarrierAssignmentRequiredMixin, DeleteView):
    model = TraineePosition
    template_name = "trainee_position_delete.html"
    context_object_name = "tp"

    def test_func(self):
        carrier_node = CarrierNode.objects.get(id=self.request.user.id)
        if self.get_object().carrier == carrier_node.carrier:
            return True
        return False

    def get_success_url(self):
        return reverse("carrier:traineeposition_list")


class TraineePositionUpdateView(UserPassesTestMixin,CarrierAssignmentRequiredMixin, UpdateView):
    model = TraineePosition
    form_class = TraineePositionForm
    template_name = "trainee_position_update.html"
    success_url = "/carrier/traineepositions/list"
    group_required = u"carrier_node"

    def test_func(self):
        carrier_node = CarrierNode.objects.get(id=self.request.user.id)
        if self.get_object().carrier == carrier_node.carrier:
            return True
        return False

class AsssignmentListView( ListView):
    model= Assignment
    template_name = "assignments.html"
    context_object_name="assignments"

    def get_queryset(self):
        carrier_node = CarrierNode.objects.get(id=self.request.user.id)
        return Assignment.objects.filter(
            assignment_period__department=carrier_node.carrier.department,finalized="P"
        )

class AsssignmentDetailView(UserPassesTestMixin,DetailView):
    model= Assignment
    template_name = "assignment_detail.html"
    context_object_name="assignment"

    def test_func(self):
        carrier_node = CarrierNode.objects.get(id=self.request.user.id)
        if self.get_object().trainee_position.carrier == carrier_node.carrier:
            return True
        return False


def assignment_accept(request, pk):
    carrier_node = CarrierNode.objects.get(id=self.request.user.id)
    assignment = get_object_or_404(Assignment, pk=pk)
    if assignment.trainee_position.carrier == carrier_node.carrier:
        if CarrierConsent.objects.filter(assignement_upon=assignment).exists():
            context={
                'message' : 'Carrier consent already exists !',
                'assignment': assignment
            }
            return render(request,'assignment_detail.html',context)
        else:
            assignment.finalized="A"
            assignment.save()
            CarrierConsent.objects.create(carrier=assignment.trainee_position.carrier,assignement_upon=assignment,consent=True)
            return redirect('carrier:assignments')
    else:
        raise PermissionDenied()

def assignment_reject(request, pk):
    carrier_node = CarrierNode.objects.get(id=self.request.user.id)
    assignment = get_object_or_404(Assignment, pk=pk)
    if assignment.trainee_position.carrier == carrier_node.carrier:
        if CarrierConsent.objects.filter(assignement_upon=assignment).exists():
            context={
                    'message' : 'Carrier consent already exists !',
                    'assignment': assignment
                }
            return render(request,'assignment_detail.html',context)
        else:
            assignment.finalized="R"
            assignment.save()
            CarrierConsent.objects.create(carrier=assignment.trainee_position.carrier,assignement_upon=assignment,consent=False)
            return redirect('carrier:assignments')
    else:
        raise PermissionDenied()


class AcceptedAsssignmentListView( ListView):
    model= Assignment
    template_name = "accepted_assignments.html"
    context_object_name="assignments"

    def get_queryset(self):
        carrier_node = CarrierNode.objects.get(id=self.request.user.id)
        return Assignment.objects.filter(
            assignment_period__department=carrier_node.carrier.department,finalized="A"
        )

class AcceptedAsssignmentDetailView(UserPassesTestMixin,DetailView):
    model= Assignment
    template_name = "accepted_assignment_detail.html"
    context_object_name="assignment"

    def test_func(self):
        carrier_node = CarrierNode.objects.get(id=self.request.user.id)
        if self.get_object().trainee_position.carrier == carrier_node.carrier:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assignment=self.get_object()
        context["assignment"]=assignment
        report=InternshipReport.objects.filter(assignment=assignment)
        if report.exists():
            context["report"]=report.first()
        assesment=CarrierAssesement.objects.filter(assignement_upon=assignment)
        if assesment.exists():
            context["assesment"]=assesment.first()
        return context

class CarrierAssesementCreateView(CreateView):
    model = CarrierAssesement
    fields=['comments','grade']
    template_name = "carrier_assesment_create.html"

    def form_valid(self, form):
        form.instance.assignement_upon = Assignment.objects.get(id=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("carrier:accepted_assignment_detail" ,kwargs={'pk':self.kwargs.get('pk')})

class TraineePositionAutocomplete(auto.Select2QuerySetView):
    def get_queryset(self):
        print(self.forwarded)
        tr1 = self.forwarded.get("trainee_position_1", None)
        tr2 = self.forwarded.get("trainee_position_2", None)
        tr3 = self.forwarded.get("trainee_position_3", None)
        tr4 = self.forwarded.get("trainee_position_4", None)
        tr5 = self.forwarded.get("trainee_position_5", None)
        student = UndergraduateStudent.objects.get(user=self.request.user)

        qs = TraineePosition.objects.filter(
            carrier_assignment__department=student.department
        )
        if tr1:
            qs = qs.exclude(id=tr1)
        if tr2:
            qs = qs.exclude(id=tr2)
        if tr3:
            qs = qs.exclude(id=tr3)
        if tr4:
            qs = qs.exclude(id=tr4)
        if tr5:
            qs = qs.exclude(id=tr5)
        if self.q:

            qs = qs.filter(
                Q(title__icontains=self.q)
                | Q(carrier_assignment__carrier__official_name__icontains=self.q)
            )

        return qs

class CarrierDetailView(DetailView):
    model= Carrier
    template_name = "carrier_detail.html"
    context_object_name="carrier"

    def get_object(self):
        carrier_node = CarrierNode.objects.get(user=self.request.user)
        return carrier_node.carrier

class CarrierUpdateView(UpdateView):
    model= Carrier
    form_class=CarrierUpdateForm
    template_name = "carrier_update.html"
    context_object_name="carrier"

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields["country"].initial = self.object.full_address.country
        form.fields["city"].initial = self.object.full_address.city
        form.fields["street_name"].initial = self.object.full_address.street_name
        form.fields["street_number"].initial = self.object.full_address.street_number
        form.fields["postal_code"].initial = self.object.full_address.postal_code
        return form

    def form_valid(self, form):
        saved_form = form.save(commit=False)
        saved_form.full_address.country = form.cleaned_data["country"],
        saved_form.full_address.city = form.cleaned_data["city"],
        saved_form.full_address.street_name = form.cleaned_data["street_name"],
        saved_form.full_address.street_number = form.cleaned_data["street_number"],
        saved_form.full_address.postal_code = form.cleaned_data["postal_code"],
        saved_form.save()
        return super().form_valid(saved_form)

    def get_success_url(self):
        return reverse("carrier:carrier_detail" )

    def get_object(self):
        carrier_node = CarrierNode.objects.get(user=self.request.user)
        return carrier_node.carrier

