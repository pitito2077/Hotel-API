from rest_framework import serializers
from django.contrib.auth import get_user_model

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
        return usuario