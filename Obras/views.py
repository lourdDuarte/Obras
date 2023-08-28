from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from Obras.models import Obras
from SectorObra.models import Sector
from Localidad.models import Localidad
from Organismo.models import Organismo
from EstadoObra.models import EstadoObra


# Create your views here.

class ObrasTemplateView(TemplateView):
    
    template_name = "mapa.html"
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['ubicacion'] = Obras.objects.all()
        context['estado'] = EstadoObra.objects.all()
        context['localidad'] = Localidad.objects.all()
        context['organismo'] = Organismo.objects.all()
        context['sector'] = Sector.objects.all()
    
        return context 
    
        
     
    








