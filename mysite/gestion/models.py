from django.db import models
from django.utils import timezone
# Modelos
class Person(models.Model):
    id_person = models.BigAutoField(primary_key=True, auto_created=True)       #ci de la persona
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = 'person'
        verbose_name_plural = 'Personas'
        verbose_name = 'Persona'
        ordering = ['first_name', 'last_name']
    def datosPersona(self):
        return self.id_person, self.first_name, self.last_name, self.birth_date
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Carrer(models.Model):
    id_carrer = models.BigAutoField(primary_key=True, auto_created=True)
    name_carrer = models.CharField(max_length=50, default=None)
    faculty = models.CharField(max_length=50, default=None)
    duracion = models.PositiveSmallIntegerField(default=5)
    class Meta:
        db_table = 'carrer'
        verbose_name_plural = 'Carreras'
        verbose_name = 'Carrera'
        ordering = ['id_carrer', 'name_carrer']
    def __str__(self):
        return f'{self.name_carrer} ({self.duracion})'


class User(models.Model):
    id_user = models.BigAutoField(primary_key=True, auto_created=True)            #identificador unico, definido por el sistema
    id_person = models.ForeignKey('Person', on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, unique=True)
    #pass_hash = models.CharField(max_length=50)
    #salt = models.CharField(max_length=50)
    type = [
        ('EST', 'Estudiante'),
        ('PRO', 'Profesor'),
        ('ADM', 'Administrativo'),
    ]
    user_type = models.CharField(max_length=3, choices=type, default='EST')
    class Meta:
        db_table = 'user'
        verbose_name_plural = 'Usuarios'
        verbose_name = 'Usuario'
        ordering = ['id_user', 'id_person']
    def __str__(self):
        return f'({self.id_person}){self.id_user} ({self.user_type})'

class Student(models.Model):
    id_student = models.BigAutoField(primary_key=True)      #identificador unico definido por el sistema
    id_person = models.ForeignKey('Person', on_delete=models.CASCADE)
    id_carrer = models.ForeignKey('Carrer', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    class Meta:
        db_table = 'student'
        verbose_name_plural = 'Estudiantes'
        verbose_name = 'Estudiante'
        ordering = ['id_student', 'id_person']
    def __str__(self):
        if self.status == True:
            estadoEstudiante = "Vigente"
        else:
            estadoEstudiante = "De baja"
        return f'{self.id_student} ({self.id_person}){self.id_carrer} ({estadoEstudiante})'

class Teacher(models.Model):
    id_teacher = models.BigAutoField(primary_key=True)
    id_person = models.ForeignKey('Person', on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50)
    id_subject = models.ForeignKey('Subject', on_delete=models.CASCADE, default=None)
    class Meta:
        db_table = 'teacher'
        verbose_name_plural = 'Profesores'
        verbose_name = 'Profesor'
        ordering = ['id_teacher', 'id_person']
    def __str__(self):
        return f'{self.id_person}'

class AcademicPeriod(models.Model):
    id_academicPeriod = models.BigAutoField(primary_key=True)
    name_academicPeriod = models.CharField(max_length=50)
    year_academicPeriod = models.DateTimeField(auto_now_add=True)
    semester_academicPeriod = models.IntegerField()
    class Meta:
        db_table = 'academicperiod'
        verbose_name_plural = 'Periodos Academicos'
        verbose_name = 'Periodo Academico'
        ordering = ['id_academicPeriod', 'year_academicPeriod']
    def __str__(self):
        return f'({self.id_academicPeriod}) {self.name_academicPeriod}'
class Subject(models.Model):
    id_subject = models.BigAutoField(primary_key=True)
    name_subject = models.CharField(max_length=50, default=None)
    id_academicPeriod = models.ForeignKey('AcademicPeriod', on_delete=models.CASCADE)
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
        db_table = 'subject'
        verbose_name_plural = 'Asignaturas'
        verbose_name = 'Asignatura'
        ordering = ['id_subject']
    def __str__(self):
        return f'({self.id_subject}) {self.name_subject} ({self.id_academicPeriod})'

class Course(models.Model):
    id_course = models.BigAutoField(primary_key=True)
    course_name = models.CharField(max_length=50)
    course_description = models.TextField()
    id_carrer = models.ForeignKey('Carrer', on_delete=models.CASCADE)
    id_subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    class Meta:
        db_table = 'course'
        verbose_name_plural= 'Cursos'
        verbose_name = 'Curso'
        ordering = ['id_course', 'course_name']
    def __str__(self):
        return f'({self.id_course}) {self.course_name} ({self.id_carrer})'

class Registration(models.Model):
    id_registration = models.BigAutoField(primary_key=True)
    id_student = models.ForeignKey('Student', on_delete=models.CASCADE)
    id_subject = models.ForeignKey('Carrer', on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'registration'
        verbose_name_plural = 'Matriculas'
        verbose_name = 'Matricula'
        ordering = ['id_registration', 'id_student', 'id_subject']
    def __str__(self):
        return f'({self.id_registration}) {self.id_student} {self.id_subject}'

class Grades(models.Model):
    id_grades = models.BigAutoField(primary_key=True)
    id_student = models.ForeignKey('Student', on_delete=models.CASCADE)
    id_curse = models.ForeignKey('Course', on_delete=models.CASCADE)
    id_subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    note = models.TextField(default=None)
    evaluation_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'grades'
        verbose_name = 'Calificación'
        verbose_name_plural = 'Calificaciones'
    def __str__(self):
        return f'({self.id_subject}) {self.id_student} {self.id_curse} ({self.note})'