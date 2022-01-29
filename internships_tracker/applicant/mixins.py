from django.shortcuts import get_object_or_404, redirect
from internships_app.models import (
    UndergraduateStudent,
)
from .models import Preference


class ApplicationExistsRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        student = UndergraduateStudent.objects.get(user=user)
        if Preference.objects.filter(applicant=student).exists():
            return redirect("/studentapplications/application/update")
        else:
            return super().dispatch(request, *args, **kwargs)
