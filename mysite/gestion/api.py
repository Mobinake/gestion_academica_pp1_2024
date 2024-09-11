from .models import Materia
from rest_framework import viewsets, permissions
from .serializers import GestionSerializer

#aqui creamos el viewsets
class GestionViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GestionSerializer
