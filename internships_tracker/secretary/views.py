from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
from datetime import date
from internships_app.models import UndergraduateStudent, User, CarrierNode, Supervisor
from applicant.models import Preference
from carrier.models import TraineePosition, CarrierAssignmentPeriod, Assignment, AssignmentPeriod
from .forms import *
from .filters import CarrierNodeFilter, UndergraduateStudentFilter, TraineePositionsFilter, PreferencesFilter, AssignmentFilter

deps = ['IT', 'ND', 'ESD', 'G']


class ApprovalRejectionUndergraduateStudentListView(ListView):
    model = UndergraduateStudent
    context_object_name = "students"
    template_name = "students_registrations.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'student_reg_message_result': self.request.session.pop('student_reg_message', None)
        }
        myFilter = UndergraduateStudentFilter(
            self.request.GET, queryset=self.get_queryset())
        context['filter'] = myFilter
        return context


def student_approval_rejection(request, pk):
    undergraduate_student = UndergraduateStudent.objects.filter(id=pk).first()
    req_user = User.objects.filter(
        id=undergraduate_student.user_ptr_id).first()
    context = {'req_user': req_user,
               'student': undergraduate_student}
    return render(request, "undergraduate_student_app_rjc.html", context)


def student_approve(request, pk):
    undergraduate_student = UndergraduateStudent.objects.filter(id=pk).first()
    user = User.objects.filter(id=undergraduate_student.user_ptr_id).first()
    user.is_active = True
    user.save()
    request.session['student_reg_message'] = "User: " + \
        str(user)+" has been activated!"
    return redirect('/secretary/students/registrations')


def student_reject(request, pk):
    undergraduate_student = UndergraduateStudent.objects.filter(id=pk).first()
    user = User.objects.filter(id=undergraduate_student.user_ptr_id).first()
    undergraduate_student.delete()
    user.delete()
    request.session['student_reg_message'] = "User: " + \
        str(user)+" has been deleted!"
    return redirect('/secretary/students/registrations')


class ApprovalRejectionCarrierNodeListView(ListView):
    model = CarrierNode
    context_object_name = "carriers"
    template_name = "carrier_registrations.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myFilter = CarrierNodeFilter(
            self.request.GET, queryset=self.get_queryset())
        context = {'filter': myFilter,
                   'carrier_node_reg_result': self.request.session.pop('carrier_node_reg', None)}
        return context


def carrier_node_approval_rejection(request, pk):
    carrier_node = CarrierNode.objects.filter(id=pk).first()
    req_user = User.objects.filter(id=carrier_node.user_ptr_id).first()
    context = {'req_user': req_user,
               'carrier_node': carrier_node}
    return render(request, "carrier_node_app_rjc.html", context)


def carrier_node_approve(request, pk):
    carrier_node = CarrierNode.objects.filter(id=pk).first()
    user = User.objects.filter(id=carrier_node.user_ptr_id).first()
    user.is_active = True
    user.save()
    request.session["carrier_node_reg"] = "User: " + \
        str(user)+" has been activated!"
    print(request.session["carrier_node_reg"])
    return redirect('/secretary/carriers/registrations')


def carrier_node_reject(request, pk):
    carrier_node = CarrierNode.objects.filter(id=pk).first()
    user = User.objects.filter(id=carrier_node.user_ptr_id).first()
    username = user.username
    carrier = carrier_node.carrier
    carrier.delete()
    carrier_node.delete()
    user.delete()
    request.session["carrier_node_reg"] = "User: " + \
        username+" has been deleted!"
    return redirect('/secretary/carriers/registrations')


class ApprovalTraineePositionsListView(ListView):
    model = TraineePosition
    context_object_name = "tps"
    template_name = "sec_trainee_positions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'trainee_position_message_result': self.request.session.pop('trainee_position_message', None),
            'period_message': self.request.session.pop('period_message', None)
        }
        myFilter = TraineePositionsFilter(
            self.request.GET, queryset=self.get_queryset())
        context = {'filter': myFilter}
        return context


class SecretaryTraineePositionDeleteView(DeleteView):
    model = TraineePosition
    template_name = "trainee_position_delete.html"
    context_object_name = "tp"

    def get_success_url(self):
        return "/secretary/carriers/trainee_positions"


def trainee_position_approval_rejection(request, pk):
    trainee_position = TraineePosition.objects.filter(id=pk).first()
    context = {'trainee_position': trainee_position}
    return render(request, "trainee_position_app_rjc.html", context)


