"""cruddjango4 URL Configuration

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
from django.urls import path, include 
#from rest_framework.routers import DefaultRouter
from beerpub import viewsets
from django.conf import settings
from django.conf.urls.static import static


from beerpub.router import router
#from beerpub.router import router

from beerpub.views import BeerpubPpal, BeerpubListado, BeerpubDetalle, BeerpubCrear, BeerpubActualizar, BeerpubEliminar,AcercadePage, ContactoPage, FaqPage, LocalizacionPage
#from beerpub.views import BeerpubPpal, BeerpubListado, BeerpubDetalle, BeerpubCrear, BeerpubActualizar, BeerpubEliminar,AcercadePage, ContactoPage, FaqPage, LocalizacionPage


#agrego esto que me faltaba
app_name = "beerpub"

# mi_router = DefaultRouter()
# mi_router.register('beerpub', viewsets.BeerpubViewSet)

urlpatterns = [ 
    # path('',include(mi_router.urls)),

    #path('api-auth',include('rest_framework.urls')),
    
    path('admin/', admin.site.urls), 

    # La ruta 'indice' en donde se vera la pagina principal del proyecto front end
    path('', BeerpubPpal.as_view(template_name = "beerpub/index.html"), name="index"),
    
        # La ruta 'detalles' en donde mostraremos una página con los detalles de un registro 
    path('beerpub/detalle/<int:pk>', BeerpubDetalle.as_view(template_name = "beerpub/detalles.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo registro  
    path('beerpub/crear', BeerpubCrear.as_view(template_name = "beerpub/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un registro de la Base de Datos 
    path('beerpub/editar/<int:pk>', BeerpubActualizar.as_view(template_name = "beerpub/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un  registro de la Base de Datos 
    path('beerpub/eliminar/<int:pk>', BeerpubEliminar.as_view(), name='eliminar'), 

    # La ruta 'momento' en donde listamos todos los registros  de la Base de Datos
    path('beerpub/momentos', BeerpubListado.as_view(template_name = "beerpub/momentos.html"), name='leer'),

    # La ruta 'acercade' es donde mostramos el consumo de nuestra API
    path("beerpub/acercade/",AcercadePage.as_view(template_name = "beerpub/acercade.html"), name="acercade"),
 
    # La ruta 'contacto' es la pagina para contactarnos
    path("beerpub/contacto/", ContactoPage.as_view(template_name = "beerpub/contacto.html"), name="contacto"),

    # La ruta 'faq' es la pagina que nos muestra las preguntas frecuentes
    path("beerpub/faq/", FaqPage.as_view(template_name = "beerpub/faq.html"), name="faq"),

    # La ruta 'localizacion' es la pagina que brinda por un lado nuestros datos y por el otro el mapa de nuestra ubicacion
    path("beerpub/localizacion/", LocalizacionPage.as_view(template_name = "beerpub/localizacion.html"), name="localizacion"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns+=router.urls




# class AcercadePage(TemplateView):
#     template_name = "acercade.html"


# class ContactoPage(TemplateView):
#     template_name = "contacto.html"


# class FaqPage(TemplateView):
#     template_name = "faq.html"


# class LocalizacionPage(TemplateView):
#     template_name = "localizacion.html"


# from django.contrib import admin
# from django.urls import path

# from .views import IndexPage
# from .views import TiendaPage

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("", IndexPage.as_view(), name="index"),
#     path("tienda/", TiendaPage.as_view(), name="tienda"),
# ]