from rest_framework import serializers
from gestion.models.prestamo import Prestamo

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'
        read_only_fields = ['saldo_pendiente']  # No lo pide el cliente
