from django.shortcuts import render, redirect
from django.contrib import messages
from django.forms import ModelForm
from django.views.generic import CreateView, TemplateView
from Obras.models import Obras
from SectorObra.models import Sector
from Localidad.models import Localidad
from Organismo.models import Organismo
from EstadoObra.models import EstadoObra
from financiamiento.models import Financiamiento
from .forms import ObrasForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import yagmail


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
           
        
        return render(request, self.template_name, context)
    
    @login_required
    def view_dashboard(request):
        total_obras = Obras.objects.all().count()
        obras_finalizadas = Obras.objects.filter(estado_obra=3).count()
        obras_formosa = Obras.objects.filter(localidad=1).count()
        obras_parciales = Obras.objects.filter(estado_obra=4).count()
        obras_interrumpidas = Obras.objects.filter(estado_obra=5).count()
        obras_ideas = Obras.objects.filter(estado_obra = 1).count()
        obras_formulacion = Obras.objects.filter(estado_obra = 2).count()

        # ****** CONTEXTOS ******

        context = {'finalizadas': obras_finalizadas,
                   'total_obras': total_obras,
                   'obras_formosa': obras_formosa,
                   'obras_parciales': obras_parciales,
                   'obras_interrumpidas':obras_interrumpidas,
                   'obra_ideas': obras_ideas,
                   'obras_formulacion': obras_formulacion}
       
      
        return render(request, 'dashboard.html', context)
     
     
    @login_required
    def add_new_obra(request):
       
        if request.method == 'POST':
            form = ObrasForm(request.POST)
            if form.is_valid():
                
                form.save()
                messages.success(request, '¡Obra cargada con exito!')  # Define el mensaje de éxito
                return redirect('formulario')
            else:
                messages.error(request, form.errors)
                form = ObrasForm()
                
        estado = EstadoObra.objects.all()
        localidad = Localidad.objects.all()
        organismo = Organismo.objects.all()
        sector = Sector.objects.all()
        financiamiento = Financiamiento.objects.all()

        context = {'estado': estado,
                   'localidad': localidad,
                   'organismo': organismo,
                   'sector': sector,
                   'financiamiento': financiamiento}

    
       
        return render(request, 'formulario_data/form_obras.html', context)

    @login_required
    def listado_obras(request):
        obras = Obras.objects.all()
        context = {'obras':obras}
        return render(request,'listado_obras.html', context)
    
    @login_required
    def actualizar_obra(request,pk):
        
        obra = Obras.objects.get(id=pk)
        context = {'obra': obra}
        form = ObrasForm(instance=obra)
        if request.method == 'POST':   
             form = ObrasForm(request.POST, request.FILES,instance=obra)
             if form.is_valid():
                form.save()
                messages.success(request, '¡Obra actualizada con exito!')
                return redirect('listado-obras')
             else:
                 messages.error(request, form.errors)
                 return render (request,'actualizar.html',{'form':form})
        
        return render (request,'actualizar.html',{'form':form, **context})
    
    @login_required
    def eliminar_cartel(request, pk):
        request = Obras.objects.get(id=pk)
        request.delete()
        return redirect('listado-obras')

    def login(request):
        
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
              
                login(request, user)
                return redirect('listado-obras')
            else:
               
                return render(request, 'login.html', {'error': 'Invalid username and password'})


        return render(request,'login.html')



    def logout_view(request):
        logout(request)
        return redirect('login-obras')

    def solicitud_usuario(request):
        destinario = 'lourdes123duarte@gmail.com'
        password = 'badspsaurjkgkxvj'
        email = 'lourdes123duarte@gmail.com'
        
        if request.method == 'POST':

                nombre = request.POST['nombre_dependencia']
                correo = request.POST['correo']
                comentario = request.POST['comentario']
            
                if (len(nombre) and len(correo) ):
                    yag = yagmail.SMTP(user = email, password = password)

                    destinario = [destinario]

                    asunto = 'SISTEMA DE OBRAS: SOLICITUD DE NUEVO USUARIO '

                    mensaje = 'Se solicita un nuevo usuario para la dependencia: '+  nombre +'.' +'<br>Por el siguiente motivo: ' + comentario +'.' +'<br> Se adjunta el correo al cual enviar la informacion: ' + correo

                    yag.send(destinario,asunto, mensaje) 


                    messages.success(request, 'Solicitud enviada. Quede atento a su correo')  # Define el mensaje de éxito
                    return redirect('nuevo-usuario')
                else:
                    messages.error(request,'Los campos nombre y correo no pueden estar vacio')
                    return redirect('nuevo-usuario')
        
        return render(request, 'registrarse.html')


