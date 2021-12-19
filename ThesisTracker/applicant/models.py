from carrier.models import TraineePosition
from ThesisApp.models import UndergraduateStudent
from django.db import models


class Preference(models.Model):
    applicant = models.ForeignKey(UndergraduateStudent, on_delete=models.CASCADE)
    trainee_position = models.ForeignKey(TraineePosition, on_delete=models.CASCADE)
