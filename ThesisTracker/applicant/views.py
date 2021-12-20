from .forms import PreferenceCreateForm
from .models import Preference
from django.views.generic.edit import CreateView

# Create your views here.
class CreatePreferenceView(CreateView):
    model = Preference
    form_class = PreferenceCreateForm
    template_name = "preference_create.html"
    success_url = "/"
    permission_required = ("ThesisApp.change_undergraduatestudent",)

    def form_valid(self, form):
        pref = form.save(commit=False)
        pref.save()
        return super().form_valid(form)
