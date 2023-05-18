import tensorflow
import pandas
import numpy


# Prediccion de comidas favoritas

# Creamos un dataset con los datos iniciales comidas por dia en un mes
data = {
    'Día': [1, 2, 3, 4, 5, 6, 7],
    'Comida': ['Hamburguesa', 'Pollo asado', 'Pasta', 'Sopa de verduras', 'Pizza', 'Pasta', 'Asado'],
}

# Creamos un DataFrame con los datos y lo mostramos
df = pandas.DataFrame(data)
print(df)

# Pedimos al usuario que ingrese los datos adicionales
n = 1

while input("Desea ingresar un nuevo dato? (S/N)") in ['S', 's']:
    dia = data['Día'][-1] + n
    comida = input("Ingrese la comida que se servirá: ")
    nuevo_dato = {
        'Día': dia,
        'Comida': comida, }
    df = df._append(nuevo_dato, ignore_index=True)
    print(df)
    n += 1
else:
    print("Gracias por ingresar los datos")


# Guardar DataFrame en archivo CSV
df.to_csv('comidas.csv', index=False)

# Leemos el dataset
data = pandas.read_csv("comidas.csv")

# Creamos el conjunto de entrenamiento y el conjunto de prueba
data_train = data.sample(frac=0.8, random_state=0)
data_test = data.drop(data_train.index)

# entrenar el modelo con el conjunto de entrenamiento y evaluarlo con el conjunto de prueba para ver si funciona
# Separamos las características (features) de las etiquetas (labels)
train_features = data_train.drop(columns=['Comida'])
train_labels = data_train['Comida']
test_features = data_test.drop(columns=['Comida'])
test_labels = data_test['Comida']

# Creamos el modelo de clasificación
model = tensorflow.keras.Sequential([
    tensorflow.keras.layers.Dense(16, activation='relu', input_shape=(1,)),
    tensorflow.keras.layers.Dense(16, activation='relu'),
    tensorflow.keras.layers.Dense(6, activation='softmax')
])

# Compilamos el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenamos el modelo
model.fit(train_features, train_labels, epochs=50, batch_size=32,
          validation_data=(test_features, test_labels))

# Evaluamos el modelo en datos de prueba
test_loss, test_acc = model.evaluate(test_features, test_labels)
print('Precisión en datos de prueba:', test_acc)

# Realizar inferencias con el modelo
# Generar nuevas comidas aleatorias para realizar inferencias
num_new_samples = 1
X_new = numpy.random.rand(num_new_samples, 1)

# Realizar predicciones
predictions = model.predict(X_new)

# Decodificar las etiquetas predichas
print(predictions)
