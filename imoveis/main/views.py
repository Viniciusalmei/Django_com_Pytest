from django.shortcuts import render
from .models import * 
from .serializers import * 
from rest_framework import viewsets

# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ImovelViewSet(viewsets.ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

class FaturaViewSet(viewsets.ModelViewSet):
    queryset = Fatura.objects.all()
    serializer_class = FaturaSerializer