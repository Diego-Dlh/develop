from django.db import models
from .prestamo import Prestamo

class Pago(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE, related_name="pagos")
    monto_pagado = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.prestamo.saldo_pendiente -= self.monto_pagado
        if self.prestamo.saldo_pendiente <= 0:
            self.prestamo.saldo_pendiente = 0
            self.prestamo.estado = 2  # estado "Pagado"
        self.prestamo.save()

        super().save(*args, **kwargs)
