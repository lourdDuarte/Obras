"""obrasFormosa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Obras.views import ObrasTemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('mapa/', ObrasTemplateView.as_view(template_name="mapa.html"), name = 'mapa'),
    path('dashboard/', ObrasTemplateView.view_dashboard, name='dashboard'),
    path('formulario/', ObrasTemplateView.add_new_obra, name='formulario'),
    path('actualizar/<str:pk>/', ObrasTemplateView.actualizar_obra, name='actualizar'),
    path('listado-obras/', ObrasTemplateView.listado_obras, name='listado-obras'),
    path('eliminar/<str:pk>/', ObrasTemplateView.eliminar_cartel, name='eliminar'),
    path('login-obras/', ObrasTemplateView.login, name='login-obras'),
    path('logout-obras/', ObrasTemplateView.logout_view, name='logout-obras'),
    path('nuevo-usuario/', ObrasTemplateView.solicitud_usuario, name='nuevo-usuario')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
