# <----------------Importar Bibliotecas------------>
from rest_framework import viewsets, permissions

# <---------------Importar Componentes----------------->
from .models import stock_models
from .serializers import stock_serializers

# <---------------Classe para Visualizar dados pela API----------------->
class stock_viewset(viewsets.ModelViewSet):
    queryset = stock_models.objects.all()
    serializer_class = stock_serializers
    permission_classes = [permissions.IsAuthenticated]
