from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("gestion/", include('gestion.urls')),
    path("admin/", admin.site.urls)
]
