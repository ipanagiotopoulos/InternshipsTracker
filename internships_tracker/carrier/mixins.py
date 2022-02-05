from .models import *
from internships_app.models import CarrierNode
from django.shortcuts import  redirect
from datetime import date


class CarrierAssignmentRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        user=request.user
        cn = CarrierNode.objects.get(id=user.id)
        cas = CarrierAssignmentPeriod.objects.filter(
            department=cn.carrier.department
        ).first()
        if cas and cas.from_date <= date.today() <= cas.to_date:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("/carrier/carrier-assignment/not-found")
