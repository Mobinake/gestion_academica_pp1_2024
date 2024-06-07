from django.contrib import admin

# Register your models here.
from .models import Estudiante, Profesor, Curso, Matricula, Asignatura, Nota

admin.site.register(Estudiante)
