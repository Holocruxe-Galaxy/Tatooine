
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


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tipos_comida'] = Tipo_Comida.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        dia_semana = request.POST.get('dia_semana')
        tipo_comida = request.POST.get('tipo_comida')
        context['comidas'] = recomendar_comida(dia_semana, tipo_comida)
        return self.render_to_response(context)


class ComidaListView(ListView):
    model = Comida
    template_name = 'comida_list.html'
    context_object_name = 'comidas'


class ComidaCreateView(CreateView):
    model = Comida
    template_name = 'comida_create.html'
    fields = '__all__'
    success_url = reverse_lazy('comida_list')


class ComidaUpdateView(UpdateView):
    model = Comida
    template_name = 'comida_update.html'
    fields = '__all__'
    success_url = reverse_lazy('comida_list')


class ComidaDeleteView(DeleteView):
    model = Comida
    template_name = 'comida_delete.html'
    success_url = reverse_lazy('comida_list')


# Funcion para predecir la comida que elegiria el usario segun sus gustos por puntaje del 1 al 10 con 10 siendo el mas alto

def recomendar_comida(dia_semana, tipo_comida):
    if (dia_semana == None or tipo_comida == None):
        return ""
    # create the dataframe from db.sqlite3 database using pd.read_sql_query
    connection = sqlite3.connect("db.sqlite3")
    dataframe = pd.read_sql_query(
        "SELECT * FROM gustos_comida", connection)
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
    comida = modelo.predict([dia_semana])
    comida = nombres[int(comida[0][0])]
    return comida


def recomendar_comida_gpt(comida):
    # Generar recomendación utilizando GPT-3
    prompt = f"Comida: {comida}\n Recomendación:"
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
