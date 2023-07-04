from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(user)
admin.site.register(meal_type)
admin.site.register(meal)
admin.site.register(user_meal)
