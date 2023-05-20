from flask import Flask, request

app = Flask(__name__)

# Lista para almacenar los registros de comidas
comidas = []

@app.route('/registrar_comida', methods=['POST'])
def registrar_comida():
    # Obtener los datos de entrada del cuerpo de la solicitud
    data = request.get_json()

    # Obtener la hora y la comida del cuerpo de la solicitud
    hora = data['hora']
    comida = data['comida']

    # Registrar la comida en la lista
    comidas.append((hora, comida))

    # Obtener la recomendación sobre si debe comer o no
    recomendacion = recomendar_comida(comida)

    # Devolver una respuesta con la recomendación
    return {'recomendacion': recomendacion}

import openai

# Configurar la API de OpenAI
#openai.api_key = 'asdasdasdas'

def recomendar_comida(comida):
    # Generar recomendación utilizando GPT-3
    prompt = f"Comida: {comida}\nRecomendación:"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )

    recomendacion = response.choices[0].text.strip()

    return recomendacion


if __name__ == '__main__':
    app.run()