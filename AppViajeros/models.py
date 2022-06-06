from django.db import models
from django.contrib.auth.models import User 

class America(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    experiencia = models.CharField(max_length=600)
    autor = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    
    def __str__(self):
        return self.lugar+" - "+self.titulo

class Europa(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    experiencia = models.CharField(max_length=600)
    autor = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    
    def __str__(self):
        return self.lugar+" - "+self.titulo

class Asia(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    experiencia = models.CharField(max_length=600)
    autor = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    
    def __str__(self):
        return self.lugar+" - "+self.titulo

class Africa(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    experiencia = models.CharField(max_length=600)
    autor = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    
    def __str__(self):
        return self.lugar+" - "+self.titulo

class Oceania(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    experiencia = models.CharField(max_length=600)
    autor = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    
    def __str__(self):
        return self.lugar+" - "+self.titulo

class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)

    def __str__(self):
        return self.user