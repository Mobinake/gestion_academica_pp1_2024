from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Profesor, Estudiante

# Register your models here.

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','hire_date','specialization')
    search_fields = ('first_name', 'last_name', 'hire_date', 'specialization')
    list_filter = ('first_name', 'last_name', 'hire_date', 'specialization')

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','birth_date','enrollment_date')
    search_fields = ('first_name', 'last_name', 'birth_date', 'enrollment_date')
    list_filter = ('first_name', 'last_name', 'birth_date', 'enrollment_date')
    # futura implementacion de administracion de permisos
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(groups__name=['secretario cyt', 'admin del sistema'])

admin.site.site_header = "Panel de Administracion"
admin.site.site_title = "Gestión Académica"
admin.site.index_title = "Gestion Academica"