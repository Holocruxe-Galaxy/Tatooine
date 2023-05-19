from django.urls import path

from . import views

urlpatterns = [
    path("", views.ComidaListView.as_view(), name="comida_list"),
]


