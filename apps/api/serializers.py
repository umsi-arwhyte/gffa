from rest_framework import serializers
from django.contrib.auth.models import User
from apps.webapp.models import Film, FilmCharacter, FilmPlanet, FilmVehicle, SentientBeing, Planet, Vehicle, VehicleClass, VehicleType


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
            'name',
            'birth_year',
            'eye_color',
            'gender',
            'hair_color',
            'height',
            'mass',
            'skin_color',
            'home_world',
            # 'films',
            'species',
            # 'starships',
            # 'vehicles',
            'url',
            # 'created',
            # 'edited',
            )


class PlanetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Planet
        fields = (
            'name',
            'diameter',
            'rotation_period',
            'orbital_period',
            # 'gravity',
            'population',
            'climate',
            'terrain',
            # 'surface_water',
            # 'residents',
            # 'films',
            # 'url',
            # 'created',
            # 'edited',
        )


class VehicleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Vehicle
        fields = (
            'vehicle_id',
            'vehicle_type',
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
    character_id = serializers.ReadOnlyField(source='character.person_id')

    class Meta:
        model = FilmCharacter

        fields = {
            # 'film_person_id',
            'film_id',
            'character_id',
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
    vehicle_id = serializers.ReadOnlyField(source='vehicle.vehicle_id')
    vehicle_class_id = serializers.ReadOnlyField(source='vehicle_class.vehicle_class_id')

    class Meta:
        model = VehicleClass

        fields = {
            'vehicle_id'
            'vehicle_class_id'
        }

class VehicleTypeSerializer(serializers.HyperlinkedModelSerializer):
    vehicle_id = serializers.ReadOnlyField(source='vehicle.vehicle_id')
    vehicle_type_id = serializers.ReadOnlyField(source='vehicle_type.vehicle_type_id')

    class Meta:
        model = VehicleType

        fields = {
            'vehicle_id'
            'vehicle_type_id'
        }