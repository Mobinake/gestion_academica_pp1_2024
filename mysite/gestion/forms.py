from django import forms
from .models import Student, User, Course, Carrer, AcademicPeriod, Grades, Registration, Person, Teacher, Subject

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'birth_date','email', 'phone', 'address', 'enrollment_date']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grades
        fields = ['student', 'subject', 'grade']