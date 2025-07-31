from django.db import models
from .usuario import Usuario
from .deudor import Deudor

class Prestamo(models.Model):
    ESTADO_CHOICES = (
        (1, 'Pendiente'),
        (2, 'Pagado'),
        (3, 'Vencido'),
    )
    interes_choices = (
        (10, '10%'),
        (15, '15%'),
        (20, '20%'),
    )
    meses_choices = (
        (1, '1 mes'),
        (2, '2 meses'),
    )

    deudor = models.ForeignKey(Deudor, on_delete=models.CASCADE)
    cobrador = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 2})
    monto = models.IntegerField()
    saldo_pendiente = models.IntegerField(blank=True)

    interes = models.IntegerField(choices=interes_choices, default=0)
    meses = models.IntegerField(choices=meses_choices, default=1)
    fecha = models.DateField(auto_now_add=True)
    estado = models.IntegerField(choices=ESTADO_CHOICES, default=1)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.saldo_pendiente = int(self.monto + (self.monto * float(self.interes) / 100))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Préstamo #{self.id} - {self.deudor}"
