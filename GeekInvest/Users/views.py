# <------------Importar Bibliotecas--------------->
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# <----------Importar Componentes----------------->
from .seralizers import user_serializers

# <-----------------Classe visualização dados da API------------------->
class user_API_views(RetrieveAPIView):
    serializer_class = user_serializers
    permission_classes = (IsAuthenticated)

    def get_object(self):
        return self.request.user
