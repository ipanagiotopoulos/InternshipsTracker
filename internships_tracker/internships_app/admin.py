from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import *

# Register your models here.
# admin.site.unregister(User)
class SupervisorAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {
                "fields": (
                    "title",
                    "father_name",
                    "mother_name",
                    "birth_day",
                    "address",
                    "mobile_phone",
                    "home_phone",
                    "register_number",
                    "department",
                )
            },
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "fields": (
                    "title",
                    "father_name",
                    "mother_name",
                    "birth_day",
                    "address",
                    "mobile_phone",
                    "home_phone",
                    "register_number",
                    "department",
                )
            },
        ),
    )


class UndergraduateStudentAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {
                "fields": (
                    "title",
                    "father_name",
                    "mother_name",
                    "birth_day",
                    "address",
                    "mobile_phone",
                    "home_phone",
                    "register_number",
                    "department",
                )
            },
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "fields": (
                    "title",
                    "father_name",
                    "mother_name",
                    "birth_day",
                    "address",
                    "mobile_phone",
                    "home_phone",
                    "register_number",
                    "department",
                )
            },
        ),
    )


class CarrierNodeAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {
                "fields": (
                    "title",
                    "father_name",
                    "mother_name",
                    "birth_day",
                    "address",
                    "mobile_phone",
                    "home_phone",
                    "carrier",
                    "department",
                )
            },
        ),
    )

    # def has_add_permission(self, request):
    #     # if there's already an entry, do not allow adding
    #     carriers = Carrier.objects.all()
    #     carrier_nodes = CarrierNode.objects.all()
    #     carrier_node_carriers_names = []
    #     carrier_node_carriers = []
    #     for carrier_node in carrier_nodes:
    #         carrier_node_carriers_names.append(carrier_node.__dict__["carrier_id"])
    #         carrier_node_carriers.append(
    #             Carrier.objects.filter(
    #                 carrier_node_carriers_names.pop(
    #                     carrier_node_carriers_names.__sizeof__ - 1
    #                 )
    #                 == id
    #             )
    #         )

    #     for carrier_in in carriers:
    #         for carrier_node_in in carrier_node_carriers:
    #             count = CarrierNode.objects.filter(
    #                 carrier_node_in.official_name == carrier_in.official_name
    #             )
    #             if count == 0:
    #                 return True
    #             return False

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "fields": (
                    "title",
                    "father_name",
                    "mother_name",
                    "birth_day",
                    "address",
                    "mobile_phone",
                    "home_phone",
                    "carrier",
                    "department",
                )
            },
        ),
    )


admin.site.unregister(User)
admin.site.register(Supervisor, SupervisorAdmin)
admin.site.register(CarrierNode, CarrierNodeAdmin)
admin.site.register(UndergraduateStudent, UndergraduateStudentAdmin)
admin.site.register(Carrier)
admin.site.register(Address)
