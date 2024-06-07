from django.db import models

# Create your models here.
class Profesor(models.Model):
    name = models.CharField(max_length=100)
    employee_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name_plural='Profesores'
    def __str__(self):
        return self.name

class Curso(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title