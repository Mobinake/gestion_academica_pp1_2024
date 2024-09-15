from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
	return render(request, 'index.html', {'message': 'Bienvenido a Index'})

def home(request):
	#template = loader.get_template('home.html')
	return render(request, 'home.html')

def form_contact(request):
	request.POST['USERNAME']
	return render(request, 'form_contact.html', {'titulo': 'contact'})

def contact(request):
	return render(request, "contacto_exitoso.html")