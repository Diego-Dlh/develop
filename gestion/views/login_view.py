import jwt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from gestion.models.usuario import Usuario
from rest_framework.permissions import AllowAny
from datetime import datetime, timedelta

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        identificacion = request.data.get("identificacion")
        contraseña = request.data.get("contraseña")

        try:
            usuario = Usuario.objects.get(identificacion=identificacion)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        if usuario.contraseña != contraseña:
            return Response({"error": "Contraseña incorrecta"}, status=status.HTTP_401_UNAUTHORIZED)

        payload = {
            "usuario_id": usuario.id,
            "rol": usuario.rol,
            "nombre": usuario.nombre,
            "exp": datetime.utcnow() + timedelta(hours=2),
            "iat": datetime.utcnow(),
        }

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

        return Response({
            "access": token,
            "usuario_id": usuario.id,
            "rol": usuario.rol,
            "nombre": usuario.nombre,
        })
