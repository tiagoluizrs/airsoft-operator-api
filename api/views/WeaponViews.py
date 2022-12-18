from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from api.serializers.WeaponSerializer import WeaponSerializer, Weapon
from rest_framework.permissions import IsAuthenticated

class WeaponViewSet(viewsets.ModelViewSet):    
    queryset = Weapon.objects.all()
    ordering_fields = '__all__'
    filter_fields = '__all__'
    search_fields = ('name',)
    serializer_class = WeaponSerializer
    permission_classes = (IsAuthenticated,)