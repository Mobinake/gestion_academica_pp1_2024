from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("about/", views.about_view, name="about"),
    path("contact/", views.contact_view, name="contact"),
    path("eliminar_materia/<id_materia>", views.eliminar_materia_view, name="eliminar_materia"),
    path("edicion_materia/<id_materia>", views.edicion_materia_view, name="edicion_materia"),
    path("editar_materia/", views.editar_materia_view, name="editar_materia"),
    path("evaluacion/", views.evaluacion_view, name="evaluacion"),
    path("home/", views.home_view, name="home"),
    path("logged/", views.logged_view, name="logged"),
    path("logout/", views.signout_view, name="logout"),
    path("materia/", views.materia_view, name="materia"),
    path("matricula/", views.matricula_view, name="matricula"),
    path("registrar_materia/", views.registar_materia_view, name="registrar_materia"),
    path("registrar_tipo_evaluacion/", views.registrar_tipo_evaluacion_view, name="registrar_tipo_evaluacion"),
    path("signin", views.signin_view, name="signin"),
    path("signup/", views.signup_view, name="signup"),
    path("tipo_evaluacion/", views.tipo_evaluacion_view, name="tipo_evaluacion"),
]
