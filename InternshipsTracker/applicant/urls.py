from django.urls import path
from . import views

app_name = "applicant"

urlpatterns = [
    path(
        "application/submit",
        views.CreatePreferenceView.as_view(),
        name="student_preference",
    ),
]
