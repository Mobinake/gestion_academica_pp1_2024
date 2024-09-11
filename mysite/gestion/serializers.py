from rest_framework import serializers
from .models import Materia

#convertimos el modelo en datos consultables, creando el serializer
class GestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = ('id_materia', 'nombre_materia')
        #campos que no se podran editar
        #read_only_fields = ('id_materia',)
