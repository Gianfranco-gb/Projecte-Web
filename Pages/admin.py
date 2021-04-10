from django.contrib import admin
from .models import *
import formula1_project
# Register your models here.

admin.site.register(Scuderia)
admin.site.register(Driver)
admin.site.register(StatisticsDriver)
admin.site.register(StatisticsScuderia)
admin.site.register(Circuit)
admin.site.register(Season)
