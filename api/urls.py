from rest_framework.routers import SimpleRouter
from api import views
from django.urls import path, include

router = SimpleRouter()

router.register(r'weapon', views.WeaponViewSet, 'weapon')

urlpatterns = [
    path('', include(router.urls))
]