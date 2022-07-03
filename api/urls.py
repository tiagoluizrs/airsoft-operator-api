from rest_framework.routers import SimpleRouter
from api import views
from django.urls import path, include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Meu Operador API')

router = SimpleRouter()

router.register(r'weapon', views.WeaponViewSet, 'weapon')
router.register(r'profile', views.ProfileViewSet, 'profile')

urlpatterns = [
    path('', include(router.urls)),
    url(r'^$', schema_view)
]