from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('generate_data/', generate_synthetic_data, name='generate_data'),
]
