from rest_framework import serializers
from .models import Carrito, ElementoCarrito
from producto.serializers import ProductoSerializer

class ElementoCarritoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()

    class Meta:
        model = ElementoCarrito
        fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):
    elementoscarrito_set = ElementoCarritoSerializer(many=True, read_only=True)

    class Meta:
        model = Carrito
        fields = '__all__'