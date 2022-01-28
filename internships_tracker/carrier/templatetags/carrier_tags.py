from carrier.models import TraineePosition
from carrier.models import CarrierAssignmentPeriod
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
def get_carrier_asssignment_period(user):
    cn = CarrierNode.objects.get(id=user.id)
    cas = CarrierAssignmentPeriod.objects.filter(carrier=cn.carrier).first()
    return cas.carrier_assignment.from_date