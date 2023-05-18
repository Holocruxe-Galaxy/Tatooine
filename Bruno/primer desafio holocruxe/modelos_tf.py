import tensorflow as tf
from datos import *
import random

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

gustos_musicales = [
    'rock',
    'pop',
    'hip hop',
    'electrónica',
    'reggaetón',
    'jazz',
    'blues',
    'metal',
    'folklore',
    'cumbia',
    'tango',
    'clásica',
    'reggae',
    'salsa',
    'country',
    'punk',
    'indie',
    'rap',
    'trap',
]

gustos_deportivos = [
    'fútbol',
    'tenis',
    'rugby',
    'basquet',
    'voley',
    'automovilismo',
    'hockey',
    'boxeo',
    'atletismo',
    'handball',
    'natación',
    'ciclismo',
    'golf',
    'patinaje',
    'surf',
    'esquí',
    'paddle',
    'karate',
]

gustos_generales = [
    'viajar',
    'ver películas',
    'leer',
    'escuchar música',
    'deportes',
    'comer',
    'bailar',
    'salir con amigos',
    'jugar videojuegos',
    'pintar',
    'escribir',
    'ir de compras',
    'acampar',
    'hacer manualidades',
    'cantar',
    'tocar un instrumento',
    'jardinería',
    'meditar',
]

#diccionario de respuestas
respuestas_comidas = {
    'gusto': 'Te recomiendo comer {} en Argentina. ¡Es lo más rico!',
    'nogusto': 'No estoy seguro de qué recomendarte comer en Argentina.'
}

#diccionario de respuestas gustos_musicales
respuestas_musicales = {
    'gusto': 'Te recomiendo escuchar {} en Argentina. ¡Es lo más!',
    'nogusto': 'No estoy seguro de qué recomendarte escuchar en Argentina.'
}

#diccionario de respuestas gustos_deportivos
respuestas_deportivos = {
    'gusto': 'Te recomiendo practicar {} en Argentina. ¡Es lo más!',
    'nogusto': 'No estoy seguro de qué recomendarte practicar en Argentina.'
}

#diccionario de respuestas gustos_generales
respuestas_generales = {
    'gusto': 'Te recomiendo {} en Argentina. ¡Es lo más!',
    'nogusto': 'No estoy seguro de qué recomendarte hacer en Argentina.'
}

#Recomendaciones gustos_comidas
Recomendaciones_comidas = {
"carnes" : ['asado', 'milanesa', 'choripán', 'churrasco', 'bondiola', 'parrillada', 'matambre', 'pollo al disco', 'carbonada', 'bife de chorizo'],

"pastas" : ['Ñoquis', 'tarta', 'ravioles', 'fideos con tuco', 'gnocchi'],

"rápida" : ['pizza', 'empanadas', 'helado', 'hamburguesa', 'tacos', 'sushi', 'tamales', 'criolla', 'tamal en cazuela'],

"otros" : ['humita', 'revuelto gramajo', 'locro', 'rabas', 'mariscos', 'pastel de papa', 'lomito', 'wok de pollo', 'provoleta', 'chipá', 'puchero', 'pasta frola', 'bagna cauda', 'mondongo', 'sopa paraguaya', 'pastelitos', 'fainá'],

}

