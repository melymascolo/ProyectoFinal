from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class America(models.Model):
    titulo = models.CharField(max_length=300)
    subtitulo = models.CharField(max_length=300)
    lugar = models.CharField(max_length=300)
    experiencia = RichTextField()
    autor = models.CharField(max_length=300)
    fecha = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)

    def __str__(self):
        return self.lugar+" - "+self.titulo

class Asia(models.Model):
    titulo = models.CharField(max_length=300)
    subtitulo = models.CharField(max_length=300)
    lugar = models.CharField(max_length=300)
    experiencia = RichTextField()
    autor = models.CharField(max_length=300)
    fecha = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)

    def __str__(self):
        return self.lugar+" - "+self.titulo

class Africa(models.Model):
    titulo = models.CharField(max_length=300)
    subtitulo = models.CharField(max_length=300)
    lugar = models.CharField(max_length=300)
    experiencia = RichTextField()
    autor = models.CharField(max_length=300)
    fecha = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    
    def __str__(self):
        return self.lugar+" - "+self.titulo


class Europa(models.Model):
    titulo = models.CharField(max_length=300)
    subtitulo = models.CharField(max_length=300)
    lugar = models.CharField(max_length=300)
    experiencia = RichTextField()
    autor = models.CharField(max_length=300)
    fecha = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)

    def __str__(self):
        return self.lugar+" - "+self.titulo

class Oceania(models.Model):
    titulo = models.CharField(max_length=300)
    subtitulo = models.CharField(max_length=300)
    lugar = models.CharField(max_length=300)
    experiencia = RichTextField()
    autor = models.CharField(max_length=300)
    fecha = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)

    def __str__(self):
        return self.lugar+" - "+self.titulo

class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)

