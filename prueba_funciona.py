import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Paso 1: Generar datos aleatorios
np.random.seed(42)

# Generar 1000 comidas con 3 ingredientes y asignarles una categoría
num_samples = 1000
num_ingredients = 3

ingredients = ['Ajo', 'queso', 'tomate']
categories = ['frio', 'calientes', 'tibio']

X = np.random.rand(num_samples, num_ingredients)
y = np.random.choice(categories, num_samples)

# Paso 2: Preprocesamiento de datos
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 3: Preprocesamiento adicional de características
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Paso 4: Construir el modelo de clasificación
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(num_ingredients,)),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(len(categories), activation='softmax')
])

# Paso 5: Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Paso 6: Entrenar el modelo
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

# Paso 7: Evaluar el modelo en datos de prueba
test_loss, test_acc = model.evaluate(X_test, y_test)
print('Precisión en datos de prueba:', test_acc)

# Paso 8: Realizar inferencias con el modelo
# Generar nuevas comidas aleatorias para realizar inferencias
num_new_samples = 1
X_new = np.random.rand(num_new_samples, num_ingredients)
X_new = scaler.transform(X_new)

# Realizar predicciones
predictions = model.predict(X_new)

# Decodificar las etiquetas predichas
predicted_labels = label_encoder.inverse_transform(np.argmax(predictions, axis=1))

# Imprimir las predicciones
for i in range(num_new_samples):
    print('Comida:', X_new[i])
    print('Categoría predicha:', predicted_labels[i])
    print()