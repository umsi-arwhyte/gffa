
from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination

from django.contrib.auth.models import User
from apps.webapp.models import Film, Planet, SentientBeing, Vehicle, Language
from .serializers import FilmSerializer, PlanetSerializer, SentientBeingSerializer, VehicleSerializer, LanguageSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Film.objects.all()
        title = self.request.query_params.get('title', None)
        episode_id = self.request.query_params.get('episode_id', None)
        if title:
            queryset = queryset.filter(title__contains=title)
        if episode_id:
            queryset = queryset.filter(episode_id=episode_id)

        return queryset.order_by('film_id')


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Planet.objects.all()
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name__contains=name)

        return queryset.order_by('planet_id')


class SentientBeingViewSet(viewsets.ModelViewSet):
    queryset = SentientBeing.objects.all()
    serializer_class = SentientBeingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = SentientBeing.objects.all()
        home_world = self.request.query_params.get('home_world', None)
        name_first = self.request.query_params.get('name_first',None)
        if home_world:
            queryset = queryset.filter(home_world__name_first__iexact=home_world)
        if name_first:
            queryset = queryset.filter(name_first__contains=name_first)

        return queryset.order_by('sentient_being_id')


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Vehicle.objects.all()
        name = self.request.query_params.get('name', None)
        manufacturer = self.request.query_params.get('manufacturer', None)
        if name:
            queryset = queryset.filter(name__contains=name)
        if manufacturer:
            queryset = queryset.filter(manufacturer__contains=manufacturer)

        return queryset.order_by('vehicle_id')

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Language.objects.all()
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name__contains=name)

        return queryset.order_by('language_id')