from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario, Matricula, Materia, matricula_materia, tipo_evaluacion, Metodologia, Evaluacion

User = get_user_model()


class FormularioRegistroUsuarioPersonalizado(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'estado']


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
