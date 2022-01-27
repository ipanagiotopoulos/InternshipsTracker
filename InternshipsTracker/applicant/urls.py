from django.urls import path
from . import views

app_name = "applicant"

urlpatterns = [
    path(
        "/application/<int:pk>",
        views.PreferenceView.as_view(),
        name="student_preference",
    ),
    path(
        "application/submit",
        views.CreatePreferenceView.as_view(),
        name="student_preference_submit",
    ),
    path(
        "positions",
        views.TraineePositionStudentListView.as_view(),
        name="student_all_positions",
    ),
]
