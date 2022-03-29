from django.shortcuts import  redirect
from django.core.exceptions import PermissionDenied
from internships_app.models import UndergraduateStudent,Supervisor,CarrierNode

class StudentExistsMixin:
    def dispatch(self, request, *args, **kwargs):
        user=request.user
        if not UndergraduateStudent.objects.filter(user_ptr_id=user.id).exists():
            return super().dispatch(self.request, *args, **kwargs)
        else:
            return redirect("/")

class SupervisorMixin:
    def dispatch(self, request, *args, **kwargs):
        user=request.user
        username =user.username
        if (not(username.startswith("it") or username.startswith("gs") or username.startswith("ds") or username.startswith("ds"))) and username.endswith("@hua.gr"):
            if not Supervisor.objects.filter(user_ptr_id=user.id).exists():
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect("/")
        else:
            raise PermissionDenied()

class CarrierNodeMixin:
    def dispatch(self, request, *args, **kwargs):
        user=request.user
        username =user.username
  
        if username.endswith("@hua.gr"):
            raise PermissionDenied()
        else:
            if(CarrierNode.objects.filter(user_ptr_id=user.id).exists()):
                return redirect("/")
            return super().dispatch(request, *args, **kwargs)