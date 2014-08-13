from django.db import models

from core.models.base import BaseModel


# Create your models here.
class Gun(BaseModel):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)

    class Meta:
        app_label = 'core'