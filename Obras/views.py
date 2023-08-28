from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from Obras.models import Obras

# Create your views here.

class ObrasTemplateView(TemplateView):
    
    template_name = "mapa.html"
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['ubicacion'] = Obras.objects.all()
        print(context['ubicacion'])
        return context 
    
        
     
    








