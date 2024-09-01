from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Rol, Usuario, Matricula, Materia, matricula_materia, tipo_evaluacion, Metodologia, Evaluacion

# Register your models here.
@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('id_rol', 'nombre')
    search_fields = ['nombre']

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'nombre', 'id_rol')
    search_fields = ['nombre', 'id_usuario']

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('id_matricula', 'fecha', 'id_usuario')
    list_filter = ['fecha', 'id_usuario']
    search_fields = ['id_matricula', 'fecha', 'id_usuario']

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('id_materia', 'nombre')
    search_fields = ['nombre', 'id_materia']

@admin.register(matricula_materia)
class MatriculaMateriaAdmin(admin.ModelAdmin):
    list_display = ('id_matri_mater', 'id_matricula', 'id_materia', 'estado')
    list_filter = ['id_matricula', 'id_materia', 'estado']
    search_fields = ['id_matri_mater', 'id_matricula', 'id_materia', 'estado']

@admin.register(tipo_evaluacion)
class TipoEvaluacionAdmin(admin.ModelAdmin):
    list_display = ('id_tipo_evaluacion', 'nombre')
    search_fields = ['nombre']

@admin.register(Metodologia)
class MetodologiaAdmin(admin.ModelAdmin):
    list_display = ('id_metodologia', 'nombre', 'descripcion')
    search_fields = ['nombre']

@admin.register(Evaluacion)
class EvaluacionAdmin(admin.ModelAdmin):
    list_display = ('id_evaluacion', 'nombre_evaluacion')
    list_filter = ['id_tipo_evaluacion', 'id_metodologia']
    search_fields = ['id_evaluacion', 'id_tipo_evaluacion', 'nombre_evaluacion', 'id_metodologia']


admin.site.site_header = "Panel de Administracion"
admin.site.site_title = "Gestión Académica"
admin.site.index_title = "Gestion Académica"
