from rest_framework import serializers
from django.utils.timezone import localtime
from  gestion.models.pago import Pago

class PagoSerializer(serializers.ModelSerializer):
    fecha_local = serializers.SerializerMethodField()

    class Meta:
        model = Pago
        fields = '__all__'

    def get_fecha_local(self, obj):
        return localtime(obj.fecha).strftime('%Y-%m-%d %H:%M:%S')
