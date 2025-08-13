# prestamo_serializer.py
from rest_framework import serializers
from gestion.models.prestamo import Prestamo

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'
        # IMPORTANTe: el backend calcula saldo_pendiente en save()
        # y asigna cobrador en perform_create -> ambos read-only
        read_only_fields = ['saldo_pendiente', 'cobrador']
