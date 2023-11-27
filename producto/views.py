from django.shortcuts import render
from rest_framework import generics, status
from .models import Producto, Categoria, Genero
from .serializers import ProductoSerializer, CategoriaSerializer, GeneroSerializer
from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def perform_create(self, serializer):
        # Accede al archivo de la solicitud
        imagen = self.request.data.get('imagen', None)

        # Puedes realizar alguna lógica aquí, como validar el archivo, cambiar el nombre, etc.
        # En este ejemplo, se utiliza el nombre original del archivo.

        # Si hay una imagen en la solicitud, asigna la imagen al campo 'imagen' del modelo.
        if imagen:
            serializer.validated_data['imagen'] = imagen

        serializer.save()


class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Agregar el nombre de la categoría y del género al resultado
        data = serializer.data
        data['categoria_nombre'] = instance.categoria.nombre if instance.categoria else None
        data['genero_nombre'] = instance.genero.nombre if instance.genero else None

        return Response(data)

class ListarCategoria(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ListarGenero(generics.ListCreateAPIView):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class TresPrimerosProductosView(View):
    
    def get(self, request, *args, **kwargs):
        # Obtener los tres primeros productos
        tres_primeros_productos = Producto.objects.all()[:3]
        
        # Serializar los productos
        serializer = ProductoSerializer(tres_primeros_productos, many=True)
        
        # Devolver la respuesta JSON
        return JsonResponse(serializer.data, safe=False)

class ProductosPorGeneroView(APIView):
    def get(self, request, genero_id, *args, **kwargs):
        productos = Producto.objects.filter(genero__id=genero_id)
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)