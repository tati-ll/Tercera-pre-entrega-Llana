from django.db import models

class Taller(models.Model):
    nombre = models.CharField(max_length=256)
    profesor = models.CharField(max_length=256)
    fecha = models.DateField(blank=False) 
    descripcion = models.TextField(blank=True)
    cupos = models.IntegerField(default=5)

    def __str__(self):
        return f"{self.nombre}, {self.fecha}"

class Alumno(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    
class Material(models.Model):
    nombre = models.CharField(max_length=256)
    marca = models.CharField(max_length=256)
    color = models.CharField(max_length=256)
    composicion = models.CharField(max_length=256)
    
    def __str__(self):
        return f"{self.nombre}, {self.marca}"

