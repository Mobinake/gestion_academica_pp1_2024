from django.db import models
from django.db.models import AutoField, ForeignKey, CharField, IntegerField, DateField, BooleanField
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser

# Modelos
class Usuario(AbstractUser):
    estado = models.BooleanField(default=True)
    def __str__(self):
        return self.username

#TODO agregar campos pendientes del diagrama

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
        return self.detalles

class Materia(models.Model):
    id_materia = AutoField(primary_key=True)
    nombre_materia = CharField(max_length=50, blank=False)
    class Meta:
        db_table = 'materia'
        verbose_name_plural = 'Materias'
        verbose_name = 'Materia'
        ordering = ['id_materia', 'nombre_materia']

    def __str__(self):
        return self.nombre_materia


class matricula_materia(models.Model):
    id_matri_mater = AutoField(primary_key=True)
    id_matricula = ForeignKey('Matricula', on_delete=models.CASCADE)
    id_materia = ForeignKey('Materia', on_delete=models.CASCADE)
    nombre_matricula_materia = CharField(max_length=100)
    estado = BooleanField(default=True)
    def __str__(self):
        return self.nombre_matricula_materia

class tipo_evaluacion(models.Model):
    id_tipo_evaluacion = AutoField(primary_key=True)
    nombre_tipo_evaluacion = CharField(max_length=50)
    def __str__(self):
        return self.nombre_tipo_evaluacion

class Metodologia(models.Model):
    id_metodologia = AutoField(primary_key=True)
    nombre_metodologia = CharField(max_length=50)
    descripcion = CharField(max_length=100)
    def __str__(self):
        return self.nombre_metodologia

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


#TODO unificar rama dev con main
#TODO levantar en rama master con un tag de version
