from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Teacher, Student, AcademicPeriod, Grades, Registration, Carrer, Course, Subject, Person, User

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Registration)
admin.site.register(Subject)
admin.site.register(Grades)
admin.site.register(Person)
admin.site.register(AcademicPeriod)
admin.site.register(Carrer)
admin.site.register(User)

admin.site.site_header = "Panel de Administracion"
admin.site.site_title = "Gestión Académica"
admin.site.index_title = "Gestion Academica"