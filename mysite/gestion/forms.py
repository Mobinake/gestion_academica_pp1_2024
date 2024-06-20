from django import forms
from .models import Estudiante

class StudentForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['first_name', 'last_name', 'birth_date','email', 'phone', 'address', 'enrollment_date']