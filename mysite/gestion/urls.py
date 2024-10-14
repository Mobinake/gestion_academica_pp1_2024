from django.urls import path
from django.contrib import admin
from django.contrib.auth import authenticate, login, logout
from . import views

urlpatterns = [
    path("about/", views.about_view, name="about"),
    path("contact/", views.contact_view, name="contact"),
    path("eliminar_materia/<id_materia>", views.eliminar_materia_view, name="eliminar_materia"),
    path("edicion_materia/<id_materia>", views.edicion_materia_view, name="edicion_materia"),
    path("materia/editar/", views.materia_editar_view, name="editar_materia"),
    path("evaluacion/", views.evaluacion_view, name="evaluacion"),
    path("home/", views.home_view, name="home"),
    path("logged/", views.logged_view, name="logged"),
    path("materia/", views.materia_view, name="materia"),
    path("matricula/", views.matricula_view, name="matricula"),
    path("metodologia/", views.metodologia_view, name="metodologia"),
    path("registrar_materia/", views.registar_materia_view, name="registrar_materia"),
    path("registrar_metodologia/", views.registar_metodologia_view, name="registrar_metodologia"),
    path("registrar_tipo_evaluacion/", views.registrar_tipo_evaluacion_view, name="registrar_tipo_evaluacion"),
    path("signin", views.signin_view, name="signin"),
    path("signup/", views.signup_view, name="signup"),
    path("signout/", views.signout_view, name="signout"),
    path("tipo_evaluacion/", views.tipo_evaluacion_view, name="tipo_evaluacion"),
]
