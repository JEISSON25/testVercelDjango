from model_utils.models import TimeStampedModel

from django.db import models


class File(TimeStampedModel):
    file = models.FileField(blank=True, null=True)

    def __str__(self):
        return f'{self.file}'
