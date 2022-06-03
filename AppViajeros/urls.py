from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('home', home, name='home'),
    path('postAmerica/',postAmerica, name='postAmerica'),
    path('leerPosteos/', leerPosteos, name='leerPosteos'),
    path('eliminarPosteos/<titulo>', eliminarPosteos, name='eliminarPosteos'),
    path('editarPosteos/<titulo>', editarPosteos, name='editarPosteos'),
    
    
    path('europa/pages', PosteosList.as_view(), name='europa'),
    path('pages/<pk>', PosteoDetalle.as_view(), name='europa_detalle'),
    path('europa/nuevo/', PosteoCreacion.as_view(), name='europa_crear'),
    path('europa/editar/<pk>', PosteoEdicion.as_view(), name='europa_editar'),
    path('europa/borrar/<pk>', PosteoEliminacion.as_view(), name='europa_borrar'),
    
    path('accounts/login', login_request, name='login'),
    path('accounts/signup', register, name='register'),
    path('accounts/logout', LogoutView.as_view(template_name='AppViajeros/logout.html'), name='logout'),
    path('editarPerfil', editarPerfil, name='editarPerfil'),
    path('agregarAvatar', agregarAvatar, name='agregarAvatar'),


]
