from django.db import models
from django.db.models import Model

class Thing(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()