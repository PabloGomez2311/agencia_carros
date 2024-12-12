from django import forms
from .models import Vehiculo, Marca, Cliente

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['modelo', 'color', 'año', 'precio', 'disponibilidad', 'marca']
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'disponibilidad': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
        }

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre', 'pais_origen', 'logo', 'bandera']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'pais_origen': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
            'bandera': forms.FileInput(attrs={'class': 'form-control'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'contacto', 'correo_electronico', 'vehiculo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
            'vehiculo': forms.Select(attrs={'class': 'form-control'}),
        }
