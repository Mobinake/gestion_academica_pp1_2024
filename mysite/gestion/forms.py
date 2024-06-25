from django import forms
from .models import Estudiante, Nota

class StudentForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['first_name', 'last_name', 'birth_date','email', 'phone', 'address', 'enrollment_date']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['student', 'subject', 'grade']