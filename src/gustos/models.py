from django.db import models

# El modelo usuario sera movido a la app usuarios en el futuro


class User(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=100)
    comidas = models.ManyToManyField("Comida", blank=True)

    def __str__(self):
        return self.nombre

# Comidas y tipos de comidas (desayuno, almuerzo, cena, etc)

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




class tipo_comida2(models.Model):
    id_tipo_comida = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class comida2(models.Model):
    id_comida = models.AutoField(primary_key=True)
    tipo = models.ForeignKey(tipo_comida2, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    comidacol = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class usuario_comida(models.Model):
    id_usuario_comida = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    comida = models.ForeignKey(comida2, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.usuario} - {self.comida} ({self.fecha})"