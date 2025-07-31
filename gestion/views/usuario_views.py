from rest_framework import viewsets
from gestion.models.usuario import Usuario
from gestion.serializers.usuario_serializer import UsuarioSerializer
from rest_framework.permissions import IsAuthenticated as is_authenticated

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [is_authenticated] 