from django.db import models
from EstadoObra.models import EstadoObra
from Localidad.models import Localidad
from Organismo.models import Organismo
from SectorObra.models import Sector

# Create your models here.
class Obras(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    organismo_financiador = models.ForeignKey(Organismo,on_delete=models.CASCADE)
    estado_obra = models.ForeignKey(EstadoObra, on_delete=models.CASCADE)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=200, blank=True, null=True)
    valor = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField(null=True)
    periodo_ejecucion = models.CharField(max_length=200, blank=True, null=True)
    latitud = models.CharField(max_length=200, blank=True, null=True)
    longitud = models.CharField(max_length=200, blank=True, null=True)



    def __str__(self):
        return self.nombre