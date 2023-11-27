from django.urls import path
from .views import ProductoListCreateView, ProductoDetailView, ListarCategoria, ListarGenero, TresPrimerosProductosView,  ProductosPorGeneroView

urlpatterns = [
    path('productos/', ProductoListCreateView.as_view(), name='producto-list-create'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),
    path('categoria/',ListarCategoria.as_view(),name='categoria'),
    path('generos/',ListarGenero.as_view(),name='genero'),
    path('toptres/',TresPrimerosProductosView.as_view(),name='joyitas'),
    path('productos/por-genero/<int:genero_id>/', ProductosPorGeneroView.as_view(), name='productos-por-genero'),
]