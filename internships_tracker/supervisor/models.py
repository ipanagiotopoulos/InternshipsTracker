from internships_app.models import Supervisor
from carrier.models import TraineePosition
from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class SupervisorAssesment(models.Model):
    date = models.DateField()
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    trainee_position = models.ForeignKey(TraineePosition, on_delete=models.CASCADE)
    comments = models.TextField(max_length=1500)
    grade = models.IntegerField(
        validators=[MaxValueValidator(0), MaxValueValidator(10)]
    )

    def __str__(self):
        return self.trainee_position
