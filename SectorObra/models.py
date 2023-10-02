from django.db import models

# Create your models here.
class Sector(models.Model):
    nombre_sector = models.CharField(max_length=200, blank=True, null=True)
    icono = models.FileField(upload_to='icon/')


    def __str__(self):
            return self.nombre_sector