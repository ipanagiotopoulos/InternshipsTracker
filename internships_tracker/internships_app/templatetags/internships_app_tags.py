from internships_app.models import UndergraduateStudent,Supervisor,CarrierNode
from django import template
import logging

logger = logging.getLogger(__name__)

register = template.Library()


@register.simple_tag
def is_internal_proffessor_user(user):
    print(user.id)
    if UndergraduateStudent.objects.filter(username=user.id).exists():
        return True
    return False

def is_internal_student_user(user):
    print(user.id)
    if Supervisor.objects.filter(username=user.id).exists():
        return True
    return False


@register.simple_tag
def is_external_user(user):
    print(user.id)
    if CarrierNode.objects.filter(username=user.id).exists():
        return True
    return False