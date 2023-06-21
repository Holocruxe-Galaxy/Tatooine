from django.urls import path

from . import views
from views import *

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('preguntas-comida/', preguntas_comida, name='preguntas_comida'),
]
