from rest_framework import viewsets
from .models import Carrito, ElementoCarrito
from .serializers import CarritoSerializer, ElementoCarritoSerializer

class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

class ElementoCarritoViewSet(viewsets.ModelViewSet):
    queryset = ElementoCarrito.objects.all()
    serializer_class = ElementoCarritoSerializer