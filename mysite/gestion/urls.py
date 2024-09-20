from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path("access/", views.access_view, name="access"),
    path("home/", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
    path("contact/", views.contact_view, name="contact"),
    path("materia/", views.materia_view, name="materia")
]