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
    id_carrer = models.BigAutoField(primary_key=True)
    name_carrer = models.CharField(max_length=50, default="ingese el nombre de la carrera")
    faculty = models.CharField(max_length=50, default="Ingrese el nombre de la facultad")
    class Meta:
        db_table = 'carrer'
        verbose_name_plural = 'Carreras'
        verbose_name = 'Carrera'
        ordering = ['id_carrer', 'name_carrer']
    def datosCarrer(self):
        return self.name_carrer, self.faculty
    def __str__(self):
        return f'{self.name_carrer} {self.faculty}'


class User(models.Model):
    id_user = models.BigAutoField(primary_key=True, auto_created=True)            #identificador unico, definido por el sistema
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
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
    def datosUser(self):
        return self.id_user, self.email, self.user_type
    def __str__(self):
        return f'{self.id_user} {self.email}'

class Student(models.Model):
    id_student = models.BigAutoField(primary_key=True)      #identificador unico definido por el sistema
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    id_carrer = models.ForeignKey(Carrer, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    class Meta:
        db_table = 'student'
        verbose_name_plural = 'Estudiantes'
        verbose_name = 'Estudiante'
        ordering = ['id_student', 'id_person']
    def nombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.id_student, self.id_person, self.id_carrer)
    def __str__(self):
        return f'{self.id_student} {self.id_person} {self.id_carrer}'

class Teacher(models.Model):
    id_teacher = models.BigAutoField(primary_key=True)
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50)
    class Meta:
        db_table = 'teacher'
        verbose_name_plural = 'Profesores'
        verbose_name = 'Profesor'
        ordering = ['id_teacher', 'id_person']
    def datosProfesor(self):
        return self.id_teacher, self.id_person, self.specialization
    def __str__(self):
        return f'{self.id_teacher} {self.id_person} {self.specialization}'

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
    def datosAacademicPeriod(self):
        return self.id_academicPeriod, self.name_academicPeriod, self.year_academicPeriod, self.semester_academicPeriod
    def __str__(self):
        return f'{self.id_academicPeriod} {self.name_academicPeriod} {self.year_academicPeriod}'
class Subject(models.Model):
    id_subject = models.BigAutoField(primary_key=True)
    id_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name_subject = models.CharField(max_length=50, default="Ingrese el nombre de la materia")
    id_academicPeriod = models.ForeignKey(AcademicPeriod, on_delete=models.CASCADE)
    class Meta:
        db_table = 'subject'
        verbose_name_plural = 'Asignaturas'
        verbose_name = 'Asignatura'
        ordering = ['id_subject', 'id_teacher']
    def datosAsignatura(self):
        return self.id_subject, self.id_teacher, self.id_academicPeriod
    def __str__(self):
        return f'{self.id_subject} {self.id_teacher} {self.id_academicPeriod}'

class Course(models.Model):
    id_course = models.BigAutoField(primary_key=True)
    course_name = models.CharField(max_length=50)
    course_description = models.TextField()
    id_carrer = models.ForeignKey(Carrer, on_delete=models.CASCADE)
    id_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class Meta:
        db_table = 'course'
        verbose_name_plural= 'Cursos'
        verbose_name = 'Curso'
        ordering = ['id_course', 'course_name']
    def datosCourse(self):
        return self.id_course, self.course_name, self.course_description, self.id_carrer, self.id_subject
    def __str__(self):
        return f'{self.id_course} {self.course_name} {self.course_description}'

class Registration(models.Model):
    id_registration = models.BigAutoField(primary_key=True)
    id_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    id_subject = models.ForeignKey(Carrer, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'registration'
        verbose_name_plural = 'Matriculas'
        verbose_name = 'Matricula'
        ordering = ['id_registration', 'id_student', 'id_subject']
    def datosRegistration(self):
        return self.id_registration, self.id_student, self.id_subject, self.registration_date
    def __str__(self):
        return f'{self.id_registration} {self.id_student} {self.id_subject}'

class Grades(models.Model):
    id_grades = models.BigAutoField(primary_key=True)
    id_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    id_curse = models.ForeignKey(Course, on_delete=models.CASCADE)
    id_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    note = models.TextField(default='')
    evaluation_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'grades'
        verbose_name = 'Calificación'
        verbose_name_plural = 'Calificaciones'
    def datosGrades(self):
        return self.id_subject, self.id_student, self.id_curse, self.id_subject, self.note, self.evaluation_date
    def __str__(self):
        return f'{self.id_grades} {self.id_student} {self.id_curse} {self.id_subject}'