from django import forms
from .models import Concesionario, Marca, Cliente, Venta

class ConcesionarioForm(forms.ModelForm):
    class Meta:
        model = Concesionario
        fields = ['nombre', 'direccion']

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['concesionario', 'marca', 'cliente', 'fecha']