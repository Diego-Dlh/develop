from rest_framework import viewsets
from gestion.models.prestamo import Prestamo
from gestion.serializers.prestamo_serializer import PrestamoSerializer

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.none()  # solo para que DRF lo registre sin error
    serializer_class = PrestamoSerializer

    def get_queryset(self):
        user = self.request.user
        if user.rol == 1:  # Administrador
            return Prestamo.objects.all()
        return Prestamo.objects.filter(cobrador=user)

    def perform_create(self, serializer):
        serializer.save(cobrador=self.request.user)
