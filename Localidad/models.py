from django.db import models

# Create your models here.
class Localidad(models.Model):
    nombre_localidad = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
            return self.nombre_localidad