from django.db import models

class America(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=30)
    cuerpo = models.CharField(max_length=500)
    autor = models.CharField(max_length=50)
    fecha = models.CharField(max_length=30)

    def __str__(self):
        return self.titulo+" - "+self.autor

class Europa(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=30)
    cuerpo = models.CharField(max_length=500)
    autor = models.CharField(max_length=50)
    fecha = models.CharField(max_length=30)
    
    def __str__(self):
        return self.titulo+" - "+self.autor

class Africa(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=30)
    cuerpo = models.CharField(max_length=500)
    autor = models.CharField(max_length=50)
    fecha = models.CharField(max_length=30)

class Asia(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=30)
    cuerpo = models.CharField(max_length=500)
    autor = models.CharField(max_length=50)
    fecha = models.CharField(max_length=30)

class Oceania(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=30)
    cuerpo = models.CharField(max_length=500)
    autor = models.CharField(max_length=50)
    fecha = models.CharField(max_length=30)