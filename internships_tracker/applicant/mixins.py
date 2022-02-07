from django.shortcuts import  redirect
from datetime import date
from internships_app.models import UndergraduateStudent
from carrier.models import ApplicationPeriod,IntershipReportPeriod

class ApplicationPeriodRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        user=request.user
        student = UndergraduateStudent.objects.get(id=user.id)
        ap = ApplicationPeriod.objects.filter(
            department=student.department
        ).first()
        if ap and ap.from_date <= date.today() <= ap.to_date:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("/studentapplications/application-period/not-found")

class InternshipReportPeriodRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        user=request.user
        student = UndergraduateStudent.objects.get(id=user.id)
        ap = IntershipReportPeriod.objects.filter(
            department=student.department
        ).first()
        if ap and ap.from_date <= date.today() <= ap.to_date:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("/studentapplications/report-period/not-found")
