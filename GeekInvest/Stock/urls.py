# <--------------Importar Bibliotecas-------------->
from rest_framework.routers import DefaultRouter

# <--------------Importar Componentes----------------->
from .views import stock_viewset

app_name = 'stock'

router = DefaultRouter(trailing_slash=False)
router.register(r'stock', stock_viewset)

urlpatterns = router.urls
