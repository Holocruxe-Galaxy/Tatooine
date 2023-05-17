import tensorflow as tf

# Lista de lugares turísticos de Argentina
lugares = [
    'Buenos Aires', 'Bariloche', 'Cataratas del Iguazú', 'Ushuaia', 'Salta',
    'Mendoza', 'El Calafate', 'Mar del Plata', 'Puerto Madryn', 'Córdoba',
    'San Carlos de Bariloche', 'Rosario', 'Jujuy', 'Tilcara', 'Villa La Angostura',
    'Tigre', 'San Martín de los Andes', 'Colonia del Sacramento', 'Purmamarca', 'Cafayate'
]

# Diccionario de respuestas del modelo
respuestas = {
    'gusto': 'Te recomiendo visitar {} en Argentina. ¡Es un lugar hermoso!',
    'nogusto': 'No estoy seguro de qué lugar te gustaría visitar en Argentina.'
}

# Diccionario de estaciones del año y lugares recomendados
estaciones = {
    'verano': ['Mar del Plata', 'Tigre'],
    'otoño': ['Mendoza', 'San Martín de los Andes'],
    'invierno': ['Bariloche', 'Ushuaia'],
    'primavera': ['Cataratas del Iguazú', 'Córdoba']
}

# Creación de los datos de entrenamiento
entradas = tf.convert_to_tensor([[i+1] for i in range(len(lugares))])
etiquetas = tf.convert_to_tensor([1 if i % 2 == 0 else 0 for i in range(len(lugares))])

# Definición del modelo
modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compilación del modelo
modelo.compile(optimizer='adam',
               loss='binary_crossentropy',
               metrics=['accuracy'])

# Entrenamiento del modelo
modelo.fit(entradas, etiquetas, epochs=10)

# Obtención de la estación del año del usuario
estacion_usuario = input("¿En qué estación del año te encuentras? (verano, otoño, invierno, primavera): ")

# Verificación de la estación y ajuste de la predicción
if estacion_usuario in estaciones:
    lugares_estacion = estaciones[estacion_usuario]
    entradas_estacion = tf.convert_to_tensor([[lugares.index(lugar)+1] for lugar in lugares_estacion])
    prediccion = modelo.predict(entradas_estacion)
    indice_lugar = tf.argmax(prediccion, axis=1).numpy()[0]
    respuesta = respuestas['gusto'].format(lugares_estacion[indice_lugar])
else:
    respuesta = respuestas['nogusto']

print(respuesta)