from django.db import models

# Modelos de Estudiante
class Estudiante(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    enrollment_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Profesor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    hire_date = models.DateField()
    specialization = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Profesores'

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.specialization}"

class Curso(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Matricula(models.Model):
    student = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    course = models.ForeignKey(Curso, on_delete=models.CASCADE)
    enrollment_date = models.DateField()

    def __str__(self):
        return f"{self.student} enrolled in {self.course} on {self.enrollment_date}"

class Asignatura(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Curso, related_name='subjects', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Nota(models.Model):
    student = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    course = models.ForeignKey(Curso, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student} - {self.course} : {self.grade}"