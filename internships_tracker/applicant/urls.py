from django.urls import path
from . import views

app_name = "applicant"

urlpatterns = [
    path(
        "application/update",
        views.PreferenceUpdateView.as_view(),
        name="student_preference_update",
    ),
    path(
        "application/my",
        views.PreferenceDetailView.as_view(),
        name="student_preference_detail",
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
