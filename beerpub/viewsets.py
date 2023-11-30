# Elementos necesarios para que el API REST funcione 
from rest_framework.viewsets import ModelViewSet 
#from rest_framework import permissions


#from django.http import Http404
#from rest_framework import status
#from rest_framework.response import Response



# Clase 'BeerpubSerializer' 
from .serializers import BeerpubSerializer
#from beerpub.serializers import BeerpubSerializer

# Modelo 'Beerpub' 
#from beerpub.models import Beerpub
from .models import Beerpub


# # Importo la clase 'IsAuthenticated' de Django Rest Framework 
# from rest_framework.permissions import IsAuthenticated

class BeerpubViewSet(ModelViewSet):
    
    #permission_classes = [IsAuthenticated] # Llamo a la clase 'IsAuthenticated' de Django Rest Framework 
    #queryset = Beerpub.objects.all().order_by('id')
    queryset = Beerpub.objects.all()
    serializer_class = BeerpubSerializer
    #permission_classes= [permissions.IsAdminUser]

    