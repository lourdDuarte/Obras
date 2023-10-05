from django.db import models

# Create your models here.
class Financiamiento(models.Model):
    tipo_solicitud = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
            return self.tipo_solicitud