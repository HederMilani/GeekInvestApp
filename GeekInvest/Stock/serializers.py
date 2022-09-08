# <---------------Importar Bibliotecas--------------->
from dataclasses import fields
from rest_framework import serializers

# <-----------------Importar Componentes---------------->
from .models import stock_models

# <-------------------Classe para serializar API----------------->
class stock_serializers(serializers.ModelSerializer):
    class Meta:
        model = stock_models
        fields = '__all__'
