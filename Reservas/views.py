from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import ReservaSerializer
from .models import Reserva
# Create your views here.

class ReservaViewSet(viewsets.ModelViewSet):
    serializer_class = ReservaSerializer
    queryset = Reserva.objects.all()
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]