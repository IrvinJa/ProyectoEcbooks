from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Balance(models.Model):
    titular = models.OneToOneField(User, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        balance="{} {}".format(self.titular, self.saldo)
        return balance
    
    def realizar_transaccion(self, accion, descripcion, monto):
        if accion == 'Depósito':
            self.saldo += monto
        elif accion == 'Retiro' and monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Operación no válida. Saldo insuficiente para el retiro.")
            return

        # Guardar el saldo actualizado
        self.save()

        # Registrar la transacción en el historial
        HistorialBalance.objects.create(
            balance=self,
            accion=accion,
            descripcion=descripcion,
            monto=monto
        )
    
    class Meta:
        verbose_name = 'Balance'
        verbose_name_plural = 'Balances'
        db_table = 'balance'
        ordering = ['pk']

class HistorialBalance(models.Model):
    ACCION_DEPOSITO = 'Depósito'
    ACCION_RETIRO = 'Retiro'
    
    ACCIONES_CHOICES = [
        (ACCION_DEPOSITO, 'Depósito'),
        (ACCION_RETIRO, 'Retiro'),
    ]

    balance = models.ForeignKey(Balance, on_delete=models.CASCADE)
    accion = models.CharField(max_length=10, choices=ACCIONES_CHOICES)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "{} - {} - {}".format(self.accion, self.descripcion, self.fecha)

    class Meta:
        verbose_name = 'Historial de Balance'
        verbose_name_plural = 'Historiales de Balance'
        db_table = 'historial_balance'
        ordering = ['-fecha']