from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehiculo, Marca, Cliente
from .forms import VehiculoForm, MarcaForm, ClienteForm
from django.shortcuts import render
from .models import Cliente, Vehiculo, Marca
<<<<<<< HEAD
from django.db.models import Count

def index(request):
    # Estadísticas básicas
    total_clientes = Cliente.objects.count()
    total_vehiculos = Vehiculo.objects.count()
    total_marcas = Marca.objects.count()

    # Lista de clientes y vehículos
    clientes = Cliente.objects.all()[:5]  # Limitamos a 5 clientes
    vehiculos = Vehiculo.objects.select_related('marca').all()[:5]  # Limitamos a 5 vehículos

=======

def index(request):
    total_clientes = Cliente.objects.count()
    total_vehiculos = Vehiculo.objects.count()
    total_marcas = Marca.objects.count()
>>>>>>> fc8ba0a41a8635567d5705060d161bf95028d91e
    context = {
        'total_clientes': total_clientes,
        'total_vehiculos': total_vehiculos,
        'total_marcas': total_marcas,
<<<<<<< HEAD
        'clientes': clientes,
        'vehiculos': vehiculos,
    }
    return render(request, 'concesionario/index.html', context)
=======
    }
    return render(request, 'index.html', context)
>>>>>>> fc8ba0a41a8635567d5705060d161bf95028d91e


def marca_list(request):
    marcas = Marca.objects.all()
    return render(request, 'concesionario/marca_list.html', {'marcas': marcas})

def vehiculo_list(request):
<<<<<<< HEAD
    queryset = Vehiculo.objects.all()
    
    # Obtener los filtros
    filtros = {
        'modelo': request.GET.get('modelo', ''),
        'marca': request.GET.get('marca', ''),
        'precio_min': request.GET.get('precio_min', ''),
        'precio_max': request.GET.get('precio_max', ''),
        'año': request.GET.get('año', '')
    }

    # Aplicar filtros
    if filtros['modelo']:
        queryset = queryset.filter(modelo__icontains=filtros['modelo'])
    
    if filtros['marca']:
        queryset = queryset.filter(marca__nombre=filtros['marca'])

    # Procesar y aplicar filtros de precio
    try:
        if filtros['precio_min']:
            precio_min = int(filtros['precio_min'].replace('.', ''))
            queryset = queryset.filter(precio__gte=precio_min)
        
        if filtros['precio_max']:
            precio_max = int(filtros['precio_max'].replace('.', ''))
            queryset = queryset.filter(precio__lte=precio_max)
    except ValueError:
        # Manejar el caso de valores no numéricos
        pass

    if filtros['año']:
        queryset = queryset.filter(año=filtros['año'])

    # Obtener todas las marcas para el selector
    marcas = Marca.objects.all()

    context = {
        'vehiculos': queryset,
        'marcas': marcas,
        'filtros': filtros
    }

    return render(request, 'concesionario/vehiculo_list.html', context)
=======
    vehiculos = Vehiculo.objects.all()
    return render(request, 'concesionario/vehiculo_list.html', {'vehiculos': vehiculos})
>>>>>>> fc8ba0a41a8635567d5705060d161bf95028d91e

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


from django.shortcuts import render, redirect, get_object_or_404
from .models import Marca
from .forms import MarcaForm

def marca_create(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('marca_list')
    else:
        form = MarcaForm()
    return render(request, 'concesionario/marca_form.html', {'form': form})

def marca_update(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == 'POST':
        form = MarcaForm(request.POST, request.FILES, instance=marca)
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

def marca_confirm_delete(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == 'POST':
        marca.delete()
        return redirect('marca_list')
    return render(request, 'concesionario/marca_confirm_delete.html', {'marca': marca})


<<<<<<< HEAD
# Vistas para Vehiculo
def vehiculo_list(request):
    queryset = Vehiculo.objects.all()
    
    # Obtener los filtros
    filtros = {
        'modelo': request.GET.get('modelo', ''),
        'marca': request.GET.get('marca', ''),
        'precio_min': request.GET.get('precio_min', ''),
        'precio_max': request.GET.get('precio_max', ''),
        'año': request.GET.get('año', '')
    }

    # Aplicar filtros
    if filtros['modelo']:
        queryset = queryset.filter(modelo__icontains=filtros['modelo'])
    
    if filtros['marca']:
        queryset = queryset.filter(marca__nombre=filtros['marca'])

    # Procesar y aplicar filtros de precio
    try:
        if filtros['precio_min']:
            precio_min = int(filtros['precio_min'].replace('.', ''))
            queryset = queryset.filter(precio__gte=precio_min)
        
        if filtros['precio_max']:
            precio_max = int(filtros['precio_max'].replace('.', ''))
            queryset = queryset.filter(precio__lte=precio_max)
    except ValueError:
        # Manejar el caso de valores no numéricos
        pass

    if filtros['año']:
        queryset = queryset.filter(año=filtros['año'])

    # Obtener todas las marcas para el selector
    marcas = Marca.objects.all()

    context = {
        'vehiculos': queryset,
        'marcas': marcas,
        'filtros': filtros
    }

    return render(request, 'concesionario/vehiculo_list.html', context)
=======

# Otras vistas...

# Vistas para Vehiculo
def vehiculo_list(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'concesionario/vehiculo_list.html', {'vehiculos': vehiculos})
>>>>>>> fc8ba0a41a8635567d5705060d161bf95028d91e

def vehiculo_create(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
<<<<<<< HEAD
        try:
            if form.is_valid():
                vehiculo = form.save(commit=False)
                precio_str = request.POST.get('precio', '0')
                # Limpiar el precio de puntos y convertir a entero
                precio_limpio = precio_str.replace('.', '')
                vehiculo.precio = int(precio_limpio)
                vehiculo.save()
                return redirect('vehiculo_list')
        except Exception as e:
            print("Error al guardar:", str(e))
            form.add_error('precio', 'Error al procesar el precio')
=======
        if form.is_valid():
            form.save()
            return redirect('vehiculo_list')
>>>>>>> fc8ba0a41a8635567d5705060d161bf95028d91e
    else:
        form = VehiculoForm()
    return render(request, 'concesionario/vehiculo_form.html', {'form': form})

def vehiculo_update(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
<<<<<<< HEAD
    print("Hola mundo")
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        try:
            if form.is_valid():
                vehiculo = form.save(commit=False)
                precio_str = request.POST.get('precio', '0')
                precio_limpio = precio_str.replace('.', '')
                vehiculo.precio = int(precio_limpio)
                vehiculo.save()
                print(f"Precio: {vehiculo.precio}")
                return redirect('vehiculo_list')
        except Exception as e:
            print("Error al guardar:", str(e))
            form.add_error('precio', 'Error al procesar el precio')
=======
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('vehiculo_list')
>>>>>>> fc8ba0a41a8635567d5705060d161bf95028d91e
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