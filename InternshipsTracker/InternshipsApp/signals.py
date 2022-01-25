from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import Group
from .models import *


@receiver(post_save, sender=CarrierNode)
def carrier_node_add_to_default_group(sender, **kwargs):
    cn = kwargs["instance"]
    if kwargs["created"]:
        carrierNodeGroup, created = Group.objects.get_or_create(name="carrier_node")
        if created == True:
            carrierNodeGroup.save()
        cn.groups.add(carrierNodeGroup)


@receiver(post_save, sender=Supervisor)
def supervisor_add_to_default_group(sender, **kwargs):
    supervisor = kwargs["instance"]
    if kwargs["created"]:
        supervisorGroup, created = Group.objects.get_or_create(name="supervisor")
        if created == True:
            supervisorGroup.save()
        supervisor.groups.add(supervisorGroup)


@receiver(post_save, sender=UndergraduateStudent)
def student_add_to_default_group(sender, **kwargs):
    student = kwargs["instance"]
    if kwargs["created"]:
        studentGroup, created = Group.objects.get_or_create(name="student")
        if created == True:
            studentGroup.save()
        student.groups.add(studentGroup)
