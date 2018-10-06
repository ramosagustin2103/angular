from django.db import models

# Create your models here

class Auto(models.Model):
    nombre = models.CharField(max_length=20, blank=True)
    descripcion = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return self.nombre


class Perro(models.Model):
    nombre = models.CharField(max_length=20, blank=True)
    descripcion = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return self.nombre