def trainee_position_approve(request, pk):
    trainee_position = TraineePosition.objects.filter(id=pk).first()
    uni_department = trainee_position.carrier_assignment.department
    ca_per = CarrierAssignmentPeriod.objects.filter(
        department=uni_department).first()

    if ca_per != None:
        if ca_per.from_date <= date.today() <= ca_per.to_date:
            trainee_position.finalized = True
            trainee_position.save()
            print(trainee_position)
            return redirect('/secretary/carriers/trainee_positions')
        else:
            request.session['period_message'] = 'Application period not available for department: '+uni_department
            return redirect('/secretary/carriers/trainee_positions')
    else:
        request.session['period_message'] = 'Application  not found! for department: '+uni_department
        return redirect('/secretary/carriers/trainee_positions')


def carrier_node_reject(request, pk):
    carrier_node = CarrierNode.objects.filter(id=pk).first()
    user = User.objects.filter(id=carrier_node.user_ptr_id).first()
    username = user.username
    carrier = carrier_node.carrier
    carrier.delete()
    carrier_node.delete()
    user.delete()
    context = {'message': "User: "+username+" deleted!"}
    return render(request, "carrier_registrations.html", context)


class ApprovalPreferencesListView(ListView):
    model = Preference
    context_object_name = "preferences"
    template_name = "undergraduate_students_preferences.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myFilter = PreferencesFilter(
            self.request.GET, queryset=self.get_queryset())
        context = {'filter': myFilter}
        return context


class SecretaryPreferenceDeleteView(DeleteView):
    model = Preference
    template_name = "preference_delete.html"
    context_object_name = "tp"

    def get_success_url(self):
        return "/secretary/students/preferences"


class SecretaryPreferenceUpdateView(UpdateView):
    model = Preference
    context_object_name = "preference"
    template_name = "secretary_preference_update.html"
    form_class = SecrataryPreferenceForm
    success_url = "/secretary/students/preferences"

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        student = UndergraduateStudent.objects.get(
            user_ptr_id=self.request.user.id)
        for i in range(1, 5):
            form.fields[
                "trainee_position_" + str(i)
            ].queryset = TraineePosition.objects.filter(
                carrier_assignment__department=student.department
            )
        return form

    def get_object(self):
        student = UndergraduateStudent.objects.get(
            user_ptr_id=self.request.user.id)
        return Preference.objects.get(applicant=student)


class SecretaryPreferenceDeleteView(DeleteView):
    model = Preference
    template_name = "preference_delete.html"
    context_object_name = "preference"

    def get_success_url(self):
        return "/secretary/students/preferences"


def preferences_approve(request, pk):
    preference = Preference.objects.filter(id=pk).first()
    preference.finalized = True
    preference.save()
    return redirect('/secretary/students/preferences')


def preference_approval_rejection(request, pk):
    preference = Preference.objects.filter(id=pk).first()
    context = {'preference': preference}
    return render(request, "preference_app_rjc.html", context)


class AssingmentListView(ListView):
    model = Assignment
    context_object_name = "assignments"
    template_name = "sec_assignments.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myFilter = AssignmentFilter(
            self.request.GET, queryset=self.get_queryset())
        context = {'filter': myFilter}
        return context


class AssingmentCreateView(CreateView):
    model = Assignment
    context_object_name = "assignments"
    form_class = AssignmentSecretaryForm
    template_name = "sec_create_assignment.html"
    succes_url = "/secretary/assignments"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        department_request = self.request.GET.get("department")
        if department_request not in deps:
            raise Http404
        context['form'].fields['trainee'].queryset = UndergraduateStudent.objects.filter(
            department=department_request).all()
        context['form'].fields['trainee_position'].queryset = TraineePosition.objects.filter(
            carrier_assignment__department=department_request, finalized=True).all()
        context['form'].fields['supervisor'].queryset = Supervisor.objects.filter(
            department=department_request).all()
        context['form'].fields['assignment_period'].queryset = AssignmentPeriod.objects.filter(
            department=department_request).all()
        return context

    def get_success_url(self):
        department_request = self.request.GET.get("department")
        if department_request not in deps:
            raise Http404
        return "/secretary/assignments?department="+department_request

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        return form

    def form_valid(self, form):
        return super().form_valid(form)


class AssingmentUpdateView(UpdateView):
    model = Assignment
    context_object_name = "assignments"
    form_class = AssignmentSecretaryForm
    template_name = "create_assignment.html"
    succes_url = "/"

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        return form


class AssignmentDetailView(DetailView):
    model = Assignment
    context_object_name = "assignment"
    template_name = "sec_assignment.html"


class AssingmentDeleteView(DeleteView):
    model = Assignment
    context_object_name = "assignment"
    form_class = AssignmentSecretaryForm
    template_name = "sec_assignment_delete.html"
    succes_url = "/"

    def get_success_url(self):
        return "/secretary/assignments"


def assignment_approve(request, pk):
    assignment = Assignment.objects.filter(id=pk).first()
    assignment.finalized = "A"
    assignment.save()
    return redirect('/')


def assignment_reject(request, pk):
    assignment = Assignment.objects.filter(id=pk).first()
    assignment.assingment_status = "R"
    assignment.save()
    return redirect('/')
