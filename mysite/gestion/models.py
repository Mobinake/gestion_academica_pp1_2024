from django.db import models

# Modelos

class Person(models.Model):
    id_person = models.IntegerField(primary_key=True)       #ci de la persona
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'person'
        verbose_name_plural = 'Personas'
        verbose_name = 'Persona'
        ordering = ['first_name', 'last_name']
    def datosPersona(self):
        return self.id_person, self.first_name, self.last_name, self.birth_date

class User(models.Model):
    id_user = models.AutoField(primary_key=True)            #identificador unico, definido por el sistema
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, unique=True)
    pass_hash = models.CharField(max_length=50)
    salt = models.CharField(max_length=50)
    tipe = [
        ('EST', 'Estudiante'),
        ('PRO', 'Profesor'),
        ('ADM', 'Administrativo'),
    ]
    user_tipe = models.CharField(max_length=3, choices=tipe, default='EST')
    if user_tipe == 'EST':
        carrer = models.ForeignKey(Carrer, null=False, blank=False, on_delete=models.CASCADE)
    class Meta:
        db_table = 'user'
        verbose_name_plural = 'Usuarios'
        verbose_name = 'Usuario'
        ordering = ['id_user', 'id_person']
    def datosUser(self):
        return self.id_user, self.email, self.user_tipe

class Student(models.Model):
    id_student = models.IntegerField(primary_key=True)      #identificador unico definido por el sistema
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    id_carrer = models.ForeignKey(Carrer, null=False, blank=False, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    class Meta:
        db_table = 'student'
        verbose_name_plural = 'Estudiantes'
        verbose_name = 'Estudiante'
        ordering = ['id_student', 'id_person']
    def nombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.id_student, self.id_person, self.id_carrer)

class Carrer(models.Model):
    id_carrer = models.AutoField(primary_key=True)
    name_carrer = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)
    class Meta:
        db_table = 'carrer'
        verbose_name_plural = 'Carreras'
        verbose_name = 'Carrera'
        ordering = ['id_carrer', 'name_carrer']
    def datosCarrer(self):
        return self.name_carrer, self.faculty

class Teacher(models.Model):
    id_teacher = models.IntegerField(primary_key=True)
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50)
    class Meta:
        db_table = 'profesor'
        verbose_name_plural = 'Profesores'
        verbose_name = 'Profesor'
        ordering = ['id_teacher', 'id_person']
    def datosProfesor(self):
        return self.id_teacher, self.id_person, self.specialization

class Course(models.Model):
    id_course = models.AutoField(primary_key=True)
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

class Registration(models.Model):
    id_registration = models.AutoField(primary_key=True, auto_created=True)
    id_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    id_subject = models.ForeignKey(Carrer, on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'registration'
        verbose_name_plural = 'Matriculas'
        verbose_name = 'Matricula'
        ordering = ['id_registration', 'id_student', 'id_subject']
    def datosRegistration(self):
        return self.id_registration, self.id_student, self.id_subject, self.registration_date

class Subject(models.Model):
    id_subject = models.AutoField(primary_key=True, auto_created=True)
    id_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    id_academicPeriod = models.ForeignKey(AcademicPeriod, on_delete=models.CASCADE)
    class Meta:
        db_table = 'subject'
        verbose_name_plural = 'Asignaturas'
        verbose_name = 'Asignatura'
        ordering = ['id_subject', 'id_teacher']
    def datosAsignatura(self):
        return self.id_subject, self.id_teacher, self.id_academicPeriod

class AcademicPeriod(models.Model):
    id_academicPeriod = models.AutoField(primary_key=True, auto_created=True)
    name_academicPeriod = models.CharField(max_length=50)
    year_academicPeriod = models.DateField(auto_now_add=True)
    semester_academicPeriod = models.IntegerField()
    class Meta:
        db_table = 'academicperiod'
        verbose_name_plural = 'Periodos Academicos'
        verbose_name = 'Periodo Academico'
        ordering = ['id_academicPeriod', 'year_academicPeriod']
    def datosAacademicPeriod(self):
        return self.id_academicPeriod, self.name_academicPeriod, self.year_academicPeriod, self.semester_academicPeriod

class Grades(models.Model):
    id_grades = models.AutoField(primary_key=True, auto_created=True)
    id_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    id_curse = models.ForeignKey(Curse, on_delete=models.CASCADE)
    id_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    note = models.TextField(default='')
    evaluation_date = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'grades'
        verbose_name = 'Calificación'
        verbose_name_plural = 'Calificaciones'
    def datosGrades(self):
        return self.id_subject, self.id_student, self.id_curse, self.id_subject, self.note, self.evaluation_date