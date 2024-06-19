from django.db import models

# Modelos
class Estudiante(models.Model):
    first_name = models.CharField(max_length=50, default="unknow")
    last_name = models.CharField(max_length=50, default="unknow")
    birth_date = models.DateField(default="2024-07-01")
    enrollment_date = models.DateField(default='2024-07-01')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Profesor(models.Model):
    first_name = models.CharField(max_length=50, default="unknow")
    last_name = models.CharField(max_length=50, default="unknow")
    hire_date = models.DateField(default='2024-07-01')
    specialization = models.CharField(max_length=100, default="unknow")

    class Meta:
        verbose_name_plural='Profesores'

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.specialization}"

class Curso(models.Model):
    name = models.CharField(max_length=50, default="unknow")
    description = models.TextField(default="Vacio")
    teacher = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Matricula(models.Model):
    student = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)
    enrollment_date = models.DateField(default='2024-07-01')

    def __str__(self):
        return f"{self.student} enrolled in {self.course} on {self.enrollment_date}"

class Asignatura(models.Model):
    name = models.CharField(max_length=100, default="unknow")
    course = models.ForeignKey(Curso, related_name='subjects', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Nota(models.Model):
    student = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)
    grade = models.CharField(max_length=2, default=" ", null=True, blank=True)

    def __str__(self):
        return f"{self.student} - {self.course} : {self.grade}"