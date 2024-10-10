from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from gestion.models import Materia, Usuario, Evaluacion, Matricula, tipo_evaluacion, Metodologia
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import datetime


# Create your views here.

def about_view(request):
    return render(request, "public/about.html")


def contact_view(request):
    return render(request, "public/contact.html")


def home_view(request):
    return render(request, "public/home.html")


def edicion_materia_view(request, id_materia):
    materia = Materia.objects.get(id_materia=id_materia)
    return render(request, "logged/edicion_materia.html", {"materia": materia})


def editar_materia_view(request):
    id_materia = request.POST["txt_id"]
    nombre_materia = request.POST["txt_nombre"]

    materia = Materia.objects.get(id_materia=id_materia)
    materia.id_materia = id_materia
    materia.nombre_materia = nombre_materia
    materia.save()
    return redirect("/materia")


def eliminar_materia_view(request, id_materia):
    materia = Materia.objects.get(id_materia=id_materia)
    materia.delete()
    return redirect("/materia")


def evaluacion_view(request):
    evaluacion = Evaluacion.objects.all()
    return render(request, "logged/evaluacion.html", {"evaluacion": evaluacion})


def logged_view(request):
    return render(request, "logged/logged.html")


def materia_view(request):
    materias = Materia.objects.all()
    return render(request, "logged/materia.html", {"materias": materias})


def matricula_view(request):
    matricula = Matricula.objects.all()
    return render(request, "logged/matricula.html", {"matricula": matricula})

def metodologia_view(request):
    metodologia = Metodologia.objects.all()
    return render(request, "logged/metodologia.html", {"metodologia": metodologia})


def registar_materia_view(request):
    nombre = request.POST["txt_nombre"]
    materia = Materia.objects.create(nombre_materia=nombre)
    return redirect("/materia")

def registar_metodologia_view(request):
    nombre = request.POST["txt_nombre"]
    metodologia = Metodologia.objects.create(nombre_materia=nombre)
    return redirect("/metodologia")


def registrar_tipo_evaluacion_view(request):
    nombre = request.POST["txt_nombre"]
    tipo = tipo_evaluacion.objects.create(nombre_tipo_evaluacion=nombre)
    return redirect("/tipo_evaluacion")

def signup_view(request):
    if request.method == "GET":
        return render(request, "public/signup.html", {
            "form": UserCreationForm()
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = Usuario.objects.create_user(username=request.POST["username"],
                                                   password=request.POST["password1"])
                user.save()
                #
                login(request, user)
                # este es el usuario con sesion iniciada
                # request.user
                return redirect("logged/logged")
            except:
                return render(request, "public/signup.html", {
                    "form": UserCreationForm(),
                    "error": "Usuario ya registrado"
                })
        else:
            return render(request, "public/signup.html", {
                "form": UserCreationForm(),
                "error": "Contraseñas no coinciden"
            })


def signout_view(request):
    logout(request)
    return redirect("public/signup")


def signin_view(request):
    if request.method == "GET":
        return render(request, "public/signin.html", {
            "form": AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "public/signin.html", {
                "form": AuthenticationForm(),
                "error": "Usuario o contraseña incorrectos"
            })
        else:
            login(request, user)
            return redirect("logged/")


def tipo_evaluacion_view(request):
    tipo = tipo_evaluacion.objects.all()
    return render(request, "logged/tipo_evaluacion.html", {"tipo_evaluacion": tipo})
