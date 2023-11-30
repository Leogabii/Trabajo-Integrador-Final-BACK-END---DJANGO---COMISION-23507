from django.db import models
from django.utils import timezone
 
# Creación de campos de la tabla 'beerpub' 
class Beerpub(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=50)
    experiencia = models.CharField(max_length=100)
    img = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
         db_table = 'beerpub' # Le doy de nombre 'beerpub' a nuestra tabla en la Base de Datos 

#------------------------- agregado -----------------------------
    #"como el toString en Java"
    def __str__(self):
        return f" { Nombre: {self.nombre}, contacto: {self.contacto} }"
    
    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]         