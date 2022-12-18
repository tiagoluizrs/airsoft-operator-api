from api.models.Profile import Team
from rest_framework import serializers

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'