from django.contrib.auth.models import User
from rest_framework import serializers


class UserUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_null=True)
    first_name = serializers.CharField(required=False, allow_null=True)
    last_name = serializers.CharField(required=False, allow_null=True)
    email = serializers.EmailField(required=False, allow_null=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)