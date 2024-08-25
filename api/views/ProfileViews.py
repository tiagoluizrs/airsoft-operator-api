from rest_framework import viewsets
from api.serializers.ProfileSerializer import ProfileSerializer, Profile
from rest_framework.permissions import IsAuthenticated

class ProfileViewSet(viewsets.ModelViewSet):    
    queryset = Profile.objects.all()
    ordering_fields = '__all__'
    filter_fields = '__all__'
    search_fields = ('name',)
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)