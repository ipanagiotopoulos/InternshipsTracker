from InternshipsTracker.supervisor.models import SupervisorAssesment
from django.shortcuts import render

# Create your views here.
class CreateSupervisorAssesment(CreateView):
    model = SupervisorAssesment
    form_class = SupervisorAssesmentForm
    template_name = "preference_create.html"
    success_url = "/"
    group_required = u"student"

    class Meta:
        model = SupervisorAssesment
        fields = (
            "first_name",
            "last_name",
            "username",
            "msisdn",
            "tel_no2",
            "country",
            "city",
            "street_name",
            "street_no",
            "postal_code",
            "register_number",
        )
