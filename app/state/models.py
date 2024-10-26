from model_utils.models import TimeStampedModel
from django.db import models

class State(TimeStampedModel):
    name = models.CharField('Nombre', max_length=50)

    def __str__(self):
        return f'{self.name}'