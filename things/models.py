from django.db import models
from django.db.models import Model

class Thing(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    description = models.CharField(max_length=120, blank=True, unique=False)
    quantity = models.PositiveIntegerField(max_length=100)