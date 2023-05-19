from django.urls import path

from . import views

urlpatterns = [
    path("", views.ComidaCreateView.as_view(), name="comida_create"),
]


