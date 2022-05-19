from django.contrib import admin

from .models import Carrera, Ciudad, Pais, Provincia, TipoCarrera

# Register your models here.

admin.site.register(Pais)

admin.site.register(Provincia)

admin.site.register(Ciudad)

admin.site.register(Carrera)

admin.site.register(TipoCarrera)