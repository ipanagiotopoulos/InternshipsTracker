import django_filters
from django import forms
from .models import TraineePosition, Assignment


class TraineePositionsFilter(django_filters.FilterSet):
    carrier_assignment__department = "IT"

    class Meta:
        model = TraineePosition
        fields = {

            'title': ['icontains'],
            'job_code': ['exact'],
            'no_id': ['exact'],
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


class ConsentFilter(django_filters.FilterSet):

    class Meta:
        model = Assignment
        fields = {
            'title': ['icontains'],
            'finalized':  ['exact'],
            'job_code': ['exact'],
            'no_id': ['exact'],
        }
