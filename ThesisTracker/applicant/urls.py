from django.urls import path
from . import views


urlpatterns = [
    path(
        "application/submit",
        views.CreatePreferenceView.as_view(),
        name="student_preference",
    ),
]
