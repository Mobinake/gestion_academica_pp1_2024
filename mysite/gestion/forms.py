from django import forms
from .models import Noticias, Usuario

class NoticiasForm(forms.ModelForm):
    class Meta:
        model = Noticias
        fields = ['titulo', 'contenido', 'id_usuario']

    id_usuario = forms.ModelChoiceField(
        queryset=Usuario.objects.all(),  # Cambia User por Usuario
        label="Autor",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ingrese el título'})
        self.fields['contenido'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ingrese el contenido'})
