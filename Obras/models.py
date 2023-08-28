from django.db import models

# Create your models here.
class Obras(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    valor = models.CharField(max_length=200, blank=True, null=True)
    localidad = models.CharField(max_length=200, blank=True, null=True)
    latitud = models.CharField(max_length=200, blank=True, null=True)
    longitud = models.CharField(max_length=200, blank=True, null=True)