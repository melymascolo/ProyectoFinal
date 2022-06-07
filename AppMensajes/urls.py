from django.urls import path
from .views import *


urlpatterns = [
   
    path('', inicio, name='portada'),
    path('nuevo', crearMensaje.as_view(), name='nuevo'),
    path('misMensajes', MensajeList.as_view(), name='misMensajes'),
    path('enviado', enviado, name='enviado'),



]