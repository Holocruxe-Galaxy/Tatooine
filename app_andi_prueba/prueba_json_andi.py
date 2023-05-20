import requests
import json

# Datos de entrada para registrar la comida
input_data = {
    'hora': '15:55',
    'comida': 'arepas'
}

# Enviar la solicitud POST al servidor Flask
response = requests.post('http://localhost:5000/registrar_comida', json=input_data)

# Obtener la respuesta del servidor
response_data = response.json()

# Imprimir la recomendación
recomendacion = response_data['recomendacion']
print(f'Recomendación: {recomendacion}')