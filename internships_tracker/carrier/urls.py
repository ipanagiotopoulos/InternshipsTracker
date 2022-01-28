from django.urls import path
from . import views

app_name = "carrier"
urlpatterns = [
    path(
        "traineepositions/autocomplete",
        views.TraineePositionAutocomplete.as_view(),
        name="traineeposition_autocomple",
    ),
    path(
        "traineepositions/list",
        views.TraineePositionListView.as_view(),
        name="traineeposition_list",
    ),
    path(
        "traineepositions/create",
        views.TraineePositionCreateView.as_view(),
        name="traineeposition_create",
    ),
    path(
        "traineepositions/<int:pk>/view",
        views.TraineePositionDetailView.as_view(),
        name="traineeposition",
    ),
    path(
        "traineepositions/<int:pk>/update",
        views.TraineePositionUpdateView.as_view(),
        name="traineeposition_update",
    ),
    path(
        "traineepositions/<int:pk>/delete",
        views.TraineePositionDeleteView.as_view(),
        name="traineeposition_delete",
    ),
    path("consents", views.CreateCarrierConsentView.as_view(), name="carrier_consent"),
    path("assignement", views.CreateAssignemtView.as_view(), name="assignement"),
    # path("assignements", views.AssignmentDetailView.as_view(), name="assignements"),
]
