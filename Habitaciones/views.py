from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import HabitacionSerializer
from .models import Habitacion
# Create your views here.

class HabitacionViewSet(viewsets.ModelViewSet):
    serializer_class = HabitacionSerializer
    queryset = Habitacion.objects.all()
    #cambiar despues que chambee el pendejo.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    http_method_names = ['get']
    
class DetalleHabitacionView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, id):
        try:
            habitacion =Habitacion.objects.get(id=id)
        except Habitacion.DoesNotExist:
            return Response('La habitacion consultada no existe', status=status.HTTP_404_NOT_FOUND)
        serializer = HabitacionSerializer(habitacion)
        return Response(serializer.data)