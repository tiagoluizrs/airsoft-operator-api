from api.models.Profile import Profile
from api.serializers.UserSerializer import UserUpdateSerializer
from api.models.Profile import Team, Patent
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    user = UserUpdateSerializer()  # Utiliza o serializer para atualizar os campos do usuário
    team_name = serializers.CharField(source='team.name', read_only=True)
    patent_name = serializers.CharField(source='patent.name', read_only=True)
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), required=False)
    patent = serializers.PrimaryKeyRelatedField(queryset=Patent.objects.all(), required=False)

    class Meta:
        model = Profile
        fields = '__all__'