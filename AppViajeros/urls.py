from django.urls import path
from .views import *

urlpatterns = [
   
    path('postAmerica/',postAmerica, name='postAmerica'),
    path('leerPosteos/', leerPosteos, name='leerPosteos'),
    path('eliminarPosteos/<titulo>', eliminarPosteos, name='eliminarPosteos'),
    path('editarPosteos/<titulo>', editarPosteos, name='editarPosteos'),
    
    path('europa', europa, name='europa'),
    path('europa/list/', PosteosList.as_view(), name='europa_listar'),
    path('posteo/<pk>', PosteoDetalle.as_view(), name='europa_detalle'),
    path('posteo/nuevo/', PosteoCreacion.as_view(), name='europa_crear'),
    path('posteo/editar/<pk>', PosteoEdicion.as_view(), name='europa_editar'),
    path('europa/borrar/<pk>', PosteoEliminacion.as_view(), name='europa_borrar'),
    path('login', login_request, name='login'),


]
