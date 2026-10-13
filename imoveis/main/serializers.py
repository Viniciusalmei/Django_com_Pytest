from rest_framework import serializers 
from .models import * 


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = "__all__"

class FaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fatura
        fields = "__all__"