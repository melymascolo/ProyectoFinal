from msilib.schema import ListView
from urllib import request
from django.shortcuts import render

from .models import *
from django.http import HttpResponse
from AppViajeros.forms import formularioPost, formularioRegistroUser, UserEditForm, AvatarForm
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def home(request):
    return render (request, 'AppViajeros/home.html')

def inicio(request):
    avatar = Avatar.objects.filter(user=request.user)
    return render(request, 'AppViajeros/inicio.html', {'url': avatar[0].avatar.url})

def aboutMe(request):
    return render(request, 'AppViajeros/aboutMe.html')  

def america(request):
    return render(request, 'AppViajeros/america.html')

class PosteosListAm(ListView):
    model = America
    template_name = 'AppViajeros/america_list.hmtl'


class PosteoDetalleAm(DetailView):
    model = America
    template_name = 'AppViajeros/america_detalle.html'

class PosteoCreacionAm(CreateView):
    model = America
    success_url = reverse_lazy('america')
    fields=['titulo','subtitulo','cuerpo','autor','fecha']

class PosteoEdicionAm(UpdateView):
    model = America
    success_url = reverse_lazy('america')
    fields=['titulo','subtitulo','cuerpo','autor','fecha']

class PosteoEliminacionAm(DeleteView):
    model = America
    success_url = reverse_lazy('america')
    fields=['titulo','subtitulo','cuerpo','autor','fecha']



#--------------------------EUROPA----------------------------
def europa(request):
    return render(request, 'AppViajeros/europa.html')

class PosteosListEu(ListView):
    model = Europa
    template_name = 'AppViajeros/europa_list.hmtl'


class PosteoDetalleEu(DetailView):
    model = Europa
    template_name = 'AppViajeros/europa_detalle.html'

class PosteoCreacionEu(CreateView):
    model = Europa
    success_url = reverse_lazy('europa')
    fields=['titulo','subtitulo','cuerpo','autor','fecha']

class PosteoEdicionEu(UpdateView):
    model = Europa
    success_url = reverse_lazy('europa')
    fields=['titulo','subtitulo','cuerpo','autor','fecha']

class PosteoEliminacionEu(DeleteView):
    model = Europa
    success_url = reverse_lazy('europa')
    fields=['titulo','subtitulo','cuerpo','autor','fecha']

#---------------------AFRICA----------------------------
def africa(request):
    return render(request, 'AppViajeros/africa.html')

class PosteosListAf(ListView):
    model = Africa
    template_name = 'AppViajeros/africa_list.hmtl'


class PosteoDetalleAf(DetailView):
    model = Africa
    template_name = 'AppViajeros/africa_detalle.html'

class PosteoCreacionAf(CreateView):
    model = Africa
    success_url = reverse_lazy('africa')
    fields=['titulo','subtitulo','cuerpo','autor','fecha']

class PosteoEdicionAf(UpdateView):
    model = Africa
    success_url = reverse_lazy('africa')
    fields=['titulo','subtitulo','cuerpo','autor','fecha']

class PosteoEliminacionAf(DeleteView):
    model = Africa
    success_url = reverse_lazy('africa')
    fields=['titulo','subtitulo','cuerpo','autor','fecha']

#-----------------------------------ASIA---------------------------------------
def asia(request):
    return render(request, 'AppViajeros/asia.html')

class PosteosListAs(ListView):
    model = Asia
    template_name = 'AppViajeros/asia_list.hmtl'


class PosteoDetalleAs(DetailView):
    model = Asia
    template_name = 'AppViajeros/asia_detalle.html'

class PosteoCreacionAs(CreateView):
    model = Asia
    success_url = reverse_lazy('asia')
    fields=['titulo','subtitulo','cuerpo','autor','fecha']

class PosteoEdicionAs(UpdateView):
    model = Asia
    success_url = reverse_lazy('asia')
    fields=['titulo','subtitulo','cuerpo','autor','fecha']

class PosteoEliminacionAs(DeleteView):
    model = Asia
    success_url = reverse_lazy('asia')
    fields=['titulo','subtitulo','cuerpo','autor','fecha']




#------------------
def login_request(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request=request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            clave = formulario.cleaned_data.get('password')

            user=authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request, 'AppViajeros/home.html', {'usuario':usuario, 'mensaje': 'Bienvenido'})
            else:
                return render(request, 'AppViajeros/login.html', {'formulario': formulario, 'mensaje': 'Usuario incorrecto, vuelva a intentarlo'})
        else:
            return render(request, 'AppViajeros/login.html', {'formulario': formulario, 'mensaje': 'Formulario invalido, vuelva a intentarlo'})
    else:
        formulario=AuthenticationForm()
        return render(request, 'AppViajeros/login.html', {'formulario':formulario})

def register(request):
    if request.method == 'POST':
        formulario = formularioRegistroUser(request.POST)
        if formulario.is_valid():
            username=formulario.cleaned_data['username']
            formulario.save()
            return render(request, 'AppViajeros/home.html', {'mensaje':f'El usuario {username} ha sido creado exitosamente'})
        else:
            return render(request, 'AppViajeros/home.html', {'mensaje':'No se pudo crear el usuario'})
    else:
        formulario = formularioRegistroUser()
        return render(request, 'AppViajeros/register.html', {'formulario': formulario})

@login_required
def editarPerfil(request):
    usuario=request.user

    if request.method == 'POST':
        formulario = UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']          
            usuario.save()

            return render(request, 'AppViajeros/inicio.html', {'usuario': usuario, 'mensaje': 'Perfil editado con exito'})
    else:
        formulario = UserEditForm(instance=usuario)
    return render(request, 'AppViajeros/editarPerfil.html', {'formulario': formulario, 'usuario':usuario.username})

def mostrarPerfil(request):
    usuario=request.user
    return render (request, 'AppViajeros/perfil_detalle.html', {'usuario':usuario})
    

@login_required
def agregarAvatar(request):
    user=User.objects.get(username=request.user)
    if request.method == 'POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            
            avatarViejo=Avatar.objects.get(user=request.user)
            if(avatarViejo.avatar):
                avatarViejo.delete()
            avatar = Avatar(user=user, avatar=formulario.cleaned_data['avatar'])
            avatar.save()
            return render (request, 'AppViajeros/home.html', {'usuario':user, 'mensaje':'Tu avatar fue agregado'})
    else:
        formulario=AvatarForm()
    return render(request, 'AppViajeros/agregarAvatar.html', {'formulario':formulario, 'usuario':user})