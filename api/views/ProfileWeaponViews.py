from rest_framework import viewsets
from rest_framework.decorators import action

from api.serializers.ProfileWeaponSerializer import ProfileWeaponSerializer
from rest_framework.permissions import IsAuthenticated
from api.models.Weapon import ProfileWeapon
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status

from api.utils.CustomPagination import CustomPagination

class ProfileWeaponViewSet(viewsets.ModelViewSet):
    queryset = ProfileWeapon.objects.all()
    search_fields = ('weapon__name',)
    filterset_fields = ('id', 'weapon__name', 'profile__id')
    ordering_fields = ('weapon__name',)
    ordering = ('weapon__name',)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    serializer_class = ProfileWeaponSerializer
    permission_classes = (IsAuthenticated,)

    pagination_class = CustomPagination

    @action(detail=False, methods=['DELETE'], url_path='delete-selected')
    def delete_selected(self, request):
        ids = request.data.get('ids', [])
        ProfileWeapon.objects.filter(id__in=ids).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)