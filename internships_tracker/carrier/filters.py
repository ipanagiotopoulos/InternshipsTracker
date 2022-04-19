import django_filters
from django import forms
from .models import TraineePosition, Assignment, CarrierConsent


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


# class CarrierConsentFilter(django_filters.FilterSet):

#     class Meta:
#         model = CarrierConsent
#         fields = {
#             'carrier__official_name': ['exact'],
#             # 'assignment_upon__trainee__first_name': ['icontains'],
#             # 'assignment_upon__trainee__last_name': ['icontains'],
#             # 'assignment_upon__trainee__register_number': ['icontains'],
#             # 'assignment_upon__trainee__department': ['exact'],
#             # 'assignment_upon__trainee_position__title': ['icontains'],
#             # 'assignment_upon__trainee_position__job_code': ['exact'],
#             # 'assignment_upon__trainee_position__no_id': ['exact'],
#         }
