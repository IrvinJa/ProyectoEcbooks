from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from rest_framework import routers
from .views import  ListarUsuarios, CrearUsuario, VerUsuario




urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/listarusers/', ListarUsuarios.as_view(), name='ver_usuario'),
    path('api/verusuario/<int:pk>/', VerUsuario.as_view(), name='ver_un_usuario'),
    path('api/registro/', CrearUsuario.as_view(), name='registrar_usuario'),
    
]