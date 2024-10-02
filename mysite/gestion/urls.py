from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path("home/", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
    path("contact/", views.contact_view, name="contact"),
    path("materia/", views.materia_view, name="materia"),
    path("registrar_materia/", views.registar_materia_view, name="registrar_materia"),
    path("eliminar_materia/<id_materia>", views.eliminar_materia_view, name="eliminar_materia"),
    path("edicion_materia/<id_materia>", views.edicion_materia_view, name="edicion_materia"),
    path("editar_materia/", views.editar_materia_view, name="editar_materia"),
    path("register", views.register_view, name="register"),
    path("signup/", views.signup_view, name="signup"),
    path("logged/", views.logged_view, name="logged"),
]