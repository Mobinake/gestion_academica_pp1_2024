from django.urls import path
# from .views import student_create, student_update, grade_create, grade_update
from . import views

app_name = 'gestion'
urlpatterns = [
	path('', views.index, name='index'),
]
