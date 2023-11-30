from django.contrib import admin
from django.contrib.admin import ModelAdmin

# importo el modelo
from .models import Beerpub


# Register the models 
@admin.register(Beerpub)
class VinosAdmin(ModelAdmin):
    ...