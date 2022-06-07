from django.db import models

class Mensaje(models.Model):
    emisor = models.CharField(max_length=200)
    mensaje = models.CharField(max_length=1000)
    receptor = models.CharField(max_length=200)

    def __str__(self):
        return self.mensaje+" "+self.emisor