from django.db import models
from django.db.models import AutoField, ForeignKey, CharField, IntegerField, DateField, BooleanField
from django.contrib.auth.models import User, AbstractUser


# Modelos
class Evaluacion(models.Model):
    id_evaluacion = AutoField(primary_key=True)
    id_tipo_evaluacion = ForeignKey('tipo_evaluacion', on_delete=models.CASCADE)
    nombre_evaluacion = CharField(max_length=100)
    id_metodologia = ForeignKey('Metodologia', on_delete=models.CASCADE)
    total_puntos = IntegerField(default=100)
    id_matricula_materia = ForeignKey('matricula_materia', on_delete=models.CASCADE)
    puntos_logrados = models.FloatField(default=0)
    descripcion = CharField(max_length=100)

    class Meta:
        db_table = 'evaluacion'
        verbose_name_plural = 'Evaluaciones'
        verbose_name = 'Evaluacion'
        ordering = ['id_evaluacion', 'id_tipo_evaluacion', 'id_metodologia']

    def __str__(self):
        return self.nombre_evaluacion
#TODO: cuando el profesor crea una evaluacion, se le asignara a todos los alumnos

# con esto se va a listar los nombre de los profesores en materia
class Horario(models.Model):
    id_horario = AutoField(primary_key=True)
    id_materia = ForeignKey('Materia', on_delete=models.CASCADE)
    id_usuario = ForeignKey('Usuario', on_delete=models.CASCADE)
    date = CharField(max_length=25, blank=False)
    hora_inicio = DateField(blank=False)
    hora_fin = DateField(blank=False)

    class Meta:
        db_table = 'horario'
        verbose_name_plural = 'Horarios'
        verbose_name = 'Horario'
        ordering = ['id_horario']

#TODO: para materia, se usa el id_usuario para filtrar. para obtener el nombre de la materia se usa el id_materia
# en la vista de materia, usar esos id_usuario para filtrar y obtener el nombre de la materia con id_materia

class Materia(models.Model):
    id_materia = AutoField(primary_key=True)
    nombre_materia = CharField(max_length=50, blank=False)
    estado = CharField(max_length=25, blank=False, default="Inactivo")
    anio = IntegerField(blank=False, default=2020)


    class Meta:
        db_table = 'materia'
        verbose_name_plural = 'Materias'
        verbose_name = 'Materia'
        ordering = ['id_materia', 'nombre_materia']

    def __str__(self):
        return self.nombre_materia


class Matricula(models.Model):
    id_matricula = AutoField(primary_key=True)
    detalles = CharField(max_length=150)
    monto = IntegerField(blank=False)
    fecha = DateField(auto_now_add=True)
    id_usuario = ForeignKey('Usuario', on_delete=models.CASCADE)

    class Meta:
        db_table = 'matricula'
        verbose_name_plural = 'Matriculas'
        verbose_name = 'Matricula'
        ordering = ['id_matricula', 'fecha']

    def __str__(self):
        return str(self.id_matricula) + "-" + self.id_usuario.username


class matricula_materia(models.Model):
    id_matri_mater = AutoField(primary_key=True)
    id_matricula = ForeignKey('Matricula', on_delete=models.CASCADE)
    id_materia = ForeignKey('Materia', on_delete=models.CASCADE)
    nombre_matricula_materia = CharField(max_length=100)
    estado = BooleanField(default=True)

    def __str__(self):
        return self.nombre_matricula_materia


class Metodologia(models.Model):
    id_metodologia = AutoField(primary_key=True)
    nombre_metodologia = CharField(max_length=50)
    descripcion = CharField(max_length=100)

    class Meta:
        db_table = 'metodologia'
        verbose_name_plural = 'Metodologias'
        verbose_name = 'Metodologia'
        ordering = ['id_metodologia', 'nombre_metodologia']

    def __str__(self):
        return self.nombre_metodologia


class tipo_evaluacion(models.Model):
    id_tipo_evaluacion = AutoField(primary_key=True)
    nombre_tipo_evaluacion = CharField(max_length=50)

    class Meta:
        db_table = 'tipo_evaluacion'
        verbose_name_plural = 'Tipos de Evaluaciones'
        verbose_name = 'Tipo de Evaluacion'
        ordering = ['id_tipo_evaluacion', 'nombre_tipo_evaluacion']

    def __str__(self):
        return self.nombre_tipo_evaluacion


class Usuario(AbstractUser):
    def __str__(self):
        return self.username
