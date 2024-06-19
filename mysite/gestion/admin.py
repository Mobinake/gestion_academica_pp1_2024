from django.contrib import admin
from .models import Profesor, Estudiante

# Register your models here.

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    pass
@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    pass

class FlatPageAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": ["url", "title", "content", "sites"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["registration_required", "template_name"],
            },
        ),
    ]