from rest_framework import generics
from .models import Balance, HistorialBalance
from .serializers import BalanceSerializer, HistorialBalanceSerializer

class BalanceListCreateView(generics.ListCreateAPIView):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BalanceSerializer
        elif self.request.method == 'POST':
            return BalanceSerializer  # Otra clase de serializador para la creación si es necesario

    def perform_create(self, serializer):
        # Personaliza la creación del objeto Balance aquí si es necesario
        serializer.save()

class HistorialBalanceListCreateView(generics.ListCreateAPIView):
    serializer_class = HistorialBalanceSerializer

    def get_queryset(self):
        # Obtén el historial para una cuenta específica, ajusta esto según tu lógica
        cuenta_id = self.kwargs['pk']
        return HistorialBalance.objects.filter(balance_id=cuenta_id)

    def perform_create(self, serializer):
        # Personaliza la creación del objeto HistorialBalance aquí si es necesario
        serializer.save()