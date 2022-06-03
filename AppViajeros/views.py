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
    avatar = Avatar.objects.filter(user=request.user)
    return render(request, 'AppViajeros/home.html', {'url': avatar[0].avatar.url})


def postAmerica(request):
    
    if request.method == "POST":
        formulario=formularioPost(request.POST)
        if formulario.is_valid():
            datos=formulario.cleaned_data
            post=America(titulo=datos['titulo'], subtitulo=datos['subtitulo'], cuerpo=datos['cuerpo'], autor=datos['autor'], fecha=datos['fecha'])
            post.save()
            return render (request, 'AppViajeros/inicio.html')
    else:
        formulario=formularioPost()
        return render (request, 'AppViajeros/america.html', {'formulario':formulario})


def leerPosteos(request):
    posteo = America.objects.all()
    return render (request, 'AppViajeros/america.html', {'posteo':posteo})

def eliminarPosteos(request, titulo):
    posteo = America.objects.get(titulo=titulo)
    posteo.delete()
    listado = leerPosteos(request)
    return listado

def editarPosteos(request, titulo):
    posteo = America.objects.get(titulo=titulo)
    if request.method == 'POST':
        formulario= formularioPost(request.POST)
        if formulario.is_valid():
            datos=formulario.cleaned_data
            posteo.titulo=datos['titulo']
            posteo.subtitulo=datos['subtitulo']
            posteo.cuerpo=datos['cuerpo']
            posteo.autor=datos['autor']
            posteo.fecha=datos['fecha']
            listado = leerPosteos(request)
            return listado
    else:
        formulario=formularioPost(initial={'titulo':posteo.titulo, 'subtitulo':posteo.subtitulo, 'cuerpo':posteo.cuerpo, 'autor':posteo.autor, 'fecha':posteo.fecha})
    return render(request, 'AppViajeros/editarPosteos.html', {'formulario':formulario, 'titulo':titulo})


#--------------------------EUROPA----------------------------
def europa(request):
    return render(request, 'AppViajeros/europa.html')

class PosteosList(ListView):
    model = Europa
    template_name = 'AppViajeros/europa_list.hmtl'


class PosteoDetalle(DetailView):
    model = Europa
    template_name = 'AppViajeros/europa_detalle.html'

class PosteoCreacion(CreateView):
    model = Europa
    success_url = reverse_lazy('europa_listar')
    fields=['titulo','subtitulo','cuerpo','autor','fecha']

class PosteoEdicion(UpdateView):
    model = Europa
    success_url = reverse_lazy('europa_listar')
    fields=['titulo','subtitulo','cuerpo','autor','fecha']

class PosteoEliminacion(DeleteView):
    model = Europa
    success_url = reverse_lazy('europa_listar')
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
            return render(request, 'AppViajeros/home.html', {'mensaje': 'No se pudo crear el usuario'})
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

            return render(request, 'AppViajeros/home.html', {'usuario': usuario, 'mensaje': 'Perfil editado con exito'})
    else:
        formulario = UserEditForm(instance=usuario)
    return render(request, 'AppViajeros/editarPerfil.html', {'formulario': formulario, 'usuario':usuario.username})

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






