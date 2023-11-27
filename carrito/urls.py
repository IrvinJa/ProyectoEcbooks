from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarritoViewSet, ElementoCarritoViewSet

router = DefaultRouter()
router.register(r'carritos', CarritoViewSet, basename='carrito')
router.register(r'elementos-carrito', ElementoCarritoViewSet, basename='elemento-carrito')

urlpatterns = [
    path('', include(router.urls)),
]