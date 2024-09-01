from django.contrib import admin
from django.urls import include, path
from gestion.views import form_contact, contact

urlpatterns = [
    path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('form_contact/', form_contact, name='formContact'),
    path('contact/', contact, name='contactar'),

]
