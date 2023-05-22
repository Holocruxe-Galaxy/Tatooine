import pandas as pd
import tensorflow as tf

# Create dataframe
dataframe = pd.read_csv('comidas_consumidas.csv')

# Index data so it is numerical
dias = dataframe['Dia'].unique()
index_dia = {value: index for index, value in enumerate(dias)}
dataframe['Dia'] = dataframe['Dia'].apply(lambda x: index_dia[x])
comidas = dataframe['Comida'].unique()
index_comida = {value: index for index, value in enumerate(comidas)}
dataframe['Comida'] = dataframe['Comida'].apply(lambda x: index_comida[x])

# print(dataframe.head())


# Create training data
x_train = dataframe[['Dia']]
y_train = dataframe[['Comida']]

# Create the model
modelo = tf.keras.Sequential()
modelo.add(tf.keras.layers.Dense(units=1, input_shape=[1]))


# Compile the model
modelo.compile(optimizer='adam',
               loss='mean_squared_error')

# Train the model
modelo.fit(x_train, y_train, epochs=100)

# Prediction
while True:
    dia = input("Ingrese el día: ")
    dia = dia.lower()
    dia = dia.capitalize()
    if (dia == "Exit"):
        break
    if (dia not in index_dia):
        print("El día ingresado no es válido")
        continue
    dia = index_dia[dia]
    comida = modelo.predict([dia])
    comida = comidas[int(comida[0][0])]
    print("Probablemente comas: " + comida)
