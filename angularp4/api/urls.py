from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'autos', views.AutoViewSet)
router.register(r'perros', views.PerroViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth', include('rest_framework.urls', namespace='rest_framework')),
]