import django_filters
from django import forms
from internships_app.models import CarrierNode, UndergraduateStudent
from carrier.models import TraineePosition, Assignment
from applicant.models import Preference


class CarrierNodeFilter(django_filters.FilterSet):

    class Meta:
        model = CarrierNode
        fields = {
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'is_active': ['exact'],
            'carrier__official_name': ['exact'],
        }


class UndergraduateStudentFilter(django_filters.FilterSet):

    class Meta:
        model = UndergraduateStudent
        fields = {
            'first_name': ['icontains'],
            'last_name':  ['icontains'],
            'register_number': ['exact'],
            'department': ['exact'],
        }


class TraineePositionsFilter(django_filters.FilterSet):

    class Meta:
        model = TraineePosition
        fields = {
            'title': ['icontains'],
            'finalized':  ['exact'],
            'job_code': ['icontains'],
            'carrier__official_name': ['exact'],
            'carrier_assignment__department': ['exact'],
            'no_id': ['exact'],
        }


class PreferencesFilter(django_filters.FilterSet):

    class Meta:
        model = Preference
        fields = {
            'applicant__first_name': ['icontains'],
            'applicant__last_name':  ['icontains'],
            'applicant__register_number': ['exact'],
        }


class AssignmentFilter(django_filters.FilterSet):

    class Meta:
        model = Assignment
        fields = {
            'trainee__first_name': ['icontains'],
            'trainee__last_name': ['icontains'],
            'trainee__department': ['exact'],
            'trainee_position__carrier__official_name': ['icontains'],
            'trainee_position__title':  ['exact'],
            'assignment_status': ['exact'],
        }
