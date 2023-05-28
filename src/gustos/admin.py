from django.contrib import admin

# Register your models here.

from .models import Comida, Tipo_Comida

admin.site.register(Comida)
admin.site.register(Tipo_Comida)
