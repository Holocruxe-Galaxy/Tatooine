from django.db import models

# Create your models here.


class User(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=100)
    comidas = models.ManyToManyField("Comida", blank=True)

    def __str__(self):
        return self.nombre


class Tipo_Comida(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Comida(models.Model):
    fecha = models.DateField()
    nombre = models.CharField(max_length=100)
    tipo = models.ForeignKey(Tipo_Comida, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fecha}: {self.tipo} - {self.nombre}"
