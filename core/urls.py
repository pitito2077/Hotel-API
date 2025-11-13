"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from Usuarios.views import index
from django.conf import settings
from rest_framework import routers
from django.urls import path, include
from django.conf.urls.static import static
from Reservas.views import ReservaViewSet
from Usuarios.views import RegistroUsuarioView
from Habitaciones.views import HabitacionViewSet,DetalleHabitacionView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

room_router = routers.DefaultRouter()
room_router.register(r'habitaciones', HabitacionViewSet, 'habitaciones')

booking_router = routers.DefaultRouter()
booking_router.register(r'reservas', ReservaViewSet, 'reservas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('api/register/', RegistroUsuarioView.as_view(), name='registro'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(room_router.urls), name='habitaciones'),
    path('api/habitaciones/habitacion/<int:id>/', DetalleHabitacionView.as_view(), name='detalle-habitacion'),
    path('api/', include(booking_router.urls), name='reservas'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)