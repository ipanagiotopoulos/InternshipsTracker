from django.urls import path
from . import views

app_name = "thesis_app"

urlpatterns = [
    path(
        "register/",
        views.UserCreateView.as_view(),
        name="user_register",
    ),
    path(
        "register/<type>",
        views.UserCreateView.as_view(),
        name="user_register",
    ),
    path(
        "carrier/edit/",
        views.CarrierNodeUpdateView.as_view(),
        name="carrier_register",
    ),
    path(
        "supervisor/edit/",
        views.SupervisorUpdateView.as_view(),
        name="supervisor_update",
    ),
    # path(
    #     "student/register/",
    #     views.UnderGraduateStudentCreateView.as_view(),
    #     name="student_register",
    # ),
    path(
        "student/edit",
        views.UnderGraduateStudentUpdateView.as_view(),
        name="student_update",
    ),
]
