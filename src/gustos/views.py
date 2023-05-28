
from django.shortcuts import render
from .models import Comida
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView, TemplateView
from django.urls import reverse_lazy

import tensorflow as tf
import numpy as np
import pandas as pd


class HomeView(TemplateView):
    template_name = 'home.html'


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

def predecir_comida():
    return "esto no funciona"
