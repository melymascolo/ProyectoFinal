from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('', home, name='home'),
    path('about', aboutMe, name='about'),

    path('america/pages', PosteosListAm.as_view(), name='america'),
    path('america/pages/<pk>', PosteoDetalleAm.as_view(), name='america_detalle'),
    path('america/nuevo/', PosteoCreacionAm.as_view(), name='america_crear'),
    path('america/editar/<pk>', PosteoEdicionAm.as_view(), name='america_editar'),
    path('america/borrar/<pk>', PosteoEliminacionAm.as_view(), name='america_borrar'),
    
    path('europa/pages', PosteosListEu.as_view(), name='europa'),
    path('europa/pages/<pk>', PosteoDetalleEu.as_view(), name='europa_detalle'),
    path('europa/nuevo/', PosteoCreacionEu.as_view(), name='europa_crear'),
    path('europa/editar/<pk>', PosteoEdicionEu.as_view(), name='europa_editar'),
    path('europa/borrar/<pk>', PosteoEliminacionEu.as_view(), name='europa_borrar'),

    path('africa/pages', PosteosListAf.as_view(), name='africa'),
    path('africa/pages/<pk>', PosteoDetalleAf.as_view(), name='africa_detalle'),
    path('africa/nuevo/', PosteoCreacionAf.as_view(), name='africa_crear'),
    path('africa/editar/<pk>', PosteoEdicionAf.as_view(), name='africa_editar'),
    path('africa/borrar/<pk>', PosteoEliminacionAf.as_view(), name='africa_borrar'),

    path('asia/pages', PosteosListAs.as_view(), name='asia'),
    path('asia/pages/<pk>', PosteoDetalleAs.as_view(), name='asia_detalle'),
    path('asia/nuevo/', PosteoCreacionAs.as_view(), name='asia_crear'),
    path('asia/editar/<pk>', PosteoEdicionAs.as_view(), name='asia_editar'),
    path('asia/borrar/<pk>', PosteoEliminacionAs.as_view(), name='asia_borrar'),

    path('oceania/pages', PosteosListOc.as_view(), name='oceania'),
    path('oceania/pages/<pk>', PosteoDetalleOc.as_view(), name='oceania_detalle'),
    path('oceania/nuevo/', PosteoCreacionOc.as_view(), name='oceania_crear'),
    path('oceania/editar/<pk>', PosteoEdicionOc.as_view(), name='oceania_editar'),
    path('oceania/borrar/<pk>', PosteoEliminacionOc.as_view(), name='oceania_borrar'),
    
    
    path('accounts/login', login_request, name='login'),
    path('accounts/signup', register, name='register'),
    path('accounts/logout', LogoutView.as_view(template_name='AppViajeros/logout.html'), name='logout'),
    path('accounts/profile', mostrarPerfil, name='perfil'),
    path('editarPerfil', editarPerfil, name='editarPerfil'),
    path('agregarAvatar', agregarAvatar, name='agregarAvatar'),



]
