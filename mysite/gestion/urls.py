from django.urls import path
from . import views
from rest_framework import routers
from .api import GestionViewSet
router = routers.DefaultRouter()

router.register('api/gestion', GestionViewSet, 'gestion')

app_name = 'gestion'
urlpatterns = router.urls
