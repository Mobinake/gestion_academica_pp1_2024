from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from gestion.models import Materia, Usuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import datetime


# Create your views here.
def signup_view(request):
    if request.method == "GET":
        return render(request, "public/signup.html", {
        "form":AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "public/signup.html", {
                "form": AuthenticationForm(),
                "error": "Usuario o contraseña incorrectos"
            })
        else:
            login(request, user)
            return redirect("/logged")


def logged_view(request):

    return render(request, "logged.html")

def signout_view(request):
    logout(request)
    return redirect("/signup")

def register_view(request):
    if request.method == "GET":
        return render(request, "public/register.html", {
            "form": UserCreationForm()
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = Usuario.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                user.save()
                return redirect("/logged")
            except:
                return render(request, "public/register.html", {
                    "form": UserCreationForm(),
                    "error": "Usuario ya registrado"
                })
        else:
            return render(request, "public/register.html", {
                "form": UserCreationForm(),
                "error": "Contraseñas no coinciden"
        })


def home_view(request):
    return render(request, "public/home.html")


def about_view(request):
    return render(request, "public/about.html")


def contact_view(request):
    return render(request, "public/contact.html")


# Estudiante
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
