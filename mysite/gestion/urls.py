from django.urls import path
from . import views


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("acerca/", views.acerca, name="acerca"),
    path("cerrar_sesion/", views.cerrar_sesion, name="cerrar_sesion"),
    path("contacto/", views.contacto, name="contacto"),
    path("iniciar_sesion/", views.iniciar_sesion, name="signin"),
    path("sesion_iniciada/", views.detalles, name="sesion_iniciada"),
    path("sesion_iniciada/evaluacion/", views.evaluacion, name="evaluacion"),
    path("sesion_iniciada/materia/", views.materia, name="materia"),
    path("sesion_iniciada/matricula/", views.matricula, name="matricula"),
    path("noticias/", views.noticia, name="noticia"),
    path("noticia/crear/", views.noticia_crear, name="noticia_crear"),
    path("noticia/detalles/<int:id_noticia>/", views.noticia_detalles, name="noticia_detalles"),
]
