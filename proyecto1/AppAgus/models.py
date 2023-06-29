from django.db import models

# Create your models here.

class Clase(models.Model):
    deporte = models.CharField(max_length=30)
    turno = models.CharField(max_length=30)

class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Coach(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    deporte = models.CharField(max_length=30)


