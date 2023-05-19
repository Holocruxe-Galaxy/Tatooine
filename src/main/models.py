from django.db import models

# Create your models here.


class Comida(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    puntaje = models.IntegerField()

    def __str__(self):
        return self.nombre


# gustos_comidas = {
#     'pizza': 10,
#     'empanadas': 10,
#     'asado': 10,
#     'milanesa': 9,
#     'helado': 9,
#     'hamburguesa': 8,
#     'choripán': 8,
#     'Ñoquis': 8,
#     'churrasco': 7,
#     'tarta': 7,
#     'tacos': 6,
#     'sushi': 6,
#     'bondiola': 6,
#     'parrillada': 6,
#     'revuelto gramajo': 5,
#     'matambre': 5,
#     'locro': 5,
#     'humita': 5,
#     'rabas': 4,
#     'mariscos': 4,
#     'pollo al disco': 4,
#     'carbonada': 4,
#     'pastel de papa': 4,
#     'ravioles': 3,
#     'fideos con tuco': 3,
#     'lomito': 3,
#     'gnocchi': 3,
#     'wok de pollo': 3,
#     'bife de chorizo': 2,
#     'provoleta': 2,
#     'chipá': 2,
#     'puchero': 2,
#     'pasta frola': 2,
#     'bagna cauda': 1,
#     'mondongo': 1,
#     'sopa paraguaya': 1,
#     'pastelitos': 1,
#     'tamales': 1,
#     'criolla': 1,
#     'fainá': 1,
#     'tamal en cazuela': 1,
#     'asado al asador': 10,

# }
