from rest_framework.routers import SimpleRouter
from api import views
from django.urls import path, include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token

schema_view = get_swagger_view(title='Meu Operador API')

router = SimpleRouter()

router.register(r'weapon', views.WeaponViewSet, 'weapon')
router.register(r'profile', views.ProfileViewSet, 'profile')
router.register(r'team', views.TeamViewSet, 'team')

urlpatterns = [
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-auth/', obtain_jwt_token),
    path('', include(router.urls)),
    url(r'^$', schema_view)
]