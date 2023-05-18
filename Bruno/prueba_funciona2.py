import tensorflow as tf

# Diccionario de respuestas del modelo
respuestas = {
    'gusto_1': 'Me encantaría hacer eso.',
    'gusto_2': 'Suena interesante, definitivamente lo disfrutaría.',
    'gusto_3': 'No es mi preferencia, pero podría considerarlo.',
    'nogusto_1': 'No creo que eso sea lo mío, lo siento.',
    'nogusto_2': 'No estoy muy interesado en eso, prefiero otras actividades.',
    'nogusto_3': 'No me gusta eso en absoluto, buscaré algo más.'
}

# Definición del modelo
modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(5,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(6, activation='softmax')
])

# Compilación del modelo
modelo.compile(optimizer='adam',
               loss='sparse_categorical_crossentropy',
               metrics=['accuracy'])

# Entrenamiento del modelo con datos ficticios
entradas = tf.convert_to_tensor([
    [25, 1, 3, 2, 1],    # Ejemplo 1
    [35, 0, 2, 1, 0],    # Ejemplo 2
    [28, 1, 1, 3, 1]     # Ejemplo 3
])
etiquetas = tf.convert_to_tensor([0, 1, 2])  # Etiquetas de las respuestas

modelo.fit(entradas, etiquetas, epochs=10)

# Obtención de los datos de la persona
persona = {}
persona['edad'] = int(input("Ingrese su edad: "))
persona['genero'] = int(input("Ingrese su género (1 para femenino, 0 para masculino): "))
persona['hobbies'] = int(input("Ingrese el número de hobbies que tiene: "))
persona['idiomas'] = int(input("Ingrese el número de idiomas que habla: "))
persona['profesion'] = int(input("Ingrese su profesión (1 para arquitecto, 0 para otra profesión): "))

# Conversión de los datos de la persona a un tensor
edad = persona['edad']
genero = persona['genero']
num_hobbies = persona['hobbies']
num_idiomas = persona['idiomas']
profesion = persona['profesion']

persona_tensor = tf.convert_to_tensor([[edad, genero, num_hobbies, num_idiomas, profesion]])

# Predicción de la respuesta del modelo
prediccion = modelo.predict(persona_tensor)
indice_respuesta = tf.argmax(prediccion, axis=1).numpy()[0]

# Obtención de la respuesta del modelo basado en el índice predicho
respuesta = respuestas[f"gusto_{indice_respuesta+1}"] if indice_respuesta < 3 else respuestas[f"nogusto_{indice_respuesta-2}"]

print(respuesta)