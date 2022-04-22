from django.db import models
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

from .enums import DEPARTMENT_CHOICES, DEPARTMENT_CHOICES_CN
from utils.validators import alphanumeric, alphabetic


class Address(models.Model):
    country = models.CharField(max_length=30, validators=[alphabetic])
    city = models.CharField(max_length=40, validators=[alphabetic])
    street_name = models.CharField(max_length=100, validators=[alphabetic])
    street_number = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)]
    )
    postal_code = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)]
    )

    def __str__(self):
        return (
            self.country
            + ", "
            + self.city
            + ", "
            + self.street_name
            + ", "
            + str(self.street_number)
        )


class Carrier(models.Model):
    official_name = models.CharField(max_length=120, unique=True)
    full_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    department_1 = models.CharField(
        max_length=3, choices=DEPARTMENT_CHOICES_CN
    )  # each carrrier is for one department
    department_2 = models.CharField(
        max_length=3, choices=DEPARTMENT_CHOICES_CN
    )
    department_3 = models.CharField(
        max_length=3, choices=DEPARTMENT_CHOICES_CN
    )
    department_4 = models.CharField(
        max_length=3, choices=DEPARTMENT_CHOICES_CN
    )

    def __str__(self):
        return self.official_name


class User(AbstractUser):
    username = models.CharField('username', max_length=200, unique=True)
    email = models.EmailField('email address', unique=True)
    title = models.CharField('title', max_length=200)
    uni_department = models.CharField('uni_department', max_length=200)


class Profile(User):
    father_name = models.CharField(max_length=255, validators=[alphabetic])
    mother_name = models.CharField(max_length=255, validators=[alphabetic])
    birth_day = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    mobile_phone = PhoneNumberField(null=False, blank=False, unique=True)
    home_phone = PhoneNumberField(null=False, blank=False, unique=True)

    class Meta:
        abstract = True


class TokenManager(models.Manager):

    # get all expired tokens
    def get_expired(self):
        return Token.objects.filter(expiration__lt=timezone.now())

    # delete all expired tokens
    def delete_expired(self):
        expired_tokens = self.get_expired()
        for token in expired_tokens:
            token.delete()


class Token(models.Model):
    """
    model for token generators
    """
    token = models.CharField(max_length=200)
    expiration = models.DateTimeField('expiration date')
    externalMail = models.EmailField(max_length=100)
    username = models.CharField(max_length=100)
    type = models.CharField(max_length=20, default='activation')
    objects = TokenManager()

    def __str__(self):
        return "token %s used for %s belonging to user %s expires at %s" % (self.token,
                                                                            self.type, self.username, self.expiration)

    def has_expired(self):
        return self.expiration < timezone.now()


class CarrierNode(Profile):
    carrier = models.OneToOneField(Carrier, on_delete=models.CASCADE)
    department = models.CharField(max_length=150, validators=[
                                  alphanumeric])  # he needs ch

    class Meta:
        verbose_name = "Carrier Node"
        verbose_name_plural = "Carrier Nodes"


class UndergraduateStudent(Profile):
    register_number = models.CharField(max_length=10, validators=[
                                       alphanumeric], unique=True)
    department = models.CharField(max_length=3, choices=DEPARTMENT_CHOICES)

    class Meta:
        verbose_name = "Undergraduate Student"
        verbose_name_plural = "Undergraduate Students"

    def __str__(self):
        return str(self.register_number)+" "+self.first_name+" "+self.last_name+" "


class Supervisor(Profile):
    register_number = models.CharField(max_length=10, validators=[
                                       alphanumeric], unique=True)
    department = models.CharField(max_length=3, choices=DEPARTMENT_CHOICES)

    class Meta:
        verbose_name = "Supervisor"
        verbose_name_plural = "Supervisors"

    def __str__(self):
        return str(self.register_number)+" "+self.first_name+" "+self.last_name+" "


class Secratarian(Profile):
    department = models.CharField(max_length=3, choices=DEPARTMENT_CHOICES)
    alias_identifier = models.CharField(
        max_length=100, validators=[alphanumeric])

    class Meta:
        verbose_name = "Secretarian"
        verbose_name_plural = "Secretarians"

    def __str__(self):
        return str(self.alias_identifier)
