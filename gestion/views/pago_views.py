from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from gestion.models.pago import Pago
from gestion.serializers.pago_serializer import PagoSerializer
from gestion.models.prestamo import Prestamo
from datetime import datetime

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()  # <-- ESTO es obligatorio para DRF router
    serializer_class = PagoSerializer

    def get_queryset(self):
        user = self.request.user
        pagos = Pago.objects.all()

        if user.rol != 1:
            pagos = pagos.filter(prestamo__cobrador=user)

        mes = self.request.query_params.get('mes')
        if mes:
            try:
                mes = int(mes)
                pagos = pagos.filter(fecha__month=mes)
            except ValueError:
                pass

        return pagos

    def perform_create(self, serializer):
        user = self.request.user
        prestamo = serializer.validated_data.get("prestamo")

        if user.rol != 1 and prestamo.cobrador != user:
            raise PermissionDenied("No tienes permiso para registrar pagos en este préstamo.")

        serializer.save()
