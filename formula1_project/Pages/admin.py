from django.contrib import admin
from .models import *
import formula1_project
# Register your models here.

admin.site.register(Escuderia)
admin.site.register(Piloto)
admin.site.register(Circuito)
admin.site.register(Estadistica)
admin.site.register(Temporada)