#Recomendaciones gustos_musicales
Recomendaciones_musicales = {
    'rock': ['Divididos', 'Los Piojos', 'Los Redondos', 'Soda Stereo', 'Sumo', 'Viejas Locas', 'La Renga', 'Las Pelotas', 'Babasónicos', 'Los Gardelitos', 'Los Auténticos Decadentes', 'Los Fabulosos Cadillacs', 'Los Pericos', 'Los Caligaris', 'Los Tipitos', 'Los Cafres', 'Los Abuelos de la Nada', 'Los Enanitos Verdes', 'Los Violadores', 'Los Ratones Paranoicos', 'Los Twist', 'Los 7 Delfines', 'Los Brujos', ],
    'pop': ['Miranda!', 'Axel', 'Lali Espósito', 'Tini Stoessel', 'Luciano Pereyra', 'Diego Torres', 'Sandra?',],
    'hip hop': ['Duki', 'Khea', 'Cazzu', 'Trueno'],
    'electrónica': ['Soda Stereo', 'Miranda!', 'Gustavo Cerati'],
    'reggaetón': ['Paulo Londra', 'Nicky Jam', 'Sebastian Yatra'],
    'jazz': ['Lito Vitale', 'Gonzalo Rubalcaba', 'Daniel Barenboim'],
    'blues': ['La Mississippi', 'Pappo', 'Rata Blanca'],
    'metal': ['Rata Blanca', 'V8', 'Tren Loco'],
    'folklore': ['Atahualpa Yupanqui', 'Los Chalchaleros', 'Soledad Pastorutti'],
    'cumbia': ['Damian Cordoba', 'Amar Azul', 'Los Palmeras'],
    'tango': ['Carlos Gardel', 'Astor Piazzolla', 'Juan DArienzo'],
    'clásica': ['Martha Argerich', 'Orquesta Filarmónica de Buenos Aires', 'Orquesta Sinfónica Nacional'],
    'reggae': ['Los Pericos', 'Dread Mar I', 'Gondwana'],
    'salsa': ['Rubén Blades', 'Marc Anthony', 'Grupo Niche'],
    'country': ['Chaqueño Palavecino', 'Jorge Rojas', 'Los Nocheros'],
    'punk': ['Attaque 77', 'Flema', '2 Minutos'],
    'indie': ['Babasónicos', 'El Mató a un Policía Motorizado', 'Usted Señalemelo'],
    'rap': ['Emanero', 'C.R.O', 'Klan'],
    'trap': ['Duki', 'Khea', 'Cazzu'],
}

#Recomendaciones gustos_deportivos
Recomendaciones_deportivos = {
    'deportes_riesgo': ['automovilismo', 'surf', 'esquí'],
    'deportes_pelota': ['fútbol', 'tenis', 'rugby', 'basquet', 'voley', 'hockey', 'handball', 'paddle'],
    'deportes_combate': ['boxeo', 'karate'],
    'otros_deportes': ['atletismo', 'natación', 'ciclismo', 'golf', 'patinaje']
}

#Recomendaciones gustos_generales
Recomendaciones_generales = {
    'viajar': ['playa', 'ciudad histórica', 'naturaleza', 'montañas'],
    'ver películas': ['comedia', 'acción', 'drama', 'suspenso', 'ciencia ficción'],
    'leer': ['novela', 'biografía', 'fantasía', 'poesía', 'ensayo'],
    'escuchar música': ['rock', 'pop', 'hip hop', 'electrónica', 'jazz'],
    'deportes': ['fútbol', 'tenis', 'rugby', 'basquet', 'voley'],
    'comer': ['carnes', 'pastas', 'rápida', 'otros'],
    'bailar': ['salsa', 'bachata', 'hip hop', 'tango', 'reggaetón'],
    'salir con amigos': ['bar', 'restaurante', 'cine', 'concierto', 'fiesta'],
    'jugar videojuegos': ['acción', 'aventura', 'estrategia', 'deportes', 'rol'],
    'pintar': ['óleo', 'acrílico', 'acuarela', 'carboncillo', 'pastel'],
    'escribir': ['cuento', 'poesía', 'novela', 'ensayo', 'diario'],
    'ir de compras': ['ropa', 'electrónica', 'libros', 'decoración', 'alimentos'],
    'acampar': ['bosque', 'playa', 'montaña', 'lago', 'desierto'],
    'hacer manualidades': ['origami', 'costura', 'bisutería', 'cerámica', 'scrapbooking'],
    'cantar': ['pop', 'rock', 'baladas', 'rap', 'country'],
    'tocar un instrumento': ['guitarra', 'piano', 'violín', 'batería', 'flauta'],
    'jardinería': ['flores', 'plantas suculentas', 'horticultura', 'jardín de hierbas', 'bonsái'],
    'meditar': ['mindfulness', 'yoga', 'respiración consciente', 'visualización', 'mantras']
}


def hacer_recomendaciones_comidas(gustos_comidas, respuestas_comidas, Recomendaciones_comidas):
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
    if recomendacion_comida in Recomendaciones_comidas:
        lugares_estacion = Recomendaciones_comidas[recomendacion_comida]
        entradas_estacion = tf.convert_to_tensor([[gustos_comidas.index(comida)+1] for comida in lugares_estacion])
        prediccion = modelo.predict(entradas_estacion)
        indice_lugar = tf.argmax(prediccion, axis=1).numpy()[0]
        respuesta = respuestas_comidas['gusto'].format(lugares_estacion[indice_lugar])
    else:
        respuesta = respuestas_comidas['nogusto']

    return respuesta


#recomendacion_comida = hacer_recomendaciones(gustos_comidas, respuestas_comidas, Recomendaciones_comidas)
#print(recomendacion_comida)

