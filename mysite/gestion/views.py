from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from gestion.models import Materia

import datetime

# Create your views here.
def access_view(request):
	return render(request, "public/access.html")

def register_view(request):
	return render(request, "public/register.html")

def home_view(request):
	return render(request, "public/home.html")

def about_view(request):
	return render(request, "public/about.html")

def contact_view(request):
	return render(request, "public/contact.html")

#Estudiante
def materia_view(request):
	materias = Materia.objects.all()
	return render(request, "materia.html", {"materias": materias})

def registar_materia_view(request):
	nombre = request.POST["txt_nombre"]
	materia = Materia.objects.create(nombre_materia=nombre)
	return redirect("/materia")

def eliminar_materia_view(request, id_materia):
	materia = Materia.objects.get(id_materia=id_materia)
	materia.delete()
	return redirect("/materia")

def edicion_materia_view(request, id_materia):
	materia = Materia.objects.get(id_materia=id_materia)
	return render(request, "edicion_materia.html", {"materia": materia})

def editar_materia_view(request):
	id_materia = request.POST["txt_id"]
	nombre_materia = request.POST["txt_nombre"]

	materia = Materia.objects.get(id_materia=id_materia)
	materia.id_materia = id_materia
	materia.nombre_materia = nombre_materia
	materia.save()
	return redirect("/materia")
