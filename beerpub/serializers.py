from rest_framework.serializers import ModelSerializer 
#from beerpub.models import Beerpub
from .models import Beerpub


class BeerpubSerializer(ModelSerializer):
    class Meta:
        model = Beerpub
        fields = "__all__"
        #fields = ['id', 'nombre', 'contacto', 'experiencia', 'img', 'created_at', 'updated_at']
        #extra_kwargs = {'id': {'required': False}}