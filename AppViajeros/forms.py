from socket import fromshare
from django import forms

class formularioPost(forms.Form):
    titulo = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=30)
    cuerpo = forms.CharField(max_length=500)
    autor = forms.CharField(max_length=50)
    fecha = forms.CharField(max_length=30)

