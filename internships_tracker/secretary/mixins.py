from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from datetime import date
from internships_app.models import CarrierNode
from .models import *


class ApplicationPeriodFinished:

    def dispatch(self, request, *args, **kwargs):
        uni_department = self.request.GET.get('department', None)
        print("uni dep", uni_department)
        cas = CarrierAssignmentPeriod.objects.filter(
            department=uni_department
        ).first()
        print("here is the cas", cas)
        if cas and cas.from_date <= date.today() <= cas.to_date:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("/carrier/carrier-assignment/not-found")


class CarrierAssignmenetPeriodFinished:

    def dispatch(self, request, *args, **kwargs):
        uni_department = self.request.GET.get('department', None)
        print("uni dep", uni_department)
        cas = CarrierAssignmentPeriod.objects.filter(
            department=uni_department
        ).first()
        print("here is the cas", cas)
        if cas and cas.from_date <= date.today() <= cas.to_date:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("/carrier/carrier-assignment/not-found")
