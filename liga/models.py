from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Time(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    sigla_estado = models.CharField(max_length=2, blank=True, null=True)
    numero_de_torcedores = models.IntegerField(blank=True, null=True)
    numero_de_titulos = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.nome