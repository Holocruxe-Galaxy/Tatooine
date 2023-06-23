
from typing import Any, Dict
from django.shortcuts import render
from .models import Comida, Tipo_Comida
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView, TemplateView
from django.urls import reverse_lazy

import tensorflow as tf
import numpy as np
import pandas as pd
from django.utils.dateformat import format
import sqlite3
import openai

from .forms import ComidaForm, AgregarComidaForm

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tipos_comida'] = Tipo_Comida.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        dia_semana = request.POST.get('dia_semana')  # int
        tipo_comida = request.POST.get('tipo_comida')  # int
        context['comidas'] = recomendar_comida(dia_semana, tipo_comida)
        return self.render_to_response(context)

# Funcion para predecir la comida que elegiria el usario segun sus gustos por puntaje del 1 al 10 con 10 siendo el mas alto


def recomendar_comida(dia_semana, tipo_comida):

    # create the dataframe from db.sqlite3 database using pd.read_sql_query
    connection = sqlite3.connect("db.sqlite3")
    dataframe = pd.read_sql_query(
        "SELECT * FROM gustos_comida", connection)
    connection.close()
    # remove id column
    dataframe = dataframe.drop(['id'], axis=1)
    # convert the values from the column fecha to week day
    dataframe['fecha'] = pd.to_datetime(dataframe['fecha'])
    dataframe['fecha'] = dataframe['fecha'].dt.day_of_week
    # index data from column nombre so its numeric
    nombres = dataframe['nombre'].unique()
    index_nombre = {value: index for index, value in enumerate(nombres)}
    dataframe['nombre'] = dataframe['nombre'].apply(lambda x: index_nombre[x])

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
    comida = nombres[int(comida[0][0])]

    return y_train.values.tolist()


def recomendar_receta_gpt(comida):
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

    recomendacion = response.choices[0].text.strip()

    return recomendacion


def mostrar_valor_nutricional_gpt(comida):
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

    recomendacion = response.choices[0].text.strip()

    return recomendacion



def preguntas_comida(request):
    if request.method == 'POST':
        form = ComidaForm(request.POST)
        if form.is_valid():
            # Aquí puedes realizar acciones con los datos enviados
            desayuno = form.cleaned_data['desayuno']
            almuerzo = form.cleaned_data['almuerzo']
            cena = form.cleaned_data['cena']
            postre = form.cleaned_data['postre']
            snack = form.cleaned_data['snack']


            # Por ahora, solo mostraremos un mensaje de éxito
            return render(request, 'exito.html')
    else:
        form = ComidaForm()

    return render(request, 'Crear_Tipo_Comida.html', {'form': form})


def agregar_comida(request):
    if request.method == 'POST':
        form = ComidaForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar la comida en la base de datos
            return render(request, 'exito2.html')
    else:
        form = ComidaForm()

    return render(request, 'agregar_comida.html', {'form': form})