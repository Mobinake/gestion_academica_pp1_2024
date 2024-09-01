from django.urls import path
from .views import home

app_name = 'gestion'
urlpatterns = [
	path('', home, name='home'),
	path('index/', home, name='index'),
]
