# <----------------Importar Bibliotecas----------------->
from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

# <----------------Importar Componentes----------------->
from .models import InstituicaoModel

# <-----------------Classe para Serializar API------------------>
class InstituicaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = InstituicaoModel
        fields = ['__all__']
