from django.shortcuts import render
from .models import Concesionario, Marca, Cliente, Venta

def index(request):
    concesionarios = Concesionario.objects.all()
    marcas = Marca.objects.all()
    clientes = Cliente.objects.all()
    ventas = Venta.objects.all()
    return render(request, 'concesionario/index.html', {
        'concesionarios': concesionarios,
        'marcas': marcas,
        'clientes': clientes,
        'ventas': ventas,
    })