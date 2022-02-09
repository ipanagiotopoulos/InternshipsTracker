from carrier.models import TraineePosition, ApplicationPeriod, CarrierAssignmentPeriod
from internships_app.models import CarrierNode
from django import template
import logging
from datetime import date

logger = logging.getLogger(__name__)

register = template.Library()


@register.simple_tag
def is_active(user):
    cn = CarrierNode.objects.get(id=user.id)
    cas = CarrierAssignmentPeriod.objects.filter(
        department=cn.carrier.department
    ).first()
    if cas == None:
        return False
    elif cas.from_date <= date.today() <= cas.to_date:
        return True
    return False

@register.simple_tag
def has_job_postings(user):
    cn = CarrierNode.objects.get(id=user.id)
    print("here is the carrier node:",cn)
    trainee_positions = TraineePosition.objects.filter(carrier = cn.carrier).first()
    print("here is the first trainee position", trainee_positions)
    if trainee_positions.exists():
        return True
    else:
        return False

@register.simple_tag
def is_application_approval_active(user):
    cn = CarrierNode.objects.get(id=user.id)
    cas = ApplicationPeriod.objects.filter(department=cn.carrier.department).first()
    if cas == None:
        return False
    elif cas.to_date < date.today():
        return True
    return False
