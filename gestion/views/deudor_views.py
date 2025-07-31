from rest_framework import viewsets
from gestion.models.deudor import Deudor
from gestion.serializers.deudor_serializer import DeudorSerializer

class DeudorViewSet(viewsets.ModelViewSet):
    queryset = Deudor.objects.all()  # 👈 necesario para registrar en router
    serializer_class = DeudorSerializer

    def get_queryset(self):
        user = self.request.user
        if user.rol == 1:
            return Deudor.objects.all()
        elif user.rol == 2:
            return Deudor.objects.filter(cobrador=user)
        return Deudor.objects.none()

    def perform_create(self, serializer):
        serializer.save(cobrador=self.request.user)
