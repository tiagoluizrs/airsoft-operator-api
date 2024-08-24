from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.viewsets import ViewSet

from api.serializers.UserSerializer import UserSerializer
from django.contrib.auth import get_user_model # If used custom user model

UserModel = get_user_model()
from api.utils.code import generateCode
from api.utils.Email import Email

email = Email()

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            userEmail = serializer.data['email']
            user = UserModel.objects.filter(email=userEmail).first()
            if not user:
                user = UserModel.objects.create_user(
                    username=serializer.data['username'],
                    email=userEmail,
                    password=serializer.data['password'],
                    is_active=False
                )
                if user:
                    user.profile.code_confirm = generateCode()
                    user.profile.save()
                email.enviar_email("Código de confirmação", user.profile.code_confirm, [userEmail])
            else:
                return Response({'email': ['E-mail já existe']}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ConfirmView(ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'], url_path='code', url_name='code')
    def confirm_code(self, request):
        code = request.data['code']
        email = request.data['email']
        user = UserModel.objects.filter(profile__code_confirm=code).filter(email=email).first()
        if user:
            user.is_active = True
            user.save()
            return Response({'message': 'Usuário confirmado com sucesso'}, status=status.HTTP_200_OK)
        return Response({'message': 'Código inválido'}, status=status.HTTP_400_BAD_REQUEST)