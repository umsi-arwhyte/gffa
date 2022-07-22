from django.contrib import admin
from . models import (
    Film, FilmCharacter, FilmPlanet, FilmVehicle,
    Planet,
    SentientBeing, SentientBeingType,
    Vehicle, VehicleClass, VehicleType
    )

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    """Film administration."""

    fields = (
        'title',
        'description',
        'attributes',
        'attributes_orig',
        'date_created',
        'date_modified',
    )
    list_display = (
        'title',
        'description',
        'attributes',
        'attributes_orig',
        'date_created',
        'date_modified'
    )
    list_filter = ('title',)
    filter_horizontal = ()
    ordering = ('title',)


@admin.register(FilmCharacter)
class FilmCharacterAdmin(admin.ModelAdmin):
    """FilmCharacter administration."""

    fields = ('film', 'sentient_being')
    list_display = ('film', 'sentient_being')
    list_filter = ('film',)
    ordering = ('film', 'sentient_being')


@admin.register(FilmPlanet)
class FilmPlanetAdmin(admin.ModelAdmin):
    """FilmPlanet administration."""

    fields = ('film', 'planet')
    list_display = ('film', 'planet')
    list_filter = ('film',)
    ordering = ('film', 'planet')


@admin.register(FilmVehicle)
class FilmVehicleAdmin(admin.ModelAdmin):
    """FilmVehicle administration."""

    fields = ('film', 'vehicle')
    list_display = ('film', 'vehicle')
    list_filter = ('film',)
    ordering = ('film', 'vehicle')


@admin.register(SentientBeing)
class SentientBeingAdmin(admin.ModelAdmin):
    """SentientBeing administration."""

    fields =  (
        'sentient_being_type',
        'name_last',
        'name_first',
        'description',
        'attributes',
        'attributes_orig',
        'date_created',
        'date_modified',
    )
    list_display =  (
        'sentient_being_type',
        'name_last',
        'name_first',
        'description',
        'attributes',
        'attributes_orig',
        'date_created',
        'date_modified',
    )
    list_filter = ('name_last', 'name_first')
    ordering = ('name_last', 'name_first')


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    """Planet administration."""

    fields =  (
        'name',
        'description',
        'attributes',
        'attributes_orig',
        'date_created',
        'date_modified',
    )
    list_display =  (
        'name',
        'description',
        'attributes',
        'attributes_orig',
        'date_created',
        'date_modified',
    )
    ordering = ('name',)
    list_filter = ('name',)

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    """Vehicle administration."""

    fields =  (
        'vehicle_type',
        'vehicle_class',
        'model',
        'description',
        'attributes',
        'attributes_orig',
        'date_created',
        'date_modified',
    )
    list_display =  (
        'vehicle_type',
        'vehicle_class',
        'model',
        'description',
        'attributes',
        'attributes_orig',
        'date_created',
        'date_modified',
    )
    list_filter = ('name',)
    ordering = ('name',)
