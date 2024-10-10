from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import Usuario, Matricula, Materia, matricula_materia, tipo_evaluacion, Metodologia, Evaluacion

# Register your models here.
user = get_user_model()


class CustomUserAdmin(UserAdmin):
    pass


admin.site.register(user, CustomUserAdmin)


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('id_matricula', 'fecha', 'id_usuario')
    list_filter = ['fecha', 'id_usuario']
    search_fields = ['id_matricula', 'fecha', 'id_usuario']


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('id_materia', 'nombre_materia')
    search_fields = ['nombre_materia', 'id_materia']


@admin.register(matricula_materia)
class MatriculaMateriaAdmin(admin.ModelAdmin):
    list_display = ('id_matri_mater', 'id_matricula', 'id_materia', 'estado')
    list_filter = ['id_matricula', 'id_materia', 'estado']
    search_fields = ['id_matri_mater', 'id_matricula', 'id_materia', 'estado']


@admin.register(tipo_evaluacion)
class TipoEvaluacionAdmin(admin.ModelAdmin):
    list_display = ('id_tipo_evaluacion', 'nombre_tipo_evaluacion')
    search_fields = ['nombre_tipo_evaluacion', 'id_tipo_evaluacion']


@admin.register(Metodologia)
class MetodologiaAdmin(admin.ModelAdmin):
    list_display = ('id_metodologia', 'nombre_metodologia', 'descripcion')
    search_fields = ['nombre_metodologia']


@admin.register(Evaluacion)
class EvaluacionAdmin(admin.ModelAdmin):
    list_display = ('id_evaluacion', 'nombre_evaluacion')
    list_filter = ['id_tipo_evaluacion', 'id_metodologia']
    search_fields = ['id_evaluacion', 'id_tipo_evaluacion', 'nombre_evaluacion', 'id_metodologia']


admin.site.site_header = "Panel de Administracion"
admin.site.site_title = "Gestión Académica"
admin.site.index_title = "Gestion Académica"
