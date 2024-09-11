from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Usuario, Matricula, Materia, matricula_materia, tipo_evaluacion, Metodologia, Evaluacion
from django.core.mail import send_mail

# Create your views here.
def index(request):
	return render(request, 'index.html', {'message': 'Bienvenido a Index'})

def home(request):
	return render(request, 'home.html')

def form_contact(request):
	return render(request, 'form_contact.html')

def contact(request):
	return render(request, "contacto_exitoso.html")