from django.urls import path
from . import views

app_name = "internships_app"

urlpatterns = [
    path(
        "changepassword/",
        views.PasswordsChangeView.as_view(),
        name="passwords_change",
    ),
    path(
        "register/undergraduate_student",
        views.UndergraduateStudentCreateView.as_view(),
        name="student_register",
    ),
    path(
        "register/supervisor",
        views.SupervisorCreateView.as_view(),
        name="supervisor_register",
    ),
    path(
         "register/carrier_node",
         views.CarrierNodeCreateView.as_view(),
         name="user_register",
     ),
    path(
        "carrier_node/edit/",
        views.CarrierNodeUpdateView.as_view(),
        name="carrier_node_edit",
    ),
    path(
        "carrier_node/my_carrier/",
        views.CarrierNodeUpdateView.as_view(),
        name="carrier_node_edit",
    ),
    path(
        "carrier_node/detail/",
        views.CarrierNodeDetaillView.as_view(),
        name="carrier_node_detail",
    ),
    path(
        "supervisor/edit/",
        views.SupervisorUpdateView.as_view(),
        name="supervisor_update",
    ),
    path(
        "supervisor/detail/",
        views.SupervisorDetailView.as_view(),
        name="student_detail",
    ),
    path(
        "secretarian/edit/",
        views.SecretarianUpdateView.as_view(),
        name="secretarian_update",
    ),
    path(
        "secretarian/detail/",
        views.SecretarianDetailView.as_view(),
        name="secretarian_detail",
    ),
    path("redirect",views.redirect_based_on_user, name="redirect_base"),
    path(
        "student/edit/",
        views.UnderGraduateStudentUpdateView.as_view(),
        name="student_update",
    ),
    path(
        "student/detail/",
        views.UnderGraduateStudentDetailView.as_view(),
        name="student_detail",
    ),
]
