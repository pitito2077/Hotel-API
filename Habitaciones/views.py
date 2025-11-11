from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import HabitacionSerializer
from .models import Habitacion
# Create your views here.

class HabitacionViewSet(viewsets.ModelViewSet):
    serializer_class = HabitacionSerializer
    queryset = Habitacion.objects.all()
    #cambiar despues que chambee el pendejo.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    http_method_names = ['get']