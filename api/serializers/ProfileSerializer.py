from api.models.Profile import Profile
from api.serializers.UserSerializer import UserUpdateSerializer
from api.models.Profile import Team, Patent
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

class ProfileSerializer(WritableNestedModelSerializer):
    user = UserUpdateSerializer(required=False)
    team_name = serializers.CharField(source='team.name', read_only=True)
    patent_name = serializers.CharField(source='patent.name', read_only=True)
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), required=False, allow_null=True)
    patent = serializers.PrimaryKeyRelatedField(queryset=Patent.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Profile
        fields = '__all__'