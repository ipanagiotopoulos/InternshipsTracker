from .models import SupervisorAssesment
from django.views.generic import DetailView,ListView,CreateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse
from carrier.models import Assignment,CarrierAssesement
from internships_app.models import Supervisor
from applicant.models import InternshipReport

# Create your views here.
class AsssignmentListView(ListView):
    model= Assignment
    template_name = "supervisor_assignments.html"
    context_object_name="assignments"

    def get_queryset(self):
        supervisor = Supervisor.objects.get(id=self.request.user.id)
        return Assignment.objects.filter(
            supervisor=supervisor,finalized="A"
        )

class AsssignmentDetailView(UserPassesTestMixin,DetailView):
    model= Assignment
    template_name = "supervisor_assignment_detail.html"
    context_object_name="assignment"

    def test_func(self):
        supervisor = Supervisor.objects.get(id=self.request.user.id)
        if self.get_object().supervisor == supervisor:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assignment=self.get_object()
        context["assignment"]=assignment
        report=InternshipReport.objects.filter(assignment=assignment)
        if report.exists():
            context["report"]=report.first()
        carrier_assesment=CarrierAssesement.objects.filter(assignement_upon=assignment)
        if carrier_assesment.exists():
            context["carrier_assesment"]=carrier_assesment.first()
        supervisor_assesment=SupervisorAssesment.objects.filter(assignement_upon=assignment)
        if supervisor_assesment.exists():
            context["supervisor_assesment"]=supervisor_assesment.first()
        return context

class SupervisorAssesmentCreateView(CreateView):
    model = SupervisorAssesment
    fields=['comments','grade']
    template_name = "supervisor_assesment_create.html"

    def form_valid(self, form):
        form.instance.assignement_upon = Assignment.objects.get(id=self.kwargs.get('pk'))
        form.instance.supervisor=Supervisor.objects.get(id=self.request.user.id)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("supervisor:assignment_detail" ,kwargs={'pk':self.kwargs.get('pk')})