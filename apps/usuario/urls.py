from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'index'),
    path('listado/',Listado.as_view(), name= 'listado'),
    path('crear/',CrearUsuario.as_view(), name= 'crear'),
    path('editar/<int:pk>/',ActualizarUsuario.as_view(), name= 'editar'),
    path('eliminar/<int:pk>/',EliminarUsuario.as_view(), name= 'eliminar'),
]