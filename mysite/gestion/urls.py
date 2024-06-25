from django.urls import path
from .views import student_create, student_update, grade_create, grade_update
from . import views

app_name = 'gestion'
urlpatterns = [
	path('', views.index, name='index'),
	path('student/new/', student_create, name='student_create'),
	path('student/<int:pk>/edit/', student_update, name='student_update'),
	path('grade/new/', grade_create, name='grade_create'),
	path('grade/<int:pk>/edit/', grade_update, name='grade_update'),
]
