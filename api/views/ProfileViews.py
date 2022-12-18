from rest_framework.decorators import action
from rest_framework.response import Response
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

    @action(detail=False, methods=['get'])
    def get_by_username(self, request):
        user = Profile.objects.filter(user__username=request.GET.get('username', None)).first()
        if user:
            serializer = ProfileSerializer(user)
            return Response(serializer.data)
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND)