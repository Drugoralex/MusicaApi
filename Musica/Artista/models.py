from django.db import models

# Create your models here.

class Artista(models.Model):
    Nombre_Real = models.CharField(max_length=200)
    Nombre_Artistico = models.CharField(max_length=200)
    Edad = models.IntegerField()
    Pais_Origen = models.CharField(max_length=200)
    Nacionalidad = models.CharField(max_length=200)
    Inicio_Actividad = models.IntegerField()

    def __str__(self):
        return self.Nombre_Artistico