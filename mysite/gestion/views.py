from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
	return render(request, 'index.html', {'message': 'Bienvenido a Index'})

def home():
	template = loader.get_template('home.html')
	return HttpResponse(template.render())

def form_contact(request):
	return render(request, 'form_contact.html')

def contact(request):
	return render(request, "contacto_exitoso.html")