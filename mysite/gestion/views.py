from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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
