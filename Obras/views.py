from django.shortcuts import render
from django.forms import ModelForm
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

    def post(self, request, *args, **kwargs):
        sector = request.POST.get('selectSector')
        organismo = request.POST.get('selectOrganismo')
        estado = request.POST.get('selectEstado')
        localidad = request.POST.get('selectLocalidad')
        
        data = Obras.objects.all()
        if (organismo != '0'): 
            data = data.filter(organismo_financiador_id = organismo)
        if (sector != '0'): 
            data = data.filter(sector_id = sector)
            
        if (estado != '0'): 
            data = data.filter(estado_obra_id = estado)
           
        if (localidad != '0'): 
            data = data.filter(localidad_id = localidad)

        
        context = self.get_context_data()
        if (organismo != '0' or sector != '0' or estado != '0' or localidad != '0' ):
            context['data'] = data
            print("*********** DATA FINAL************")
            print(context['data'])
            print("*********** DATA FINAL************")
       
        
        
        return render(request, self.template_name, context)
    
        
    def view_dashboard(request):
        total_obras = Obras.objects.all().count()
        obras_finalizadas = Obras.objects.filter(estado_obra=3).count()
        obras_formosa = Obras.objects.filter(localidad=1).count()
        obras_parciales = Obras.objects.filter(estado_obra=4).count()
        obras_interrumpidas = Obras.objects.filter(estado_obra=5).count()
        obras_ideas = Obras.objects.filter(estado_obra = 1).count()
        obras_formulacion = Obras.objects.filter(estado_obra = 2).count()
        context = {'finalizadas': obras_finalizadas}
        context_total_obras = {'total_obras': total_obras}
        context_obras_formosa = {'obras_formosa': obras_formosa}
        context_obras_parciales = {'obras_parciales': obras_parciales}
        context_obras_interrumpidas = {'obras_interrumpidas':obras_interrumpidas}
        context_obras_ideas = {'obra_ideas': obras_ideas}
        context_obras_formulacion = {'obras_formulacion': obras_formulacion}
        context.update(context_total_obras)
        context.update(context_obras_formosa)
        context.update(context_obras_parciales)
        context.update(context_obras_interrumpidas)
        context.update(context_obras_ideas)
        context.update(context_obras_formulacion)
        return render(request, 'dashboard.html', context)
     
    








