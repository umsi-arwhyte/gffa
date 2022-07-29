from rest_framework import serializers
from django.contrib.auth.models import User
from apps.webapp.models import Film, FilmCharacter, FilmPlanet, FilmVehicle, SentientBeing, Planet, Vehicle, Language, SentientBeingType, VehicleClass, VehicleType


class FilmSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Film
        fields = (
            'film_id',
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
            'sentient_being_id',
            'sentient_being_type',
            'home_world',
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
            'planet_id',
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
            'vehicle_id',
            'vehicle_class',
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
            'language_id',
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
            'sentient_being_type_id',
            'name',
            'language_id',
            'description',
            'attributes',
            'attributes_orig',
            'date_created',
            'date_modified'
            )

class FilmVehicleSerializer(serializers.HyperlinkedModelSerializer):
    film_id = serializers.ReadOnlyField(source='film.film_id')
    vehicle_id = serializers.ReadOnlyField(source='vehicle.vehicle_id')

    class Meta:
        model = FilmVehicle
        fields = {
            'film_id',
            'vehicle_id',
        }

class VehicleClassSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = VehicleClass
        fields = (
            'vehicle_class_id',
            'vehicle_type'
            'name',
            'description',
            'attributes',
            'attributes_orig',
            'date_created',
            'date_modified'
        )

class VehicleTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = VehicleType
        fields = (
            'vehicle_type_id'
            'name',
            'description',
            'attributes',
            'attributes_orig',
            'date_created',
            'date_modified'
        )
