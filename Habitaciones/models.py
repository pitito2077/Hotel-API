from django.db import models

# Create your models here.

class Habitacion(models.Model):
    HABITACION_CHOICES = (
        ('suite', 'Suite'),
        ('vista_al_mar', 'Vista Al Mar'),
        ('sencilla', 'Sencilla'),
        ('doble', 'Doble'),
    )
    numero_habitacion = models.CharField(max_length=3, unique=True)
    tipo = models.CharField(choices=HABITACION_CHOICES)
    precio_por_noche = models.PositiveIntegerField()
    foto = models.ImageField(upload_to='habitaciones/',null=True, blank=True)
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.numero_habitacion} tipo {self.tipo}'