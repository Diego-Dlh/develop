from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gestion.views import UsuarioViewSet, DeudorViewSet, PrestamoViewSet, PagoViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from gestion.views.login_view import LoginView
from gestion.views.auth_views import CustomTokenObtainPairView

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'deudores', DeudorViewSet)
router.register(r'prestamos', PrestamoViewSet)
router.register(r'pagos', PagoViewSet)

from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "usuarios": "/api/usuarios/",
        "deudores": "/api/deudores/",
        "prestamos": "/api/prestamos/",
        "pagos": "/api/pagos/",
        "login": "/api/login/",
        "token_obtain_pair": "/api/token/",
        "token_refresh": "/api/token/refresh/"
    })
# ...existing code...

urlpatterns = [
    path('', api_root),
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    
]

