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

class SecretarianAdmin(UserAdmin):
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
                    "alias_identifier",
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
                    "department",
                    "alias_identifier"
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
admin.site.register(Secratarian,SecretarianAdmin)