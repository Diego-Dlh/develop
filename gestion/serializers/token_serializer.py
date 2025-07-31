from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data["usuario_id"] = self.user.id
        data["rol"] = self.user.rol
        data["nombre"] = self.user.nombre
        return data
