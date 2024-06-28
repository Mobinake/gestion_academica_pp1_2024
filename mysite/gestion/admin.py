from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id_person', 'first_name', 'last_name', 'birth_date')
    search_fields = ['first_name', 'last_name']
@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('id_career', 'name_career', 'faculty')
    search_fields = ['name_career', 'faculty']
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'id_person', 'email', 'user_type')
    list_filter = ['user_type']
    search_fields = ['email', 'id_person__first_name', 'id_person__last_name']
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id_student', 'id_person', 'id_career', 'status')
    list_filter = ['status', 'id_career']
    search_fields = ['id_person__first_name', 'id_person__last_name']
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id_teacher', 'id_person', 'id_subject')
    search_fields = ['id_person__first_name', 'id_person__last_name', 'specialization']
@admin.register(AcademicPeriod)
class AcademicPeriodAdmin(admin.ModelAdmin):
    list_display = ('id_academicPeriod', 'name_academicPeriod', 'year_academicPeriod', 'semester_academicPeriod')
    list_filter = ['year_academicPeriod', 'semester_academicPeriod']
    search_fields = ['name_academicPeriod']
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id_subject', 'name_subject', 'id_academicPeriod')
    list_filter = ['id_academicPeriod']
    search_fields = ['id_teacher__id_person__first_name', 'id_teacher__id_person__last_name']
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id_course', 'course_name', 'id_career', 'id_subject')
    list_filter = ['id_career']
    search_fields = ['course_name', 'course_description']
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id_registration', 'id_student', 'id_subject', 'registration_date')
    list_filter = ['registration_date']
    search_fields = ['id_student__id_person__first_name', 'id_student__id_person__last_name']
@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    list_display = ('id_grades', 'id_student', 'id_curse', 'id_subject', 'note', 'evaluation_date')
    list_filter = ['evaluation_date', 'id_curse']
    search_fields = ['id_student__id_person__first_name', 'id_student__id_person__last_name', 'note']

admin.site.site_header = "Panel de Administracion"
admin.site.site_title = "Gestión Académica"
admin.site.index_title = "Gestion Academica"