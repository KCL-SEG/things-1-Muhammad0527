from django.db import models
from django.db.models import Model
from django.core.validators import MinValueValidator, MaxValueValidator

class Thing(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    description = models.CharField(max_length=120, blank=True, unique=False)
    quantity = models.PositiveIntegerField(validators=
                                           [MinValueValidator(0),MaxValueValidator(100)],
                                           unique=False)