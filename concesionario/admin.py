from django.contrib import admin
from .models import Vehiculo, Marca, Cliente

admin.site.register(Vehiculo)
admin.site.register(Marca)
admin.site.register(Cliente)