from django.contrib import admin
from django.urls import include, path
from gestion.views import form_contact, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestion.urls'))
]
