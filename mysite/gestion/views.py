from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from gestion.models import Materia, Usuario, Evaluacion, Matricula, tipo_evaluacion, Metodologia, Horario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def acerca(request):
    return render(request, "publico/acerca.html")

def contacto(request):
    return render(request, "publico/contacto.html")

def horario(request):
    return render(request, "sesion_iniciada/horario.html")

def inicio(request):
    return render(request, "publico/inicio.html")

@login_required
def materia_consultar(request, id_materia):
    materia = Materia.objects.get(id_materia=id_materia)
    return render(request, "sesion_iniciada/consultar_materia.html", {"materia": materia})

@login_required
def materia_horario(request, id_materia):
    horario = Horario.objects.filter(id_materia=id_materia)
    print(horario)
    return render(request, "sesion_iniciada/materia.html", {"horario": horario})

@login_required
def evaluacion(request):
    evaluacion = Evaluacion.objects.all()
    return render(request, "sesion_iniciada/evaluacion.html", {"evaluacion": evaluacion})


@login_required
def detalles(request):
    return render(request, "sesion_iniciada/sesion_iniciada.html")


@login_required
def materia(request):
    materias = Materia.objects.all().order_by("-anio")
    horario = Horario.objects.filter(id_materia=30)
    return render(request, "sesion_iniciada/materia.html", {"materias": materias, "horario": horario})


@login_required
def matricula(request):
    matricula = Matricula.objects.all()
    return render(request, "sesion_iniciada/matricula.html", {"matricula": matricula})


def cerrar_sesion(request):
    logout(request)
    return redirect("/iniciar_sesion")


def iniciar_sesion(request):
    if request.method == "GET":
        return render(request, "publico/iniciar_sesion.html", {
            "form": AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "publico/iniciar_sesion.html", {
                "form": AuthenticationForm(),
                "error": "Usuario o contraseña incorrectos"
            })
        else:
            login(request, user)
            return redirect("/sesion_iniciada")
