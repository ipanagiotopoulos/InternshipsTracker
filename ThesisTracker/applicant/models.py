from carrier.models import TraineePosition
from ThesisApp.models import UndergraduateStudent
from django.db import models


class Preference(models.Model):
    applicant = models.ForeignKey(UndergraduateStudent, on_delete=models.CASCADE)
    trainee_position_1 = models.ForeignKey(
        TraineePosition,
        related_name="first_choice",
        verbose_name="First Choice",
        unique=True,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    trainee_position_2 = models.ForeignKey(
        TraineePosition,
        related_name="second_choice",
        verbose_name="Second Choice",
        unique=True,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    trainee_position_3 = models.ForeignKey(
        TraineePosition,
        related_name="third_choice",
        verbose_name="Third Choice",
        unique=True,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    trainee_position_4 = models.ForeignKey(
        TraineePosition,
        related_name="fourth_choice",
        verbose_name="Fourth Choice",
        unique=True,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    trainee_position_5 = models.ForeignKey(
        TraineePosition,
        related_name="fifth_choice",
        verbose_name="Fifth Choice",
        unique=True,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
