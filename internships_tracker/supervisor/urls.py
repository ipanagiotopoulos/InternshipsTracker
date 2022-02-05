from django.urls import path
from . import views

app_name = "supervisor"
urlpatterns = [
    path(
        "assignments",
        views.AsssignmentListView.as_view(),
        name="assignments",
    ),
    path(
        "assignments/<int:pk>/detail",
        views.AsssignmentDetailView.as_view(),
        name="assignment_detail",
    ),
    path(
        "assignments/<int:pk>/create-assesment",
        views.SupervisorAssesmentCreateView.as_view(),
        name="create_assesment",
    ),
]