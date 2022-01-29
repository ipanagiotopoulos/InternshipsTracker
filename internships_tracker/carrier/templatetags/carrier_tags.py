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
    cas = CarrierAssignmentPeriod.objects.filter(carrier=cn.carrier).first()
    if cas == None:
        return False
    elif cas.from_date <= date.today() <= cas.to_date:
        return True
    return False


@register.simple_tag
def is_application_approval_active(user):
    cn = CarrierNode.objects.get(id=user.id)
    cas = ApplicationPeriod.objects.filter(carrier=cn.carrier).first()
    if cas == None:
        return False
    elif cas.to_date < date.today():
        return True
    return False
