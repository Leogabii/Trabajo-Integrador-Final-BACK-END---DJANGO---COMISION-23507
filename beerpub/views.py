from django.shortcuts import render

# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView, TemplateView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
# Instanciamos el modelo 'Jugos' para poder usarlo en nuestras Vistas CRUD
from .models import Beerpub 

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms

class BeerpubPpal(TemplateView):
    Template_name= "index.html"

class BeerpubListado(ListView): 
    model = Beerpub # Llamamos a la clase 'Beerpub' que se encuentra en nuestro archivo 'models.py' 

class BeerpubCrear(SuccessMessageMixin, CreateView): 
    model = Beerpub # Llamamos a la clase 'Beerpub' que se encuentra en nuestro archivo 'models.py'
    form = Beerpub # Definimos nuestro formulario con el nombre de la clase o modelo 'Beerpub'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'beerpub' de nuestra Base de Datos 
    success_message = 'Momento Creado Correctamente !' # Mostramos este Mensaje luego de Crear 
 
    # Redireccionamos a la página principal luego de crear un registro
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class BeerpubDetalle(DetailView): 
    model = Beerpub # Llamamos a la clase 'Beerpub' que se encuentra en nuestro archivo 'models.py' 


class BeerpubActualizar(SuccessMessageMixin, UpdateView): 
    model = Beerpub # Llamamos a la clase 'Beerpub' que se encuentra en nuestro archivo 'models.py' 
    form = Beerpub # Definimos nuestro formulario con el nombre de la clase o modelo 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'beerpub' de nuestra Base de Datos 
    success_message = 'Momento Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar
 
    # Redireccionamos a la página principal luego de actualizar un registro 
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'


class BeerpubEliminar(SuccessMessageMixin, DeleteView): 
    model = Beerpub 
    form = Beerpub
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro
    def get_success_url(self): 
        success_message = 'Momento Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'


class AcercadePage(TemplateView):
    template_name = "acercade.html"


class ContactoPage(TemplateView):
    template_name = "contacto.html"


class FaqPage(TemplateView):
    template_name = "faq.html"


class LocalizacionPage(TemplateView):
    template_name = "localizacion.html"