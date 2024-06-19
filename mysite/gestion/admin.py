from django.contrib import admin

from mysite.gestion.models import Profesor, Estudiante

# Register your models here.
admin.site.register(Profesor)
admin.site.register(Estudiante)