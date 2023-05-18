import tensorflow as tf

#lista de gustos
gustos_comidas = [
'pizza',
'empanadas',
'asado',
'milanesa',
'helado',
'hamburguesa',
'choripán',
'Ñoquis',
'churrasco',
'tarta',
'tacos',
'sushi',
'bondiola',
'parrillada',
'revuelto gramajo',
'matambre',
'locro',
'humita',
'rabas',
'mariscos',
'pollo al disco',
'carbonada',
'pastel de papa',
'ravioles',
'fideos con tuco',
'lomito',
'gnocchi',
'wok de pollo',
'bife de chorizo',
'provoleta',
'chipá',
'puchero',
'pasta frola',
'bagna cauda',
'mondongo',
'sopa paraguaya',
'pastelitos',
'tamales',
'criolla',
'fainá',
'tamal en cazuela',
]

#diccionario de respuestas
respuestas = {
    'gusto': 'Te recomiendo comer {} en Argentina. ¡Es lo más rico!',
    'nogusto': 'No estoy seguro de qué recomendarte comer en Argentina.'
}

#Recomendaciones
Recomendaciones = {
"carnes" : ['asado', 'milanesa', 'choripán', 'churrasco', 'bondiola', 'parrillada', 'matambre', 'pollo al disco', 'carbonada', 'bife de chorizo'],

"pastas" : ['Ñoquis', 'tarta', 'ravioles', 'fideos con tuco', 'gnocchi'],

"rápida" : ['pizza', 'empanadas', 'helado', 'hamburguesa', 'tacos', 'sushi', 'tamales', 'criolla', 'tamal en cazuela'],

"otros" : ['humita', 'revuelto gramajo', 'locro', 'rabas', 'mariscos', 'pastel de papa', 'lomito', 'wok de pollo', 'provoleta', 'chipá', 'puchero', 'pasta frola', 'bagna cauda', 'mondongo', 'sopa paraguaya', 'pastelitos', 'fainá'],

}
# Creación de los datos de entrenamiento
entradas = tf.convert_to_tensor([[i+1] for i in range(len(gustos_comidas))])
etiquetas = tf.convert_to_tensor([1 if i % 2 == 0 else 0 for i in range(len(gustos_comidas))])

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
modelo.fit(entradas, etiquetas, epochs=20)

recomendacion_comida = input("¿Que le gustaria comer hoy? (carnes, pastas, rápida, otros): ")

# Verificación de la estación y ajuste de la predicción
if recomendacion_comida in Recomendaciones:
    lugares_estacion = Recomendaciones[recomendacion_comida]
    entradas_estacion = tf.convert_to_tensor([[gustos_comidas.index(comida)+1] for comida in lugares_estacion])
    prediccion = modelo.predict(entradas_estacion)
    indice_lugar = tf.argmax(prediccion, axis=1).numpy()[0]
    respuesta = respuestas['gusto'].format(lugares_estacion[indice_lugar])
else:
    respuesta = respuestas['nogusto']

print(respuesta)
