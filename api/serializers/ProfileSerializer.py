from api.models.Profile import Profile
from api.serializers.UserSerializer import UserSerializer
from api.serializers.TeamSerializer import TeamSerializer
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    full_name = serializers.CharField(source='user.get_full_name')
    team = serializers.CharField(source='team.name')
    patent = serializers.CharField(source='patent.name')
    team = TeamSerializer(many=False)
    user = UserSerializer(many=False)

    class Meta:
        model = Profile
        fields = '__all__'