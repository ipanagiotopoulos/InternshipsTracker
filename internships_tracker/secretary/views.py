from django.shortcuts import render,redirect
from django.views.generic import  ListView,DeleteView,UpdateView
from internships_app.models import UndergraduateStudent, User, CarrierNode
from applicant.models import Preference
from carrier.models import TraineePosition
from .forms import SecrataryPreferenceForm
class ApprovalRejectionUndergraduateStudentListView(ListView):
    model = UndergraduateStudent
    context_object_name = "students"
    template_name = "students_registrations.html"

    def get_queryset(self):
        students = UndergraduateStudent.objects.filter().all()
        return students

def student_approval_rejection(request, pk):
    undergraduate_student = UndergraduateStudent.objects.filter(id=pk).first()
    req_user =  User.objects.filter(id=undergraduate_student.user_ptr_id).first()
    context = {'req_user':req_user, 
               'student':undergraduate_student}
    return render(request, "undergraduate_student_app_rjc.html", context)

def student_approve(request, pk):
    undergraduate_student = UndergraduateStudent.objects.filter(id=pk).first()
    user =  User.objects.filter(id=undergraduate_student.user_ptr_id).first()
    user.is_active = True
    user.save()
    context = {'message':"User: "+user.username+" activated!"}
    return render(request, "students_registrations.html", context)

def student_reject(request, pk):
    undergraduate_student = UndergraduateStudent.objects.filter(id=pk).first()
    user =  User.objects.filter(id=undergraduate_student.user_ptr_id).first()
    username = user.username
    undergraduate_student.delete()
    user.delete()
    context = {'message':"User: "+username+" deleted!"}
    return render(request, "students_registrations.html", context)

class ApprovalRejectionCarrierNodeListView(ListView):
    model = CarrierNode
    context_object_name = "carriers"
    template_name = "carrier_registrations.html"

    def get_queryset(self):
        carrier_nodes = CarrierNode.objects.filter().all()
        return carrier_nodes

def carrier_node_approval_rejection(request, pk):
    carrier_node = CarrierNode.objects.filter(id=pk).first()
    req_user =  User.objects.filter(id=carrier_node.user_ptr_id).first()
    context = {'req_user':req_user, 
               'carrier_node':carrier_node}
    return render(request, "carrier_node_app_rjc.html", context)

def carrier_node_approve(request, pk):
    carrier_node = CarrierNode.objects.filter(id=pk).first()
    user =  User.objects.filter(id=carrier_node.user_ptr_id).first()
    user.is_active = True
    user.save()
    context = {'message':"User: "+user.username+"activated!"}
    return redirect('/secretary/carriers/registrations')

def carrier_node_reject(request, pk):
    carrier_node = CarrierNode.objects.filter(id=pk).first()
    user =  User.objects.filter(id=carrier_node.user_ptr_id).first()
    username = user.username
    carrier = carrier_node.carrier
    carrier.delete()
    carrier_node.delete()
    user.delete()
    context = {'message':"User: "+username+" deleted!"}
    return redirect('/secretary/carriers/registrations')

class ApprovalTraineePositionsListView(ListView):
    model = TraineePosition
    context_object_name = "tps"
    template_name = "sec_trainee_positions.html"

    def get_queryset(self):
        trainee_positions = TraineePosition.objects.filter().all()
        return trainee_positions

class SecretaryTraineePositionDeleteView(DeleteView):
    model = TraineePosition
    template_name = "trainee_position_delete.html"
    context_object_name = "tp"

    def get_success_url(self):
        return "/secretary/carriers/trainee_positions"

def trainee_position_approval_rejection(request, pk):
    trainee_position = TraineePosition.objects.filter(id=pk).first()
    context = {'trainee_position':trainee_position}
    return render(request, "trainee_position_app_rjc.html", context)

def trainee_position_approve(request, pk):
    trainee_position = TraineePosition.objects.filter(id=pk).first()
    trainee_position.finalized = True
    trainee_position.save()
    return redirect('/secretary/carriers/trainee_positions')


def carrier_node_reject(request, pk):
    carrier_node = CarrierNode.objects.filter(id=pk).first()
    user =  User.objects.filter(id=carrier_node.user_ptr_id).first()
    username = user.username
    carrier = carrier_node.carrier
    carrier.delete()
    carrier_node.delete()
    user.delete()
    context = {'message':"User: "+username+" deleted!"}
    return render(request, "carrier_registrations.html", context)

class ApprovalPreferencesListView(ListView):
    model = Preference
    context_object_name = "preferences"
    template_name = "preferences.html"

    def get_queryset(self):
        preferences = Preference.objects.all()
        return preferences

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
        student = UndergraduateStudent.objects.get(user_ptr_id=self.request.user.id)
        for i in range(1, 5):
            form.fields[
                "trainee_position_" + str(i)
            ].queryset = TraineePosition.objects.filter(
                carrier_assignment__department=student.department
            )
        return form

    def get_object(self):
        student = UndergraduateStudent.objects.get(user_ptr_id=self.request.user.id)
        return Preference.objects.get(applicant=student)

class SecretaryPreferenceDeleteView(DeleteView):
    model = Preference
    template_name = "preference_delete.html"
    context_object_name = "tp"

    def get_success_url(self):
        return "/secretary/students/preferences"


def preferences_approve(request, pk):
    preference = Preference.objects.filter(id=pk).first()
    preference.finalized = True
    preference.save()
    return redirect('/secretary/students/preferences')

def preference_approval_rejection(request, pk):
    preference = Preference.objects.filter(id=pk).first()
    context = {'preference':preference}
    return render(request, "preference_app_rjc.html", context)