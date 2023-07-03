from django.db import models

class tipo_comida(models.Model):
    id_tipo_comida = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class comida(models.Model):
    id_comida = models.AutoField(primary_key=True)
    tipo = models.ForeignKey(tipo_comida, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class usuario_comida(models.Model):
    id_usuario_comida = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    id_comida = models.ForeignKey(comida, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.usuario} - {self.comida} ({self.fecha})"