from rest_framework import viewsets
from api.serializers.WeaponSerializer import WeaponSerializer, Weapon
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from api.utils.CustomPagination import CustomPagination

class WeaponViewSet(viewsets.ModelViewSet):    
    queryset = Weapon.objects.all()
    ordering_fields = '__all__'
    search_fields = ('name',)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ('id', 'name',)
    ordering_fields = ('name',)
    ordering = ['name']
    serializer_class = WeaponSerializer
    permission_classes = (IsAuthenticated,)

    pagination_class = CustomPagination