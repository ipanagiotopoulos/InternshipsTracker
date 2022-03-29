from ..models import Preference,InternshipReport
from internships_app.models import UndergraduateStudent
from django import template
import logging
from datetime import date

logger = logging.getLogger(__name__)

register = template.Library()


@register.simple_tag
def has_preference(user):
    student = UndergraduateStudent.objects.get(user_ptr_id=user.id)
    if Preference.objects.filter(applicant=student).exists():
        return True
    return False

@register.simple_tag
def has_internship_period_student(user):
    student = UndergraduateStudent.objects.get(user_ptr_id=user.id)
    if InternshipReport.objects.filter(assignment__trainee=student).exists():
        return True
    return False
