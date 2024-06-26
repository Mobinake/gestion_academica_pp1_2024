from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Student, Teacher, Subject, Course, Carrer, AcademicPeriod, Grades, Registration, Person, User

# Create your views here.
def index(request):
	return render(request, 'index.html', {'message': 'Hello, world!'})
