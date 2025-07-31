from rest_framework import serializers
from gestion.models.deudor import Deudor

class DeudorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deudor
        fields = '__all__'
        extra_kwargs = {
            'cobrador': {'required': False, 'write_only': True}
        }
