from django.contrib.auth.models import User
from django.db import models
from django.urls.base import reverse

import formula1_project


# Create your models here.

class Scuderia(models.Model):
    name = models.CharField(max_length=200)
    main_color = models.CharField(max_length=100)
    principalDriver = models.CharField(max_length=200)
    secondaryDriver = models.CharField(max_length=200)
    num_championships = models.IntegerField()
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    # S'ha de canviar aixo
    def get_absolute_url(self):
        return reverse('scuderia')


class Driver(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    nationality = models.CharField(max_length=100)
    scuderia = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('driver')


class StatisticsDriver(models.Model):
    name = models.CharField(max_length=200)
    num_of_championships = models.IntegerField()
    num_dif_teams = models.IntegerField()
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('stats')


class Circuit(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    circuit_length = models.CharField(max_length=20)
    laps_in_race = models.IntegerField()
    first_gp = models.CharField(max_length=20)
    lap_record = models.CharField(max_length=100)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('circuit')


class Season(models.Model):
    year = models.IntegerField()
    num_gp = models.IntegerField()
    num_scuderias = models.IntegerField()
    world_champion = models.CharField(max_length=100)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('season')
