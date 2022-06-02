from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class formularioPost(forms.Form):
    titulo = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=30)
    cuerpo = forms.CharField(max_length=500)
    autor = forms.CharField(max_length=50)
    fecha = forms.CharField(max_length=30)

class formularioRegistroUser(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {k:" " for k in fields}

