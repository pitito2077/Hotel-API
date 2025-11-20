from .models import Habitacion
from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from .serializers import HabitacionSerializer
from rest_framework import viewsets, permissions
# Create your views here.

class HabitacionViewSet(viewsets.ModelViewSet):
    serializer_class = HabitacionSerializer
    queryset = Habitacion.objects.all()
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
    http_method_names = ['get']
    
class DetalleHabitacionView(RetrieveAPIView):
    serializer_class = HabitacionSerializer
    queryset = Habitacion.objects.all()
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
    lookup_field = 'id'