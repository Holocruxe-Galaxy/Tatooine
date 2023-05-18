import tensorflow as tf
import numpy as np

# Definir los datos de entrenamiento
x_train = np.array([[18, 0, 70, 3], [25, 1, 80, 5], [32, 0, 75, 7], [40, 1, 85, 10], [45, 0, 90, 12]], dtype=np.float32)
y_train = np.array([[20], [18], [16], [14], [12]], dtype=np.float32)

# Definir el modelo
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1, input_shape=(4,)))

# Compilar el modelo
model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.001), loss='mean_squared_error')

# Entrenar el modelo
model.fit(x_train, y_train, epochs=1000, verbose=0)

# Hacer una predicción con el modelo entrenado
x_test = np.array([[28, 1, 85, 8]], dtype=np.float32)
y_pred = model.predict(x_test)
print('Predicción:', y_pred)
