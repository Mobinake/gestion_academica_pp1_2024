from django.contrib import admin
from .models import Materia, Horario

# registro de modelos
@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'creditos', 'semestre', 'docente')
    list_filter = ('nombre',)

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('materia', 'dia', 'hora_inicio', 'hora_fin', 'aula')