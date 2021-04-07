from django.db import models
import formula1_project
# Create your models here.

class Escuderia(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    priority = models.IntegerField(default=1)

class Piloto(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    priority = models.IntegerField(default=1)

class Estadistica(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    priority = models.IntegerField(default=1)

class Circuito(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    priority = models.IntegerField(default=1)

class Temporada(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    priority = models.IntegerField(default=1)