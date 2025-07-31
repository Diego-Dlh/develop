from django.db import models

class Usuario(models.Model):
    ROL_CHOICES = (
        (1, 'Administrador'),
        (2, 'Cobrador'),
    )
    identificacion = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=128)
    rol = models.IntegerField(choices=ROL_CHOICES)

    def __str__(self):
        return f"{self.nombre} ({self.get_rol_display()})"
    
    @property
    def is_authenticated(self):
        return True
