from django.urls import path
from . import views


urlpatterns = [
    path("acerca/", views.acerca, name="acerca"),
    path("contacto/", views.contacto, name="contacto"),
    path("", views.inicio, name="inicio"),
    path("sesion_iniciada/", views.detalles, name="sesion_iniciada"),
    path("sesion_iniciada/evaluacion/", views.evaluacion, name="evaluacion"),
    path("sesion_iniciada/materia/", views.materia, name="materia"),
    path("sesion_iniciada/matricula/", views.matricula, name="matricula"),
    path("iniciar_sesion/", views.iniciar_sesion, name="signin"),
    path("cerrar_sesion/", views.cerrar_sesion, name="cerrar_sesion"),
]
