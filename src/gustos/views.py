
from django.shortcuts import render
from .models import Comida
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView, TemplateView
from django.urls import reverse_lazy

# CreateView para crear gustos de comida


class ComidaCreateView(CreateView):
    model = Comida
    template_name = "create.html"
    fields = ["nombre", "puntaje"]
