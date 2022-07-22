from django.db import models
from django.urls import reverse


class Film(models.Model):
    """Representation of a film (e.g., The Empire Strikes Back)."""

    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True, null=True)
    attributes = models.JSONField(blank=True, null=True)
    attributes_orig = models.JSONField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'film'
        ordering = ['title']
        verbose_name = 'Film'
        verbose_name_plural = 'Films'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film_detail', kwargs={'pk': self.pk})

    # characters = models.ManyToManyField('Person', through='FilmCharacter', related_name='film_sentient_being', blank=True)
    # planets = models.ManyToManyField('Planet', through='FilmPlanet', related_name='film_planet', blank=True)
    # starships = models.ManyToManyField('Starship', related_name="film_starships", blank=True)
    # vehicles = models.ManyToManyField('Vehicle', related_name="film_vehicles", blank=True)
    # species = models.ManyToManyField('Species', related_name="film_species", blank=True)

    # def film_characters(self):
    #     return "\n".join([character.name for character in self.characters.all()])

    # def film_planets(self):
    #     return "\n".join([planet.name for planet in self.planets])

    # def get_starships(self):
    #     return "\n".join([starship.url for starship in self.starships.all()])

    # def get_vehicles(self):
    #     return "\n".join([vehicle.url for vehicle in self.vehicles.all()])

    # def get_species(self):
    #     return "\n".join([species.url for species in self.species.all()])


class FilmCharacter(models.Model):
    """PK added to satisfy Django requirement. Row(s) will be deleted if the corresponding parent
    record(s) is/are deleted. This mirrors CONSTRAINT behavior in the DB back-end.
	"""

    film_character_id = models.AutoField(primary_key=True)
    film = models.ForeignKey('Film', on_delete=models.CASCADE, blank=True, null=True)
    sentient_being = models.ForeignKey('SentientBeing', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film_character'
        ordering = ['film', 'sentient_being']
        verbose_name = 'Film Character'
        verbose_name_plural = 'Film Characters'
        unique_together = (('film', 'sentient_being'),)


class FilmPlanet(models.Model):
    """
	PK added to satisfy Django requirement. Row(s) will be deleted
    if the corresponding parent record(s) is/are deleted.
    This mirrors CONSTRAINT behavior in the DB back-end.
	"""

    film_planet_id = models.AutoField(primary_key=True)
    film = models.ForeignKey('Film', on_delete=models.CASCADE, blank=True, null=True)
    planet = models.ForeignKey('Planet', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film_planet'
        ordering = ['film', 'planet']
        verbose_name = 'Film Planet'
        verbose_name_plural = 'Film Planets'
        unique_together = (('film', 'planet'),)


class FilmVehicle(models.Model):
    """PK added to satisfy Django requirement. Row(s) will be deleted if the corresponding parent
    record(s) is/are deleted. This mirrors CONSTRAINT behavior in the DB back-end.
	"""

    film_vehicle_id = models.AutoField(primary_key=True)
    film = models.ForeignKey('Film', on_delete=models.CASCADE, blank=True, null=True)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film_vehicle'
        ordering = ['film', 'vehicle']
        verbose_name = 'Film Vehicle'
        verbose_name_plural = 'Film Vehicless'
        unique_together = (('film', 'vehicle'),)


class Language(models.Model):
    """Representation of a language (e.g., Galatic Basic)."""

    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(blank=True, null=True)
    attributes = models.JSONField(blank=True, null=True)
    attributes_orig = models.JSONField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'language'
        ordering = ['name']
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('language_detail', kwargs={'pk': self.pk})


class Planet(models.Model):
    """Representation of a planet (e.g., Hoth)."""

    planet_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(blank=True, null=True)
    attributes = models.JSONField(blank=True, null=True)
    attributes_orig = models.JSONField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'planet'
        ordering = ['name']
        verbose_name = 'Planet'
        verbose_name_plural = 'Planets'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('planet_detail', kwargs={'pk': self.pk})


class SentientBeing(models.Model):
    """Representation of a sentient being (e.g., Luke Skywalker, R2D2)."""

    sentient_being_id = models.AutoField(primary_key=True)
    sentient_being_type = models.ForeignKey('SentientBeingType', related_name="sentient_being_sentient_being_type", on_delete=models.PROTECT, blank=True, null=True)
    home_world = models.ForeignKey('Planet', related_name="sentient_being_home_world", on_delete=models.PROTECT, blank=True, null=True)
    name_first = models.CharField(max_length=100, null=False)
    name_last = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    attributes = models.JSONField(blank=True, null=True)
    attributes_orig = models.JSONField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'SentientBeing'
        ordering = ['name_last', 'name_first']
        verbose_name = 'Sentient Being'
        verbose_name_plural = 'Sentient Beings'

    def __str___(self):
        if self.name_last:
            return f"{self.name_first} {self.name_last}"
        else:
            return self.name_first

    def get_absolute_url(self):
        return reverse('sentient_being_detail', kwargs={'pk': self.pk})


class SentientBeingType(models.Model):
    """Representation of a sentient being type (e.g., Wookiee)."""

    sentient_being_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    language = models.ForeignKey('Language', related_name="sentient_being_language", on_delete=models.PROTECT, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    attributes = models.JSONField(blank=True, null=True)
    attributes_orig = models.JSONField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'sentient_being_type'
        ordering = ['name']
        verbose_name = 'Sentient Being Type'
        verbose_name_plural = 'Sentient Being Types'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sentient_being_type_detail', kwargs={'pk': self.pk})


class Vehicle(models.Model):
    """Representation of a vehicle (e.g., Snowspeeder, X-Wing starfighter)."""

    vehicle_id = models.AutoField(primary_key=True)
    vehicle_type = models.ForeignKey('VehicleType', related_name="vehicle_vehicle_type", on_delete=models.PROTECT, blank=True, null=True)
    vehicle_class = models.ForeignKey('VehicleClass', related_name="vehicle_vehicle_class", on_delete=models.PROTECT, blank=True, null=True)
    model = models.CharField(max_length=50, null=False)
    description = models.TextField(blank=True, null=True)
    attributes = models.JSONField(blank=True, null=True)
    attributes_orig = models.JSONField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'vehicle'
        ordering = ['model']
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

    def __str___(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vehicle_detail', kwargs={'pk': self.pk})


class VehicleClass(models.Model):
    """Representation of a vehicle class (e.g., Starfighter)."""

    vehicle_class_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(blank=True, null=True)
    attributes = models.JSONField(blank=True, null=True)
    attributes_orig = models.JSONField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'vehicle_class'
        ordering = ['name']
        verbose_name = 'Vehicle Class'
        verbose_name_plural = 'Vehicle Classes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vehicle_class_detail', kwargs={'pk': self.pk})


class VehicleType(models.Model):
    """Representation of a vehicle type (e.g., Aquatic)."""

    vehicle_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(blank=True, null=True)
    attributes = models.JSONField(blank=True, null=True)
    attributes_orig = models.JSONField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'vehicle_type'
        ordering = ['name']
        verbose_name = 'Vehicle Type'
        verbose_name_plural = 'Vehicle Types'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vehicle_type_detail', kwargs={'pk': self.pk})
