from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Modelos
class Person(models.Model):
    ci = models.BigIntegerField(primary_key=True, auto_created=True)       #ci de la persona
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(default=timezone.now)
    address = models.CharField(max_length=50, default=None)
    class Meta:
        db_table = 'person'
        verbose_name_plural = 'Personas'
        verbose_name = 'Persona'
        ordering = ['ci', 'first_name', 'last_name']
    def datosPersona(self):
        return self.ci, self.first_name, self.last_name, self.birth_date
    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.ci}'

class Career(models.Model):
    id_career = models.BigAutoField(primary_key=True, auto_created=True)
    name_career = models.CharField(max_length=50, default=None)
    faculty = models.CharField(max_length=50, default=None)
    class Meta:
        db_table = 'career'
        verbose_name_plural = 'Carreras'
        verbose_name = 'Carrera'
        ordering = ['id_career', 'name_career']
    def __str__(self):
        return f'{self.id_career} - {self.name_career}'

class Student(models.Model):
    id_student = models.BigAutoField(primary_key=True, auto_created=True)      #identificador unico definido por el sistema
    ci = models.ForeignKey('Person', on_delete=models.CASCADE)
    id_career = models.ForeignKey('Career', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    assistance = models.BooleanField(default=False)
    behaviour = models.CharField(max_length=200, null=True, blank=True, default=None)
    class Meta:
        db_table = 'student'
        verbose_name_plural = 'Estudiantes'
        verbose_name = 'Estudiante'
        ordering = ['id_student', 'ci']
    def __str__(self):
        return f'{self.ci}'

class Teacher(models.Model):
    id_teacher = models.BigAutoField(primary_key=True, auto_created=True)
    ci = models.ForeignKey('Person', on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50)
    class Meta:
        db_table = 'teacher'
        verbose_name_plural = 'Profesores'
        verbose_name = 'Profesor'
        ordering = ['id_teacher', 'ci']
    def __str__(self):
        return f'{self.ci} - {Person.first_name} {Person.last_name}'

class Period(models.Model):
    id_period = models.BigAutoField(primary_key=True, auto_created=True)
    name_period = models.CharField(max_length=50)
    year_period = models.DateTimeField(auto_now_add=True)
    semester_period = models.PositiveSmallIntegerField()
    class Meta:
        db_table = 'period'
        verbose_name_plural = 'Periodos'
        verbose_name = 'Periodo'
        ordering = ['id_period', 'name_period', 'year_period']
    def __str__(self):
        return f'{self.id_period} {self.name_period} {self.year_period}'
class Subject(models.Model):
    id_subject = models.BigAutoField(primary_key=True, auto_created=True)
    name_subject = models.CharField(max_length=150, default=None)
    id_course = models.ForeignKey('Course', on_delete=models.CASCADE)
    id_period = models.ForeignKey('Period', on_delete=models.CASCADE)
    class Meta:
        db_table = 'subject'
        verbose_name_plural = 'Asignaturas'
        verbose_name = 'Asignatura'
        ordering = ['id_subject', 'name_subject']
    def __str__(self):
        return f'{self.name_subject}'

class Schedule(models.Model):
    id_schedule = models.BigAutoField(primary_key=True, auto_created=True)
    id_subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    day = models.CharField(max_length=10, default='LUN', choices=[
        ('LUN', 'Lunes'),
        ('MAR', 'Martes'),
        ('MIE', 'Miércoles'),
        ('JUE', 'Jueves'),
        ('VIE', 'Viernes'),
        ('SAB', 'Sábado'),
        ('DOM', 'Domingo'),
    ])
    time_start = models.TimeField(default='09:00')
    time_end = models.TimeField(default='12:00')
    class Meta:
        db_table = 'schedule'
        verbose_name_plural = 'Horarios'
        verbose_name = 'Horario'
        ordering = ['id_subject', 'day']
    def __str__(self):
        return f'{self.id_schedule} {self.day}'

class Course(models.Model):
    id_course = models.BigAutoField(primary_key=True, auto_created=True)
    id_career = models.ForeignKey('Career', on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50)
    class Meta:
        db_table = 'course'
        verbose_name_plural = 'Cursos'
        verbose_name = 'Curso'
        ordering = ['id_course', 'course_name']
    def __str__(self):
        return f'{self.course_name}{self.id_career}'

class Registration(models.Model):
    id_registration = models.BigAutoField(primary_key=True, auto_created=True)
    id_student = models.ForeignKey('Student', on_delete=models.CASCADE)
    id_subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    account_state = models.CharField(max_length=15, default=None, choices=[
        ('AD', 'Al dia'),
        ('D1', 'Debe 1 cuota'),
        ('D2', 'Debe 2 cuotas'),
        ('D3', 'Debe 3 cuotas'),
        ('D4', 'Debe 4 cuotas'),
        ('D5', 'Debe 5 cuotas'),
    ])
    class Meta:
        db_table = 'registration'
        verbose_name_plural = 'Matriculas'
        verbose_name = 'Matricula'
        ordering = ['id_registration', 'id_student', 'id_subject']
    def __str__(self):
        return f'{self.id_registration} - {Person.first_name} {Person.last_name}'

class Grades(models.Model):
    id_grades = models.BigAutoField(primary_key=True, auto_created=True)
    id_student = models.ForeignKey('Student', on_delete=models.CASCADE)
    id_course = models.ForeignKey('Course', on_delete=models.CASCADE)
    id_subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    note = models.IntegerField(default=None, blank=True, null=True, choices=[
        (1, 'Uno'),
        (2, 'Dos'),
        (3, 'Tres'),
        (4, 'Cuatro'),
        (5, 'Cinco'),
    ])
    evaluation_date = models.DateTimeField(auto_now_add=True)
    evaluation_type = models.CharField(default='ESC',max_length=20, choices=[
        ('ESC', 'Escrito'),
        ('ORAL', 'Oral'),
        ('PRAC', 'Practico'),
        ('MX', 'Mixto'),
    ])
    class Meta:
        db_table = 'grades'
        verbose_name = 'Calificación'
        verbose_name_plural = 'Calificaciones'
        ordering = ['id_student', 'id_student', 'note' ]
    def __str__(self):
        return f'{self.id_student} {Person.first_name} {Person.last_name}'

