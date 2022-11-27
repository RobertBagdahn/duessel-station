# snippets/admin.py
from django.contrib import admin
from .models import *

admin.site.register(Temperature)
admin.site.register(Pressure)
admin.site.register(Humidity)
