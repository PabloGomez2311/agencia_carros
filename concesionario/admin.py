from django.contrib import admin
from .models import Concesionario, Marca, Cliente, Venta

admin.site.register(Concesionario)
admin.site.register(Marca)
admin.site.register(Cliente)
admin.site.register(Venta)