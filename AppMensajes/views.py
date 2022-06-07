from django.shortcuts import render
from .models import Mensaje
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView


def inicio(request):
    return render(request, 'AppMensajes/inicio.html')

class crearMensaje(CreateView):
    model = Mensaje
    success_url = reverse_lazy('nuevo')
    fields=['emisor','mensaje','receptor']

class MensajeList(ListView):
    model = Mensaje
    template_name = 'AppMensajeria/mensaje_list.hmtl'