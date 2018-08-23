from __future__ import unicode_literals
from django.contrib.postgres.fields import ArrayField

from django.db import models

# Create your models here.
class Data(models.Model):
    data = models.DateField()