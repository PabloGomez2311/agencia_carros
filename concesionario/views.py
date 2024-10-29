from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehiculo, Marca, Cliente
from .forms import VehiculoForm, MarcaForm, ClienteForm

def marca_list(request):
    marcas = Marca.objects.all()
    return render(request, 'concesionario/marca_list.html', {'marcas': marcas})

def vehiculo_list(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'concesionario/vehiculo_list.html', {'vehiculos': vehiculos})

def index(request):
    vehiculos = Vehiculo.objects.all()
    marcas = Marca.objects.all()
    clientes = Cliente.objects.all()
    return render(request, 'concesionario/index.html', {
        'vehiculos': vehiculos,
        'marcas': marcas,
        'clientes': clientes
    })

# Vistas para Marca


def marca_create(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marca_list')
    else:
        form = MarcaForm()
    return render(request, 'concesionario/marca_create.html', {'form': form})

def marca_update(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('marca_list')
    else:
        form = MarcaForm(instance=marca)
    return render(request, 'concesionario/marca_form.html', {'form': form})

def marca_delete(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == 'POST':
        marca.delete()
        return redirect('marca_list')
    return render(request, 'concesionario/marca_confirm_delete.html', {'marca': marca})

# Otras vistas...

# Vistas para Vehiculo
def vehiculo_list(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'concesionario/vehiculo_list.html', {'vehiculos': vehiculos})

def vehiculo_create(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculo_list')
    else:
        form = VehiculoForm()
    return render(request, 'concesionario/vehiculo_form.html', {'form': form})

def vehiculo_update(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('vehiculo_list')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'concesionario/vehiculo_form.html', {'form': form})

def vehiculo_delete(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('vehiculo_list')
    return render(request, 'concesionario/vehiculo_confirm_delete.html', {'vehiculo': vehiculo})

# Vistas para Cliente
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'concesionario/cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'concesionario/cliente_form.html', {'form': form})

def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'concesionario/cliente_form.html', {'form': form})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'concesionario/cliente_confirm_delete.html', {'cliente': cliente})