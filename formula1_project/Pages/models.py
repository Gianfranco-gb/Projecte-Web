from django.db import models
import formula1_project
# Create your models here.

class Escuderia(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    colors = models.CharField(max_length=100)
    principalDriver = models.CharField(max_length=200)
    secondaryDriver = models.CharField(max_length=200)
    num_championships = models.IntegerField(max_length=100)

class Piloto(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(max_length=100)
    nacionality = models.CharField(max_length=100)
    escuderia = models.CharField(max_length=100)
    height = models.IntegerField(max_length=100)
    weight = models.IntegerField(max_length=100)

class EstadisticaDriver(models.Model):
    nameDriver = models.CharField(max_length=200)
    num_of_championships = models.IntegerField(max_length=100)
    age_validity = models.IntegerField(max_length=100)
    num_dif_teams = models.IntegerField(max_length=100)
    name_dif_teams = models.CharField(max_length=100)

class EstadisticaScuderia(models.Model):
    nameScuderia = models.CharField(max_length=100)
    age_of_birth = models.IntegerField(max_length=100)
    num_of_championships = models.IntegerField(max_length=100)

class Circuito(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    circuit_length = models.IntegerField(max_length=100)
    laps_in_race = models.IntegerField(max_length=100)
    first_gp = models.IntegerField(max_length=100)
    race_distance = models.IntegerField(max_length=100)
    lap_record = models.CharField(max_length=100)

class Temporada(models.Model):
    year = models.IntegerField(max_length=100)
    num_gp = models.IntegerField(max_length=100)
    num_scuderias = models.IntegerField(max_length=100)
    world_champion = models.CharField(max_length=100)
