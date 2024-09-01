from django import forms
from .models import Rol, Usuario, Matricula, Materia, matricula_materia, tipo_evaluacion, Metodologia, Evaluacion

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'contrasena', 'estado', 'id_rol']

class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = [
            'id_tipo_evaluacion',
            'nombre_evaluacion',
            'id_metodologia',
            'total_puntos',
            'id_matricula_materia',
            'puntos_logrados',
            'descripcion'
        ]