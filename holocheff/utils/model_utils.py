import pandas as pd
import tensorflow as tf
import os
import numpy as np

# entrenar el modelo trayendo el dataframe.csv
def train_model():
    pass
# guardar el modelo en un archivo .h5
def save_model():
    pass
# # crear checkpoint para el modelo


# Obtener la ruta absoluta del archivo CSV
current_dir = os.path.dirname(__file__)
csv_file = os.path.join(current_dir, 'C:/Users/User/OneDrive/Escritorio/tatooine/Tatooine/holocheff/data/dataframe.csv')

# Leer el archivo CSV
try:
    data = pd.read_csv(csv_file)
    print("Archivo CSV leído correctamente.")
except Exception as e:
    print("Error al leer el archivo CSV:")
    print(str(e))

# Obtener las características y etiquetas del DataFrame
ids = data['_id'].values
days = data['day'].values.astype(int)
user_ids = data['user_id'].values
breakfast = data['breakfast'].values.astype(int)
lunch = data['lunch'].values.astype(int)
dinner = data['dinner'].values.astype(int)

# Definir el modelo
inputs = tf.keras.Input(shape=(4,))
x = tf.keras.layers.Dense(10, activation='relu')(inputs)
outputs = tf.keras.layers.Dense(3, activation='linear')(x)  # Utilizamos activación "linear" para obtener valores enteros
model = tf.keras.Model(inputs=inputs, outputs=outputs)

# Compilar el modelo
model.compile(optimizer='adam', loss='mean_squared_error')  # Usamos "mean_squared_error" para valores enteros

# Preparar los datos de entrada y etiquetas
X = np.column_stack((days, breakfast, lunch, dinner))
y = np.column_stack((breakfast, lunch, dinner))

# Escalar los datos de las etiquetas a enteros (opcional, según la magnitud de los valores)
y = y.astype(int)

# Entrenar el modelo
model.fit(X, y, epochs=1000)

# Obtener la entrada del usuario para el día
day_input = input("Ingresa el valor del día para hacer la predicción: ")
day_input = int(day_input)

# Buscar el índice correspondiente al día ingresado
day_index = np.where(days == day_input)[0]

# Verificar si se encontró un índice válido
if len(day_index) > 0:
    day_index = day_index[0]
    input_data = X[day_index].reshape(1, -1)

    # Obtener la predicción para el día ingresado
    prediction = model.predict(input_data)[0]
    print(f"Predicciones enteras para el día {day_input}: {prediction.astype(int)}")
else:
    print("Día no encontrado en los datos.")


