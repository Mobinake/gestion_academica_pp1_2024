from django.db import models

# Modelos
class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    creditos = models.IntegerField()
    semestre = models.IntegerField()
    docente = models.CharField(max_length=100)
    metodo_evaluacion = models.CharField(max_length=20, choices=[
        ('Oral', 'Oral'),
        ('Escrito teórico', 'Escrito teórico'),
        ('Práctico', 'Práctico'),
        ('Teórico-Práctico', 'Teórico-Práctico'),
    ], default='Oral', verbose_name='Método de evaluación')
    metodologia = models.TextField(verbose_name='Metodología')

    def __str__(self):
        return self.nombre

class Horario(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    dia = models.CharField(max_length=20)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    aula = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.materia} - {self.dia} - {self.hora_inicio} a {self.hora_fin}"
