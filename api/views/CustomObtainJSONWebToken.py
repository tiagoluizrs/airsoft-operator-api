from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from api.serializers.ProfileSerializer import ProfileSerializer

from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Adicione quaisquer informações adicionais ao token se necessário
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password')
        )

        if user:
            if not user.is_active:
                return Response({'error': 'Este usuário está inativo.'}, status=status.HTTP_401_UNAUTHORIZED)
            if response.status_code == status.HTTP_200_OK:
                response.data.update({
                    'profile': ProfileSerializer(user.profile).data,
                })
        return response
