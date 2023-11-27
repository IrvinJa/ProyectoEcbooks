from rest_framework import serializers
from .models import Balance, HistorialBalance

class HistorialBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialBalance
        fields = '__all__'

class BalanceSerializer(serializers.ModelSerializer):
    historial = HistorialBalanceSerializer(many=True, read_only=True)

    class Meta:
        model = Balance
        fields = '__all__'