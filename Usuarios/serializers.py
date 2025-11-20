from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

Usuario = get_user_model()
class RegistroUsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password','telefono', 'pais']
        read_only_fields = ['id', 'password']
    
    def create(self, validated_data):
        usuario = Usuario.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            telefono=validated_data['telefono'],
            pais=validated_data['pais']
        )
        rol = Group.objects.get(name='cliente')
        usuario.groups.add(rol)
        return usuario
    
class RegistroUsuarioRecepcionSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password','telefono', 'pais']
        read_only_fields = ['id', 'password']
    
    def create(self, validated_data):
        usuario = Usuario.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            telefono=validated_data['telefono'],
            pais=validated_data['pais']
        )
        rol = Group.objects.get(name='recepcion')
        usuario.groups.add(rol)
        return usuario