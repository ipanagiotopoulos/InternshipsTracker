from django.core.validators import MaxValueValidator, MinValueValidator
from ThesisApp.models import Carrier, UndergraduateStudent, Supervisor
from django.db import models


# class CarrierDepartment(models.Model):
#     depatment_name: models.CharField(max_length=100)
#     carrier: models.ForeignKey(Carrier, on_delete=models.CASCADE)


class CarrierAssignmentPeriod(models.Model):
    carrier_name = models.CharField(max_length=120)
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return self.carrier_name


class AssignmentPeriod(models.Model):
    carrier_name = models.CharField(max_length=120)
    from_date = models.DateField()
    to_date = models.DateField()
    complementary = models.BooleanField(default=False)

    def __str__(self):
        return self.carrier_name


# Create your models here.


class ApplicationPeriod(models.Model):
    carrier_name = models.CharField(max_length=120)
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return self.carrier_name


class TraineePosition(models.Model):
    title = models.CharField(max_length=200)
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE)
    description = models.TextField(max_length=1500)
    application_period = models.ForeignKey(ApplicationPeriod, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Assignment(models.Model):
    date = models.DateField()
    trainee = models.OneToOneField(UndergraduateStudent, on_delete=models.CASCADE)
    trainee_position = models.ForeignKey(TraineePosition, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    assignment_period = models.ForeignKey(AssignmentPeriod, on_delete=models.CASCADE)

    def __str__(self):
        return self.trainee_position.title


class CarrierConsent(models.Model):
    date = models.DateField()
    carrier = models.OneToOneField(Carrier, on_delete=models.CASCADE)
    assignement_upon = models.OneToOneField(Assignment, on_delete=models.CASCADE)
    consent = models.BooleanField()

    def __str__(self):
        return self.assignement_upon.trainee_position.title


class CarrierAssesement(models.Model):
    date = models.DateField()
    assignement_upon = models.OneToOneField(Assignment, on_delete=models.CASCADE)
    comments = models.TextField(max_length=1000)
    grade = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    def __str__(self):
        return self.assignement_upon
