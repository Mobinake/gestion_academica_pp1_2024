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
    descripcion = CharField(max_length=100)

    class Meta:
        db_table = 'evaluacion'
        verbose_name_plural = 'Evaluaciones'
        verbose_name = 'Evaluacion'
        ordering = ['id_evaluacion', 'id_tipo_evaluacion', 'id_metodologia']

    def __str__(self):
        return self.nombre_evaluacion


# con esto se va a listar los nombre de los profesores en materia
class Horario(models.Model):
    DIAS_DE_LA_SEMANA = [
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]
    id_horario = AutoField(primary_key=True)
    id_materia = ForeignKey('Materia', on_delete=models.CASCADE)
    id_usuario = ForeignKey('Usuario', on_delete=models.CASCADE)
    date = models.CharField(max_length=10, choices=DIAS_DE_LA_SEMANA, default="lunes")
    hora_inicio = models.TimeField(blank=False)
    hora_fin = models.TimeField(blank=False)

    class Meta:
        db_table = 'horario'
        verbose_name_plural = 'Horarios'
        verbose_name = 'Horario'
        ordering = ['id_horario']


class Materia(models.Model):
    ESTADO_MATERIA = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('termminado', 'Terminado'),
    ]
    id_materia = AutoField(primary_key=True)
    nombre_materia = CharField(max_length=50, blank=False)
    estado = CharField(max_length=25, choices=ESTADO_MATERIA, default="inactivo")
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
        return f"{self.id_materia.nombre_materia} - {self.id_matricula.id_usuario.username}"


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
