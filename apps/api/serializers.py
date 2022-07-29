from rest_framework import serializers
from django.contrib.auth.models import User
from apps.webapp.models import Film, FilmCharacter, FilmPlanet, SentientBeing, Planet, Vehicle, Language, SentientBeingType


class FilmSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Film
        fields = (
            'title',
            'description',
            'attributes',
            'attributes_orig',
            'date_created',
            'date_modified'
        )


class SentientBeingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SentientBeing
        fields = (
            'sentient_being_type_id',
            'home_world_id',
            'name_first',
            'name_last',
            'description',
            'attributes',
            'attributes_orig',
            'date_created',
            'date_modified'
            )


class PlanetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Planet
        fields = (
            'name',
            'description',
            'attributes',
            'attributes_orig',
            'date_created',
            'date_modified'
        )


class VehicleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Vehicle
        fields = (
            'vehicle_class_id',
            'model',
            'description',
            'attributes',
            'attributes_orig',
            'date_created',
            'date_modified'
        )


class FilmCharacterSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.ReadOnlyField(source='film.id')
    film_id = serializers.ReadOnlyField(source='film.film_id')
    sentient_being_id = serializers.ReadOnlyField(source='sentient_being.sentient_being_id')

    class Meta:
        model = FilmCharacter

        fields = {
            'film_id',
            'sentient_being_id',
        }

class FilmPlanetSerializer(serializers.HyperlinkedModelSerializer):
    film_id = serializers.ReadOnlyField(source='film.film_id')
    planet_id = serializers.ReadOnlyField(source='planet.planet_id')

    class Meta:
        model = FilmCharacter

        fields = {
            'film_id',
            'planet_id',
        }

class LanguageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Language
        fields = (
            'name',
            'description',
            'attributes',
            'attributes_orig',
            'date_created',
            'date_modified'
        )

class SentientBeingTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SentientBeingType
        fields = (
            'name',
            'language_id',
            'description',
            'attributes',
            'attributes_orig',
            'date_created',
            'date_modified'
            )