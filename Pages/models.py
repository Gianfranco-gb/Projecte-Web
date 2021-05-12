from django.db import models
import formula1_project
from django.contrib.auth.models import User


# Create your models here.

class Scuderia(models.Model):
    name = models.CharField(max_length=200)
    main_color = models.CharField(max_length=100)
    principalDriver = models.CharField(max_length=200)
    secondaryDriver = models.CharField(max_length=200)
    num_championships = models.IntegerField()


class Driver(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    nationality = models.CharField(max_length=100)
    scuderia = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)


class StatisticsDriver(models.Model):
    name = models.CharField(max_length=200)
    num_of_championships = models.IntegerField()
    num_dif_teams = models.IntegerField()


class Circuit(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    circuit_length = models.IntegerField()
    laps_in_race = models.IntegerField()
    first_gp = models.IntegerField()
    lap_record = models.CharField(max_length=100)


class Season(models.Model):
    year = models.IntegerField()
    num_gp = models.IntegerField()
    num_scuderias = models.IntegerField()
    world_champion = models.CharField(max_length=100)
