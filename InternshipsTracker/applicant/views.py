from carrier.models import TraineePosition
from django.views.generic import CreateView, DetailView
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404
from .forms import PreferenceCreateForm
from .models import Preference


# Create your views here.
class CreatePreferenceView(GroupRequiredMixin, CreateView):
    model = Preference
    form_class = PreferenceCreateForm
    template_name = "preference_create.html"
    success_url = "/"
    group_required = "student"

    # def form_valid(self, form):
    #     student_username = self.request.user
    #     some = Preference.object.get(student_username == applicant.user.username)
    #     print(some.__dict__)
    #     return super().form_valid(form)
    def get_form_kwargs(self):
        """Passes the request object to the form class.
        This is necessary to only display members that belong to a given user"""
        print(self.__dict__)
        kwargs = super(CreatePreferenceView, self).get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs


class PreferenceView(GroupRequiredMixin, DetailView):
    model = Preference
    context_object_name = "preference"
    template_name = "preference.html"
    group_required = "student"

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Preference, pk=pk_)