def hacer_recomendaciones_musicales(gustos_musicales, respuestas_musicales, Recomendaciones_musicales):
    # Creación de los datos de entrenamiento
    entradas = tf.convert_to_tensor([[i+1] for i in range(len(gustos_musicales))])
    etiquetas = tf.convert_to_tensor([1 if i % 2 == 0 else 0 for i in range(len(gustos_musicales))])
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
    recomendacion_musica = input("¿Que le gustaria escuchar hoy?gustos_musicales = ['rock', 'pop', 'hip hop', 'electrónica', 'reggaetón', 'jazz', 'blues', 'metal', 'folklore', 'cumbia', 'tango', 'clásica', 'reggae', 'salsa', 'country', 'punk', 'indie', 'rap', 'trap']: ")
    # Verificación de la estación y ajuste de la predicción
    if recomendacion_musica in Recomendaciones_musicales:
        lugares_estacion = Recomendaciones_musicales[recomendacion_musica]
        entradas_estacion = tf.convert_to_tensor([[gustos_musicales.index(musica)+1] for musica in lugares_estacion])
        prediccion = modelo.predict(entradas_estacion)
        indice_lugar = tf.argmax(prediccion, axis=1).numpy()[0]
        respuesta = respuestas_musicales['gusto'].format(lugares_estacion[indice_lugar])
    else:
        respuesta = respuestas_musicales['nogusto']
    return respuesta
#recomendacion_musical = hacer_recomendaciones(gustos_musicales, respuestas_musicales, Recomendaciones_musicales)
#print(recomendacion_musical)

def hacer_recomendaciones_deportivos(gustos_deportivos, respuestas_deportivos, Recomendaciones_deportivos):
    # Creación de los datos de entrenamiento
    entradas = tf.convert_to_tensor([[i+1] for i in range(len(gustos_deportivos))])
    etiquetas = tf.convert_to_tensor([1 if i % 2 == 0 else 0 for i in range(len(gustos_deportivos))])
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
    recomendacion_deportes = input("¿Que le gustaria hacer hoy? (deportes_riesgo, deportes_pelota, deportes_combate, otros_deportes): ")
    # Verificación de la estación y ajuste de la predicción
    if recomendacion_deportes in Recomendaciones_deportivos:
        lugares_estacion = Recomendaciones_deportivos[recomendacion_deportes]
        entradas_estacion = tf.convert_to_tensor([[gustos_deportivos.index(deporte)+1] for deporte in lugares_estacion])
        prediccion = modelo.predict(entradas_estacion)
        indice_lugar = tf.argmax(prediccion, axis=1).numpy()[0]
        respuesta = respuestas_deportivos['gusto'].format(lugares_estacion[indice_lugar])
    else:
        respuesta = respuestas_deportivos['nogusto']
    return respuesta
#recomendacion_deportiva = hacer_recomendaciones(gustos_deportivos, respuestas_deportivos, Recomendaciones_deportivos)
#print(recomendacion_deportiva)

def hacer_recomendaciones_generales(gustos_generales,respuestas_generales, Recomendaciones_generales):
    # Creación de los datos de entrenamiento
    entradas = tf.convert_to_tensor([[i+1] for i in range(len(gustos_generales))])
    etiquetas = tf.convert_to_tensor([1 if i % 2 == 0 else 0 for i in range(len(gustos_generales))])
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
    recomendacion_general = input("¿Que le gustaria hacer hoy? ['viajar', 'ver películas', 'leer', 'escuchar música', 'deportes', 'comer', 'bailar', 'salir con amigos', 'jugar videojuegos', 'pintar', 'escribir', 'ir de compras', 'acampar', 'hacer manualidades', 'cantar', 'tocar un instrumento', 'jardinería', 'meditar'] ")
    # Verificación de la estación y ajuste de la predicción
    if recomendacion_general in Recomendaciones_generales:
        lugares_estacion = Recomendaciones_generales[recomendacion_general]
        entradas_estacion = tf.convert_to_tensor([[gustos_generales.index(general)+1] for general in lugares_estacion])
        prediccion = modelo.predict(entradas_estacion)
        indice_lugar = tf.argmax(prediccion, axis=1).numpy()[0]
        respuesta = respuestas_generales['gusto'].format(lugares_estacion[indice_lugar])
    else:
        respuesta = respuestas_generales['nogusto']
    return respuesta
#recomendacion_general = hacer_recomendaciones(gustos_generales, respuestas_generales, Recomendaciones_generales)
#print(recomendacion_general)

