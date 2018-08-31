from __future__ import unicode_literals
from django.contrib.postgres.fields import ArrayField

from django.db import models

# Create your models here.
class Data(models.Model):
    data_string = models.CharField(max_length=100, default=' ')
    data = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.data
