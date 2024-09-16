from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path("home/", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
    path("contact/", views.contact_view, name="contact"),

]