from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from internships_app.models import Carrier, UndergraduateStudent, Supervisor
from carrier.enums import APPLICATION_STATUS
from internships_app.enums import (
    DEPARTMENT_CHOICES,
)

class CarrierAssignmentPeriod(models.Model):
    department = models.CharField(unique=True, max_length=3, choices=DEPARTMENT_CHOICES)
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return self.department

# Create your models here.
class ApplicationPeriod(models.Model):
    department = models.CharField(unique=True, max_length=3, choices=DEPARTMENT_CHOICES)
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return self.department


class AssignmentPeriod(models.Model):
    department = models.CharField(unique=True, max_length=3, choices=DEPARTMENT_CHOICES)
    from_date = models.DateField()
    to_date = models.DateField()
    complementary = models.BooleanField(default=False)

    def __str__(self):
        return self.department

class IntershipReportPeriod(models.Model):
    department = models.CharField(unique=True, max_length=3, choices=DEPARTMENT_CHOICES)
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return self.department

class TraineePosition(models.Model):
    title = models.CharField(max_length=200)
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE)
    carrier_assignment = models.ForeignKey(
        CarrierAssignmentPeriod, on_delete=models.CASCADE
    )
    description = models.TextField(max_length=1500)
    def __str__(self):
        return self.title + ":" + self.carrier.official_name


class Assignment(models.Model):
    date = models.DateField(auto_now_add=True)
    trainee = models.OneToOneField(UndergraduateStudent, on_delete=models.CASCADE)
    trainee_position = models.ForeignKey(TraineePosition, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    assignment_period = models.ForeignKey(AssignmentPeriod, on_delete=models.CASCADE)
    assignment_status = models.CharField(max_length=1, choices=APPLICATION_STATUS, default="P")

    def __str__(self):
        return self.trainee_position.title


class CarrierConsent(models.Model):
    date = models.DateField(auto_now_add=True)
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE)
    assignement_upon = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    consent = models.BooleanField()

    def __str__(self):
        return self.assignement_upon.trainee_position.title


class CarrierAssesement(models.Model):
    date = models.DateField(auto_now_add=True)
    assignement_upon = models.OneToOneField(Assignment, on_delete=models.CASCADE)
    comments = models.TextField(max_length=1000)
    grade = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    def __str__(self):
        return self.assignement_upon
