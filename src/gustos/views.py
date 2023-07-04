
from typing import Any, Dict
from django.shortcuts import render
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView, TemplateView
from django.urls import reverse_lazy

import tensorflow as tf
import numpy as np
import pandas as pd
from django.utils.dateformat import format
import sqlite3
import openai


class HomeView(TemplateView):
    template_name = 'home.html'

    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     context['tipos_comida'] = Tipo_Comida.objects.all()
    #     return context

    # def post(self, request, *args, **kwargs):
    #     context = self.get_context_data()
    #     dia_semana = request.POST.get('dia_semana')  # int
    #     tipo_comida = request.POST.get('tipo_comida')  # int
    #     context['comidas'] = predict(dia_semana, tipo_comida)
    #     return self.render_to_response(context)

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
    # index data from column nombre so its numeric
    names = dataframe['name'].unique()
    name_index = {value: index for index, value in enumerate(names)}
    dataframe['name'] = dataframe['name'].apply(lambda x: name_index[x])
    return dataframe

# Train the model - If is already trained then add the new training data, else train the model with sintetic data


def train(dataframe):
    names = dataframe['name'].unique()
    # Create training data
    x_train = dataframe[['fecha']]
    y_train = dataframe[['nombre']]

    # Create the model
    modelo = tf.keras.Sequential()
    modelo.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

    # Compile the model
    modelo.compile(optimizer='adam',
                   loss='mean_squared_error')

    # Train the model
    modelo.fit(x_train, y_train, epochs=10)

    # Prediction
    dia_semana = int(dia_semana)
    comida = modelo.predict([dia_semana])
    comida = names[int(comida[0][0])]

    return y_train.values.tolist()

# Predict the meal for a given day of the week and meal type


def predict(date, meal_type):
    pass

# Recommend a recipe based on the predicted meal for the date and meal type


def recommend_recipe_gpt(comida):
    # Generate a prompt for the GPT-3 model based on the user's input and return a recipe recommendation
    prompt = f"receta para preparar {comida}\nformato:\ningredientes:\npreparacion:\n"

    # Initialize the OpenAI API with your credentials
    openai.api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your actual API key

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )

    recommenadtion = response.choices[0].text.strip()

    return recommenadtion

# Return the nutritional value of the predicted meal for the date and meal type


def nutritional_value_gpt(comida):
    # Generate a prompt for the GPT-3 model based on the user's input and return a recipe recommendation
    prompt = f"valor nutricional general de {comida}\n"

    # Initialize the OpenAI API with your credentials
    openai.api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your actual API key

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )

    recommenadtion = response.choices[0].text.strip()

    return recommenadtion
