
from typing import Any, Dict
from django.shortcuts import render
from .models import Comida, Tipo_Comida
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView, TemplateView
from django.urls import reverse_lazy

import tensorflow as tf
import numpy as np
import pandas as pd


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tipos_comida'] = Tipo_Comida.objects.all()
        context['dias_semana'] = ['Lunes', 'Martes', 'Miercoles',
                                  'Jueves', 'Viernes', 'Sabado', 'Domingo']
        dia_semana = self.request.POST.get('dia_semana')
        tipo_comida = self.request.POST.get('tipo_comida')
        context['resultado'] = predecir_comida(dia_semana, tipo_comida)
        return context


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

def predecir_comida(dia, tipo_comida):
    if (dia != None and tipo_comida != None):
        return "comida"
    else:
        return ""
