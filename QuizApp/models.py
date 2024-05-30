from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.CharField(max_length=10)
    ficha = models.CharField(max_length=100)


    class Meta:
        verbose_name = 'alumno'
        verbose_name_plural = 'alumnos'

    def __str__(self):
        return self.nombre
    
    