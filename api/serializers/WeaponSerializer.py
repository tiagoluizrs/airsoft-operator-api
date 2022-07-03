from api.models.Weapon import Weapon
from rest_framework import serializers

class WeaponSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    brand = serializers.CharField(source='brand.name')
    
    class Meta:
        model = Weapon
        fields = '__all__'