# <---------------Importar Bibliotecas-------------->
from rest_framework.routers import DefaultRouter

# <----------------Importar Componentes--------------->
from .views import InstituicaoViewSet

app_name = 'api'

# <------------------Definir padrões de Rotas da API----------------->
router = DefaultRouter(trailing_slash=False)
router.register(r'instituicao', InstituicaoViewSet)

urlpatterns = router.urls
