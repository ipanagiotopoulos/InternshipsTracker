from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
# admin.site.unregister(User)
class SupervisorAdmin(UserAdmin):
    fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "username",
                    "password",
                    "birth_day",
                    "father_name",
                    "mother_name",
                    "title",
                    "address",
                    "msisdn",
                    "tel_no2",
                    "register_number",
                    "register_date",
                    "department",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "username",
                    "password1",
                    "password2",
                    "birth_day",
                    "father_name",
                    "mother_name",
                    "title",
                    "address",
                    "msisdn",
                    "tel_no2",
                    "register_number",
                    "register_date",
                    "department",
                ),
            },
        ),
    )


class UndergraduateStudentAdmin(UserAdmin):
    fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "username",
                    "password",
                    "birth_day",
                    "father_name",
                    "mother_name",
                    "title",
                    "address",
                    "msisdn",
                    "tel_no2",
                    "register_number",
                    "register_date",
                    "department",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "username",
                    "password1",
                    "password2",
                    "birth_day",
                    "father_name",
                    "mother_name",
                    "title",
                    "address",
                    "msisdn",
                    "tel_no2",
                    "register_number",
                    "register_date",
                    "department",
                ),
            },
        ),
    )


class CarrierNodeAdmin(UserAdmin):
    fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "username",
                    "password",
                    "birth_day",
                    "father_name",
                    "mother_name",
                    "title",
                    "address",
                    "msisdn",
                    "tel_no2",
                    "carrier",
                    "department",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "username",
                    "password1",
                    "password2",
                    "birth_day",
                    "father_name",
                    "mother_name",
                    "title",
                    "address",
                    "msisdn",
                    "tel_no2",
                    "carrier",
                    "department",
                ),
            },
        ),
    )


admin.site.unregister(User)
admin.site.register(Supervisor, SupervisorAdmin)
admin.site.register(CarrierNode, CarrierNodeAdmin)
admin.site.register(UndergraduateStudent, UndergraduateStudentAdmin)
admin.site.register(Carrier)
admin.site.register(Address)
