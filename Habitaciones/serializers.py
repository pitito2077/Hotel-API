from rest_framework import serializers
from .models import Habitacion

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = ['id','numero_habitacion', 'tipo', 'precio_por_noche', 'foto', 'disponible']
        read_only_fields = ['id', 'numero_habitacion', 'tipo', 'precio_por_noche', 'foto']
    
    