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
    path("consents/", views.CarrierConsentsListView.as_view(), name="carrier_consent"),
    path(
        "consents/create",
        views.CarrierConsentAcceptRejectView.as_view(),
        name="carrier_consent_accept_reject",
    ),
    path(
        "consents/<int:pk>/accept",
        views.CarrierConsentAcceptRejectView.as_view(),
        name="carrier_consent",
    ),
    path("assesments/", views.CarrierAssesmentsView.as_view(), name="assesments"),
    path(
        "assesments/<int:pk>/accept",
        views.CreateCarrierAssesmentView.as_view(),
        name="create_assesments",
    ),
    path("assignement", views.CreateAssignmentView.as_view(), name="assignement"),
]
