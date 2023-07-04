
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


class HomeView(TemplateView):
    template_name = 'home.html'


from django.db.models import Count
from django.utils import timezone
from random import randint
from datetime import timedelta

def add_synthetic_data():
    if meal_type.objects.count() > 0:
        return

    # Crea los tipos de comida
    meal_type.objects.create(name='Breakfast')
    meal_type.objects.create(name='Lunch')
    meal_type.objects.create(name='Dinner')

    # Crea algunas comidas
    meals = [
        {'name': 'Toast', 'type': 'Breakfast'},
        {'name': 'Salad', 'type': 'Lunch'},
        {'name': 'Steak', 'type': 'Dinner'},
        # Agrega más comidas aquí
    ]

    for meal_data in meals:
        type_name = meal_data['type']
        meal_type_obj = meal_type.objects.get(name=type_name)
        meal.objects.create(name=meal_data['name'], type=meal_type_obj)

    # Crea usuarios
    users = [
        {'name': 'John Doe'},
        {'name': 'Jane Smith'},
        {'name': 'David Johnson'},
        # Agrega más usuarios aquí
    ]

    for user_data in users:
        user.objects.create(name=user_data['name'])

    # Crea comidas para usuarios en fechas aleatorias
    num_users = user.objects.count()
    num_meals = meal.objects.count()

    for _ in range(10):  # Cambia este número según cuántos registros quieres crear
        random_user = user.objects.order_by('?').first()
        random_meal = meal.objects.order_by('?').first()
        random_date = timezone.now() - timedelta(days=randint(1, 30))

        user_meal.objects.create(id_user=random_user, id_meal=random_meal, date=random_date)

add_synthetic_data()


from django.shortcuts import redirect

def generate_synthetic_data(request):
    add_synthetic_data()
    return redirect('home') 