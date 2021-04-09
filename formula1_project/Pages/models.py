from django.db import models
import formula1_project


# Create your models here.

class Escuderia(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    colors = models.CharField(max_length=100)
    principalDriver = models.CharField(max_length=200)
    secondaryDriver = models.CharField(max_length=200)
    num_championships = models.IntegerField()


class Piloto(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    nacionality = models.CharField(max_length=100)
    escuderia = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()


class EstadisticaDriver(models.Model):
    nameDriver = models.CharField(max_length=200)
    num_of_championships = models.IntegerField()
    age_validity = models.IntegerField()
    num_dif_teams = models.IntegerField()
    name_dif_teams = models.CharField(max_length=100)


class EstadisticaScuderia(models.Model):
    nameScuderia = models.CharField(max_length=100)
    age_of_birth = models.IntegerField()
    num_of_championships = models.IntegerField()


class Circuito(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    circuit_length = models.IntegerField()
    laps_in_race = models.IntegerField()
    first_gp = models.IntegerField()
    race_distance = models.IntegerField()
    lap_record = models.CharField(max_length=100)


class Temporada(models.Model):
    year = models.IntegerField()
    num_gp = models.IntegerField()
    num_scuderias = models.IntegerField()
    world_champion = models.CharField(max_length=100)
