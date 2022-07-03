from api.serializers.WeaponSerializer import WeaponSerializer
from rest_framework import viewsets
from api.models.Weapon import Weapon

class WeaponViewSet(viewsets.ModelViewSet):    
    queryset = Weapon.objects.all()
    ordering_fields = '__all__'
    filter_fields = '__all__'
    search_fields = ('name',)
    serializer_class = WeaponSerializer