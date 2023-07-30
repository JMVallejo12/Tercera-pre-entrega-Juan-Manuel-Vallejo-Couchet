from django.db import models

# Create your models here.

class Personaje(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nombrePersonaje = models.CharField(max_length=50)
    apellidoPersonaje = models.CharField(max_length=50)
 


class Temporada(models.Model):
    nombreTemporada = models.CharField(max_length=50)
    numeroCapitulos = models.IntegerField()
    fechaEmision = models.CharField(max_length=50)
    

class Suscriptor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    tarjeta = models.IntegerField()
    
