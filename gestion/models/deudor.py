from django.db import models
from gestion.models.usuario import Usuario

class Deudor(models.Model):
    TIPO_CHOICES = (
        (1, 'Normal'),
        (2, 'Especial'),
    )

    id = models.IntegerField(primary_key=True)  # <- ID manual
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    tipo = models.IntegerField(choices=TIPO_CHOICES, default=1)
    cobrador = models.ForeignKey(Usuario, related_name="deudores")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
