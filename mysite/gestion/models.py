from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Modelos
class Person(models.Model):
    ci = models.BigAutoField(primary_key=True, auto_created=True)       #ci de la persona
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(default=timezone.now)
    address = models.CharField(max_length=50, default=None)
    class Meta:
        db_table = 'person'
        verbose_name_plural = 'Personas'
        verbose_name = 'Persona'
        ordering = ['first_name', 'last_name']
    def datosPersona(self):
        return self.ci, self.first_name, self.last_name, self.birth_date
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

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
        return f'({self.id_career}){self.name_career}'


class Profile(models.Model):        #USUARIO
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')           #identificador unico, definido por el sistema
    ci = models.ForeignKey('Person', on_delete=models.CASCADE)
    name_user = models.CharField(max_length=150)
    email = models.EmailField(max_length=50, unique=True)
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
        ordering = ['user', 'ci']
    def __str__(self):
        return f'({self.ci}){self.user} ({self.user_type})'

class Student(models.Model):
    id_student = models.BigAutoField(primary_key=True, auto_created=True)      #identificador unico definido por el sistema
    ci = models.ForeignKey('Person', on_delete=models.CASCADE)
    id_career = models.ForeignKey('Career', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    assistance = models.BooleanField(default=False)
    behaviour = models.CharField(max_length=200, null=True, blank=True, default=None)
    #TODO implementar asistencia de alumno
    if status == "Vigente":
        # asistencia = models.
        pass
    else:
        if status == "De baja":
            pass
    class Meta:
        db_table = 'student'
        verbose_name_plural = 'Estudiantes'
        verbose_name = 'Estudiante'
        ordering = ['id_student', 'ci']
    def __str__(self):
        if self.status == True:
            self.status = "Vigente"
        else:
            self.status = "De baja"
        return f'{self.id_student} ({self.ci}){self.id_career} ({self.status})'

class Teacher(models.Model):
    id_teacher = models.BigAutoField(primary_key=True, auto_created=True)
    ci = models.ForeignKey('Person', on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50)
    id_subject = models.ForeignKey('Subject', on_delete=models.CASCADE, default=None)
    class Meta:
        db_table = 'teacher'
        verbose_name_plural = 'Profesores'
        verbose_name = 'Profesor'
        ordering = ['id_teacher', 'ci']
    def __str__(self):
        return f'{self.ci} {self.specialization}'

class Period(models.Model):
    id_period = models.BigAutoField(primary_key=True, auto_created=True)
    name_period = models.CharField(max_length=50)
    year_period = models.DateTimeField(auto_now_add=True)
    semester_period = models.PositiveSmallIntegerField()
    class Meta:
        db_table = 'period'
        verbose_name_plural = 'Periodos Academicos'
        verbose_name = 'Periodo Academico'
        ordering = ['id_period', 'year_period']
    def __str__(self):
        return f'({self.id_period}) {self.name_period} {self.year_period}'
class Subject(models.Model):
    id_subject = models.BigAutoField(primary_key=True, auto_created=True)
    name_subject = models.CharField(max_length=50, default=None)
    id_course = models.ForeignKey('Course', on_delete=models.CASCADE)
    id_teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    id_period = models.ForeignKey('Period', on_delete=models.CASCADE)
    id_schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE)
    class Meta:
        db_table = 'subject'
        verbose_name_plural = 'Asignaturas'
        verbose_name = 'Asignatura'
        ordering = ['id_subject']
    def __str__(self):
        return f'({self.id_subject}) {self.name_subject} ({self.id_period})'

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
        return f'({self.id_course}) {self.course_name} ({self.id_career})'

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
        return f'({self.id_registration}) {self.id_student} {self.id_subject}'

class Grades(models.Model):
    id_grades = models.BigAutoField(primary_key=True, auto_created=True)
    id_student = models.ForeignKey('Student', on_delete=models.CASCADE)
    id_course = models.ForeignKey('Course', on_delete=models.CASCADE)
    id_subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    note = models.TextField(default=None)
    evaluation_date = models.DateTimeField(auto_now_add=True)
    evaluation_type = models.IntegerField(default='ESC', choices=[
        ('ESC', 'Escrito'),
        ('ORAL', 'Oral'),
        ('PRAC', 'Practico'),
        ('MX', 'Mixto'),
    ])
    class Meta:
        db_table = 'grades'
        verbose_name = 'Calificación'
        verbose_name_plural = 'Calificaciones'
    def __str__(self):
        return f'({self.id_subject}) {self.id_student} {self.id_course} ({self.note})'