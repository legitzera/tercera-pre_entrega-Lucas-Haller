from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    camada = models.CharField(max_length=100)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)

class Camada(models.Model):
    nombre = models.CharField(max_length=100)