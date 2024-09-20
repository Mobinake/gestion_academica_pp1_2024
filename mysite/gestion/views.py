from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from gestion.models import Materia

import datetime

# Create your views here.
def access_view(request):


	return render(request, "access.html")

def home_view(request):


	return render(request, "home.html")

def about_view(request):

	return render(request, "about.html")

def contact_view(request):

	return render(request, "contact.html")

def materia_view(request):
	materia = Materia.objects.create(nombre_materia=request.POST['materia'])
	materia.save()
	
	return render(request, "materia.html")

#TODO: modificar vista de la pagina, para ver primero la ventana de acceso
