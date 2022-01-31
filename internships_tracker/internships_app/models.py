from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from .enums import DEPARTMENT_CHOICES


class Address(models.Model):
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=40)
    street_name = models.CharField(max_length=100)
    street_number = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)]
    )
    postal_code = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)]
    )

    class Meta:
        unique_together = ("country", "city", "street_name", "street_number", "postal_code")

    def __str__(self):
        return (
            self.country
            + " "
            + self.city
            + " "
            + self.street_name
            + " "
            + str(self.street_number)
        )


class Carrier(models.Model):
    official_name = models.CharField(max_length=120, unique=True)
    full_address = models.OneToOneField(Address, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    department = models.CharField(
        max_length=3, choices=DEPARTMENT_CHOICES
    )  # each carrrier is for one department

    def __str__(self):
        return self.official_name


# we removed extends user
class Profile(User):
    user = models.OneToOneField(User, parent_link=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    birth_day = models.DateField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    mobile_phone = PhoneNumberField(null=False, blank=False, unique=True)
    home_phone = PhoneNumberField(null=False, blank=False, unique=True)

    class Meta:
        abstract = True


class CarrierNode(Profile):
    carrier = models.OneToOneField(Carrier, on_delete=models.CASCADE)
    department = models.CharField(max_length=150)  # he needs ch

    class Meta:
        verbose_name = "Carrier Node"
        verbose_name_plural = "Carrier Nodes"


class UndergraduateStudent(Profile):
    register_number = models.CharField(max_length=10, unique=True)
    register_date = models.DateField(auto_now_add=True)
    department = models.CharField(max_length=3, choices=DEPARTMENT_CHOICES)

    class Meta:
        verbose_name = "Undergraduate Student"
        verbose_name_plural = "Undergraduate Students"


class Supervisor(Profile):
    register_number = models.CharField(max_length=10, unique=True)
    register_date = models.DateField(auto_now_add=True)
    department = models.CharField(max_length=3, choices=DEPARTMENT_CHOICES)

    class Meta:
        verbose_name = "Supervisor"
        verbose_name_plural = "Supervisors"

    def __str__(self):
        return str(self.register_number)
