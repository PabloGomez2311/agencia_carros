from django import forms
from .models import Marca, Vehiculo, Cliente

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre', 'pais_origen', 'logo', 'bandera']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre de la marca'
            }),
            'pais_origen': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el país de origen'
            }),
            'logo': forms.FileInput(attrs={
                'class': 'custom-file-input',
                'accept': 'image/*'
            }),
            'bandera': forms.FileInput(attrs={
                'class': 'custom-file-input',
                'accept': 'image/*'
            }),
        }

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['modelo', 'color', 'año', 'precio', 'disponibilidad', 'marca']
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control precio-input',
                'type': 'text'
            }),
            'disponibilidad': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'contacto', 'correo_electronico', 'vehiculo']
        labels = {
            'vehiculo': 'Vehículo'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control border-dark',
                'placeholder': 'Ingrese el nombre completo',
            }),
            'contacto': forms.TextInput(attrs={
                'class': 'form-control border-dark',
                'placeholder': 'Ingrese el número de contacto',
                'maxlength': '10',
                'pattern': '[0-9]*',
                'title': 'Por favor ingrese solo números (máximo 10 dígitos)',
                'oninput': 'this.value = this.value.replace(/[^0-9]/g, "")',
            }),
            'correo_electronico': forms.EmailInput(attrs={
                'class': 'form-control border-dark',
                'placeholder': 'ejemplo@correo.com',
            }),
            'vehiculo': forms.Select(attrs={
                'class': 'form-control border-dark',
            }),
        }