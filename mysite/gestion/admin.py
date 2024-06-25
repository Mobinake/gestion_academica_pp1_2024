from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Profesor, Student, Secretario, Curso, Matricula, Asignatura, Grade

# Register your models here.

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'hire_date', 'specialization')
    search_fields = ('first_name', 'last_name', 'specialization')
    list_filter = ('hire_date', 'specialization')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date', 'enrollment_date')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('enrollment_date',)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user__groups__name__in=['secretario cyt', 'admin del sistema'])

@admin.register(Secretario)
class SecretarioAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user__groups__name='secretario cyt')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')
    search_fields = ('name', 'teacher__first_name', 'teacher__last_name')

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date')
    search_fields = ('student__first_name', 'student__last_name', 'course__name')
    list_filter = ('enrollment_date', 'course')

@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('name', 'course')
    search_fields = ('name', 'course__name')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'grade', 'date_recorded')
    search_fields = ('student__first_name', 'student__last_name', 'subject')
    list_filter = ('date_recorded', 'subject')

admin.site.site_header = "Panel de Administracion"
admin.site.site_title = "Gestión Académica"
admin.site.index_title = "Gestion Academica"