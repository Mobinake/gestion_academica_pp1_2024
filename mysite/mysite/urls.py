"""
"""
from django.contrib import admin
from django.urls import include, path
import gestion.views as gestion_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion/', include('gestion.urls')),
    path('formContact/', gestion_views.formContact, name='formContact'),
    path('contactar/', gestion_views.contactar, name='contactar'),

]
