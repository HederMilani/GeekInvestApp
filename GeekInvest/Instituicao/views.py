# <---------------Importar Bibliotecas---------------------->
from rest_framework import viewsets, permissions

# <---------------Importar Componentes--------------------->
from .models import InstituicaoModel
from .serializers import InstituicaoSerializers

# <-----------------Classe Visualização dos dados pela API----------------------->
class InstituicaoViewSet(viewsets.ModelViewSet):
    queryset = InstituicaoModel.objects.all()
    serializer_class = InstituicaoSerializers
    #permission_classes = [permissions.IsAuthenticated]
