from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('ci', 'first_name', 'last_name', 'birth_date')
    search_fields = ['first_name', 'last_name']
@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('id_career', 'name_career', 'faculty')
    search_fields = ['name_career', 'faculty']
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'ci', 'name_user', 'email', 'type')
    list_filter = ['user_type']
    search_fields = ['email', 'user', 'ci']
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id_student', 'ci', 'id_career', 'status', 'assistance', 'behaviour')
    list_filter = ['status', 'id_career']
    search_fields = ['ci', 'last_name', 'first_name']
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id_teacher', 'ci', 'id_subject')
    search_fields = ['ci', 'id_teacher', 'id_subject']
@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('id_period', 'name_period', 'year_period', 'semester_period')
    list_filter = ['year_period', 'semester_period']
    search_fields = ['name_period', 'id_period']
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id_subject', 'name_subject', 'id_period')
    list_filter = ['id_period', 'id_subject']
    search_fields = ['id_teacher', 'id_course']
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id_schedule', 'id_subject')
    list_filter = ['id_schedule', 'id_subject']
    search_fields = ['id_shedule', 'id_subject']
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id_course', 'course_name', 'id_career')
    list_filter = ['id_career']
    search_fields = ['course_name', 'course_description']
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id_registration', 'id_student', 'id_subject', 'registration_date', 'account_state')
    list_filter = ['id_registration', 'id_student', 'id_subject']
    search_fields = ['id_student', 'id_subject']
@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    list_display = ('id_student', 'id_course', 'id_subject', 'note', 'evaluation_date')
    list_filter = ['evaluation_date', 'id_course']
    search_fields = ['id_student__id_person__first_name', 'id_student__id_person__last_name', 'note']


admin.site.site_header = "Panel de Administracion"
admin.site.site_title = "Gestión Académica"
admin.site.index_title = "Gestion Académica"
