from api.models.Weapon import Weapon
from rest_framework import serializers

class WeaponSerializer(serializers.Serializer):
    class Meta:
        model = Weapon
        fields = '__all__'