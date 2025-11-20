from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.db.models import Q
from Habitaciones.models import Habitacion
from django.dispatch import receiver

@receiver(post_migrate)
def crearRoles(sender, **kwargs):
    
    #! no mover💀
    if sender.name != 'Usuarios':
        return
    #TODO: checar las tareas en ms ToDo
    
    #? Grupo Recepcion
    reception_group, _ = Group.objects.get_or_create(name='recepcion')
    #? Grupo Cliente
    client_group,_ = Group.objects.get_or_create(name='cliente')
    
    ct = ContentType.objects.get_for_model(Habitacion)
    #? Permisos para recepcion
    reception_permissions = Permission.objects.filter(
        Q(codename__in=['view_habitacion', 'change_habitacion','add_habitacion', 'delete_habitacion']) &
        Q(content_type=ct)
    )
    #? Permisos para los clientes
    client_permissions = Permission.objects.filter(
        Q(content_type=ct) &
        Q(codename__in=['view_habitacion', 'change_habitacion'])
    )
    reception_group.permissions.set(reception_permissions)
    client_group.permissions.set(client_permissions)
    