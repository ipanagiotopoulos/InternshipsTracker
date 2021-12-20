from django.urls import path
from . import views

app_name = "carrier"
urlpatterns = [
    path(
        "traineepositions/submit",
        views.CreateTraineePositionView.as_view(),
        name="student_preference",
    ),
    path(
        "traineepositions/autocomplete",
        views.TraineePositionAutocomplete.as_view(),
        name="traineeposition_autocomple",
    ),
]
