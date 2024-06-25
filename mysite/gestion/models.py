from django.db import models

# Modelos

class Secretario(models.Model):
    first_name = models.CharField(max_length=50, default="secretario")
    last_name = models.CharField(max_length=50, default="apellido_secretario_opcional")
    birth_date = models.DateField(default="2024-07-01")
    email = models.EmailField(default="email")
    phone = models.CharField(max_length=50, default="0")
    address = models.CharField(max_length=50, default="desconocido")
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    ordering = ('firts_name','last_name')
    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Secretario'
        verbose_name_plural = 'Secretarios'
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Estudiante(models.Model):
    first_name = models.CharField(max_length=50, default="desconocido")
    last_name = models.CharField(max_length=50, default="desconocido")
    birth_date = models.DateField(default="2024-07-01")
    email = models.EmailField(default="email")
    phone = models.CharField(max_length=50, default="0")
    address = models.CharField(max_length=50, default="desconocido")
    enrollment_date = models.DateField(default='2024-07-01')
    class Meta:
        db_table = 'estudiante'
        verbose_name_plural = 'Estudiantes'
        verbose_name = 'Estudiante'
        ordering = ['first_name', 'last_name']
        permissions = [
            ("can_view_grades", "Puede ver sus calificaciones"),
            ("can_edit_profile", "Puede editar su perfil"),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Profesor(models.Model):
    first_name = models.CharField(max_length=50, default="desconocido")
    last_name = models.CharField(max_length=50, default="desconocido")
    hire_date = models.DateField(default='2024-07-01')
    specialization = models.CharField(max_length=100, default="desconocido")
    class Meta:
        db_table = 'profesor'
        verbose_name_plural = 'Profesores'
        verbose_name = 'Profesor'
        ordering = ['first_name', 'last_name']
        permissions = [
            ("can_edit_grades", "Puede ver sus calificaciones"),
            ("can_edit_profile", "Puede editar su perfil"),
            ("can_view_profile", "Puede ver su perfil"),
            ("can_view_grades", "Puede ver las calificaciones de los estudiantes"),
        ]
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.specialization}"

class Curso(models.Model):
    name = models.CharField(max_length=50, default="unknow")
    description = models.TextField(default="Vacio")
    teacher = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural= 'Cursos'
        verbose_name = 'Curso'
        ordering = ['name']
    def __str__(self):
        return self.name

class Matricula(models.Model):
    student = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)
    enrollment_date = models.DateField(default='2024-07-01')
    class Meta:
        verbose_name_plural = 'Matriculas'
        verbose_name = 'Matricula'
        ordering = ['student', 'course']
    def __str__(self):
        return f"{self.student} enrolled in {self.course} on {self.enrollment_date}"

class Asignatura(models.Model):
    name = models.CharField(max_length=100, default="unknow")
    course = models.ForeignKey(Curso, related_name='subjects', on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name_plural = 'Asignaturas'
        verbose_name = 'Asignatura'
        ordering = ['name']
    def __str__(self):
        return self.name

class Grade(models.Model):
    student = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='grades', default=None, null=True, blank=True)
    subject = models.CharField(max_length=100, verbose_name="Asignatura", default='asignatura')
    grade = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Calificación", default=0)
    date_recorded = models.DateField(verbose_name="Fecha de Registro", default='2024-07-01')
    class Meta:
        verbose_name = 'Calificación'
        verbose_name_plural = 'Calificaciones'
    def __str__(self):
        return f"{self.student} - {self.subject}: {self.grade}"