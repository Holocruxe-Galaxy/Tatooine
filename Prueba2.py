import tensorflow as tf
import pandas as pd
import ipywidgets as widgets

# Creamos un DataFrame vacío con las columnas necesarias
df = pd.DataFrame(columns=['Día', 'Comida', 'Plato Principal', 'Acompañamiento', 'Bebida'])

# Creamos las opciones para cada variable
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
comidas = ['Hamburguesa', 'Pollo asado', 'Pasta', 'Sopa de verduras', 'Pizza', 'Asado']
platos_principales = ['Carne', 'Pollo', 'Pasta', 'Verduras', 'Pizza']
acompañamientos = ['Papas fritas', 'Ensalada', 'Pan', 'Crutones', 'Frutas', 'Papas']
bebidas = ['Agua', 'Refresco']

# Creamos los widgets para cada variable
dia_widget = widgets.Dropdown(options=dias, description='Día:')
comida_widget = widgets.Dropdown(options=comidas, description='Comida:')
plato_principal_widget = widgets.Dropdown(options=platos_principales, description='Plato Principal:')
acompañamiento_widget = widgets.Dropdown(options=acompañamientos, description='Acompañamiento:')
bebida_widget = widgets.Dropdown(options=bebidas, description='Bebida:')

# Mostramos los widgets al usuario
display(dia_widget)
display(comida_widget)
display(plato_principal_widget)
display(acompañamiento_widget)
display(bebida_widget)

# Obtenemos los valores seleccionados por el usuario
dia = dia_widget.value
comida = comida_widget.value
plato_principal = plato_principal_widget.value
acompañamiento = acompañamiento_widget.value
bebida = bebida_widget.value

# Creamos un nuevo diccionario con los datos adicionales
nuevo_dato = {
    'Día': dia,
    'Comida': comida,
    'Plato Principal': plato_principal,
    'Acompañamiento' : acompañamiento,
    'Bebida' : bebida,
}

# Agregamos el nuevo dato al DataFrame
df = df.append(nuevo_dato, ignore_index=True)

# Mostramos el DataFrame actualizado
print(df)

# Guardar DataFrame en archivo CSV
df.to_csv('comidas.csv', index=False)

# Leemos el dataset
data = pd.read_csv("comidas.csv")

# Creamos el conjunto de entrenamiento y el conjunto de prueba
train_data = data.sample(frac=0.8, random_state=0)
test_data = data.drop(train_data.index)

# Separamos las características (features) de las etiquetas (labels)
train_features = train_data.drop(columns=['Comida'])
train_labels = train_data['Comida']
test_features = test_data.drop(columns=['Comida'])
test_labels = test_data['Comida']

print(train_features,"Aca 1")
print(train_labels,"Aca 2")
print(test_features,"Aca 3")
print(test_labels,"Aca 4")

# Creamos un modelo secuencial de TensorFlow
model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(3,)),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(6, activation='softmax')
])

print("Antes de compilar")

try:
    # Compilamos el modelo
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    print("Antes de entrenar")

    # Entrenamos el modelo
    model.fit(train_features, train_labels, epochs=50)

    # Evaluamos el modelo con el conjunto de prueba
    test_loss, test_acc = model.evaluate(test_features, test_labels, verbose=2)
    print('\nTest accuracy:', test_acc)
    
except ValueError as e:
    print("Error de entrada del modelo:", e)
    # Manejar el error de entrada del modelo de manera adecuada
except Exception as e:
    print("Ocurrió un error inesperado durante el entrenamiento del modelo:", e)
    # Manejar cualquier otro error de manera adecuada

