from django.db import models

# Create your models here.


class User(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=100)
    gustos_comida = models.ManyToManyField(
        'Comida', related_name='gustos_comida')
    comidas_consumidas = models.ManyToManyField(
        'Comida', related_name='comidas_consumidas')

    def __str__(self):
        return self.nombre


class Comida(models.Model):
    nombre = models.CharField(max_length=100)
    puntaje = models.IntegerField()

    def __str__(self):
        return self.nombre
    


