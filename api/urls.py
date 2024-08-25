from rest_framework.routers import SimpleRouter
from api import views
from django.urls import path, include
from django.urls import re_path as url
from rest_framework_swagger.views import get_swagger_view
from api.views.AuthViews import UserRegistrationView
from api.views.CustomObtainJSONWebToken import CustomTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

schema_view = get_swagger_view(title='Meu Operador API')

router = SimpleRouter()

router.register(r'weapon', views.WeaponViewSet, 'weapon')
router.register(r'profile', views.ProfileViewSet, 'profile')
router.register(r'team', views.TeamViewSet, 'team')
router.register(r'confirm', views.ConfirmView, basename='confirm')

urlpatterns = [
    path('api-token-verify/', TokenVerifyView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
    path('api-token-auth/', CustomTokenObtainPairView.as_view(), name='api_token_auth'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('', include(router.urls)),
    url(r'^$', schema_view)
]