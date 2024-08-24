from rest_framework import viewsets
from api.serializers.TeamSerializer import TeamSerializer, Team
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from api.utils.CustomPagination import CustomPagination

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    ordering_fields = '__all__'
    search_fields = ('name',)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ('id', 'name',)
    ordering_fields = ('name',)
    ordering = ['name']
    serializer_class = TeamSerializer
    permission_classes = (IsAuthenticated,)

    pagination_class = CustomPagination