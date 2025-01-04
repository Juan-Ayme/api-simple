from django.db import models

# Create your models here.

class Productor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    DNI = models.CharField(max_length=8)
    email = models.EmailField()
    telefono = models.CharField(max_length=9)
    fecha_registro = models.DateField(auto_now_add=True)
    estado = models.BooleanField(default=True)
