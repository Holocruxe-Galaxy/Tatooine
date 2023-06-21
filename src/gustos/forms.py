from django import forms
from .models import Tipo_Comida

class ComidaForm(forms.Form):
    desayuno = forms.ModelChoiceField(queryset=Tipo_Comida.objects.all())
    almuerzo = forms.ModelChoiceField(queryset=Tipo_Comida.objects.all())
    cena = forms.ModelChoiceField(queryset=Tipo_Comida.objects.all())
    postre = forms.ModelChoiceField(queryset=Tipo_Comida.objects.all())
    snack = forms.ModelChoiceField(queryset=Tipo_Comida.objects.all())
