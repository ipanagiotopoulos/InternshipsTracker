from .forms import PreferenceCreateForm
from .models import Preference
from django.views.generic import CreateView
from braces.views import GroupRequiredMixin

# Create your views here.
class CreatePreferenceView(GroupRequiredMixin, CreateView):
    model = Preference
    form_class = PreferenceCreateForm
    template_name = "preference_create.html"
    success_url = "/"
    group_required = u"student"
