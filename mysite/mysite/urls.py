from django.contrib import admin
from django.urls import include, path
from gestion.views import *

urlpatterns = [
    path('', include('gestion.urls')),
    path('admin/', admin.site.urls),
    path('formContact/', formContact, name='formContact'),
    path('contactar/', contactar, name='contactar'),

]
