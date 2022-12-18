from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from api.serializers.TeamSerializer import TeamSerializer, Team
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class TeamViewSet(viewsets.ModelViewSet):    
    queryset = Team.objects.all()
    ordering_fields = '__all__'
    search_fields = ('^name',)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ('id', 'name',)
    ordering_fields = ('name',)
    ordering = ['name']
    serializer_class = TeamSerializer
    permission_classes = (IsAuthenticated,)