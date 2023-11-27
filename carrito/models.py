from django.db import models
from django.contrib.auth.models import User
from producto.models import Producto

class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='ElementoCarrito')

    def calcular_total(self):
        return sum(item.subtotal() for item in self.elementoscarrito_set.all())

    def __str__(self):
        total = self.calcular_total()
        return f'Carrito de {self.usuario.username}. Total: {total}'

class ElementoCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='elementoscarrito_set')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.cantidad * self.producto.precio
    
    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre} en el carrito de {self.carrito.usuario.username}'
