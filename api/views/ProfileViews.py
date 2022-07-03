from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from api.serializers.ProfileSerializer import ProfileSerializer, Profile

class ProfileViewSet(viewsets.ModelViewSet):    
    queryset = Profile.objects.all()
    ordering_fields = '__all__'
    filter_fields = '__all__'
    search_fields = ('name',)
    serializer_class = ProfileSerializer