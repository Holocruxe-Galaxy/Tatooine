# add jupyter notebook to the project

# %%

import tensorflow as tf
import numpy as np
import pandas as pd
from django.utils.dateformat import format
import sqlite3
import openai

#


# Get the dataframe from the database


def get_dataframe():
    # create the dataframe from db.sqlite3 database using pd.read_sql_query
    connection = sqlite3.connect("db.sqlite3")
    dataframe = pd.read_sql_query(
        "SELECT * FROM user_meal", connection)
    connection.close()
    return dataframe

# Format the dataframe to be used in the model


def format(dataframe):
    # remove id column
    dataframe = dataframe.drop(['id'], axis=1)
    # convert the values from the column date to week day
    dataframe['date'] = pd.to_datetime(dataframe['date'])
    dataframe['date'] = dataframe['date'].dt.day_of_week
    # index data from column name so its numeric
    names = dataframe['name'].unique()
    name_index = {value: index for index, value in enumerate(names)}
    dataframe['name'] = dataframe['name'].apply(lambda x: name_index[x])
    return dataframe

# Train the model - If is already trained then add the new training data, else train the model with sintetic data


def train(dataframe):
    # Create training data
    x_train = dataframe[['date']]
    y_train = dataframe[['name']]
    z_train = dataframe[['meal_type']]

    # Create the model
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

    # Compile the model
    model.compile(optimizer='adam',
                  loss='mean_squared_error')

    # Train the model
    model.fit(x_train, y_train, z_train, epochs=10)

    # Save the model
    model.save('model.h5')
