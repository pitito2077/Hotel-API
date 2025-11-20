from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, permissions
from .serializers import RegistroUsuarioSerializer,RegistroUsuarioRecepcionSerializer
from django.contrib.auth import get_user_model
# Create your views here.
def index(request):
    return HttpResponse('<h1> Corriendo API <h1/>')

Usuario = get_user_model()
class RegistroUsuarioView(generics.CreateAPIView):
    serializer_class = RegistroUsuarioSerializer
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    
class RegistroUsuarioRecepcionView(generics.CreateAPIView):
    serializer_class = RegistroUsuarioRecepcionSerializer
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]