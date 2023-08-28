from django.db import models

# Create your models here.
class EstadoObra(models.Model):
    estado = models.CharField(max_length=150,blank=True,null=True)


    def __str__(self):
            return self.estado