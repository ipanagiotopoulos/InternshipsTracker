from django.urls import path
from . import views

app_name = "thesis_app"

urlpatterns = [
    path(
        "carrier/register/",
        views.CarrierNodeCreateView.as_view(),
        name="carrier_register",
    ),
    path(
        "carrier/edit/",
        views.CarrierNodeUpdateView.as_view(),
        name="carrier_register",
    ),
    path(
        "supervisor/register/",
        views.SupervisorCreateView.as_view(),
        name="supervisor_register",
    ),
    path(
        "supervisor/edit/",
        views.SupervisorUpdateView.as_view(),
        name="supervisor_update",
    ),
    path(
        "student/register/",
        views.UnderGraduateStudentCreateView.as_view(),
        name="student_register",
    ),
    path(
        "student/edit",
        views.UnderGraduateStudentUpdateView.as_view(),
        name="student_update",
    ),
]
