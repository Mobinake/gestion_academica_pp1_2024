from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Estudiante(models.Model):
    name = models.CharField(max_length=100)
    enrollment_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

class Profesor(models.Model):
    name = models.CharField(max_length=100)
    employee_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Curso(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Matricula(models.Model):
    student = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    course = models.ForeignKey(Curso, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.title}"

class Asignatura(models.Model):
    course = models.ForeignKey(Curso, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return self.title

class Nota(models.Model):
    assignment = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    student = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.student.name} - {self.assignment.title}: {self.grade}"