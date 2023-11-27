from django.urls import path
from .views import BalanceListCreateView, HistorialBalanceListCreateView

urlpatterns = [
    path('balance/', BalanceListCreateView.as_view(), name='balance-list-create'),
    path('balances/<int:pk>/historial/', HistorialBalanceListCreateView.as_view(), name='historialbalance-list-create'),
    
    
]