from django import template
from carrier.models import CarrierAssignmentPeriod
from InternshipsApp.models import CarrierNode
import logging
from datetime import date

logger = logging.getLogger(__name__)

register = template.Library()


@register.simple_tag
def is_active(user):
    cn = CarrierNode.objects.get(id=user.id)
    cas = CarrierAssignmentPeriod.objects.filter(carrier=cn.carrier).first()
    if cas.from_date <= date.today() <= cas.to_date:
        return True
    return False
