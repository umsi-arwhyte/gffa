from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'films', views.FilmViewSet)
router.register(r'planets', views.PlanetViewSet)
router.register(r'sentient_beings', views.SentientBeingViewSet)
router.register(r'vehicles', views.VehicleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]