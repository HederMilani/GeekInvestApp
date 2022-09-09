# <-------------Importar Bibliotecas------------>
from rest_framework import serializers
from django.contrib.auth import get_user_model

# <--------------Serializer para dados da API----------------->
class user_serializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username']
