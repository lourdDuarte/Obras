from django.forms import ModelForm, forms
from django.core.exceptions import ValidationError
from .models import Obras

class ObrasForm(ModelForm):
    
    class Meta:
        model = Obras
        fields = '__all__'
        required = ['sector', 'organismo_financiador', 'estado_obra', 'localidad', 'financiamiento', 'nombre', 'valor', 'descripcion', 'periodo_ejecucion', 'latitud', 'longitud']
        
        
