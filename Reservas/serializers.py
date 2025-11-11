from rest_framework import serializers
from .models import Reserva
from django.db.models import Q

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'usuario', 'habitacion', 'fecha_creacion', 'fecha_inicio', 'fecha_fin']
        read_only_fields = ['id', 'fecha_creacion']
        
    def validate(self, data):
        habitacion = data['habitacion']
        inicio = data['fecha_inicio']
        fin = data['fecha_fin']
        
        if fin < inicio:
            raise serializers.ValidationError('Error eligiendo fechas')
        
        fechas_cruzadas = Reserva.objects.filter(Q(habitacion=habitacion) & Q(fecha_inicio__lt=fin) & Q(fecha_fin__gt=inicio))
        
        if fechas_cruzadas.exists():
            raise serializers.ValidationError('La habitacion no esta disponible en esas fechas.')
        
        return data
    
    def create(self, validated_data):
        reserva = Reserva.objects.create(**validated_data)
        habitacion = validated_data['habitacion']
        habitacion.disponible = False
        habitacion.save()
        return reserva