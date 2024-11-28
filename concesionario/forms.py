from django import forms
from .models import Marca, Vehiculo, Cliente

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre', 'pais_origen', 'logo', 'bandera']
        widgets = {
<<<<<<< HEAD
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
=======
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'pais_origen': forms.TextInput(attrs={'class': 'form-control'}),
>>>>>>> fc8ba0a41a8635567d5705060d161bf95028d91e
        }

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['modelo', 'color', 'año', 'precio', 'disponibilidad', 'marca']
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
<<<<<<< HEAD
            'precio': forms.NumberInput(attrs={
                'class': 'form-control precio-input',
                'type': 'text'
            }),
=======
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
>>>>>>> fc8ba0a41a8635567d5705060d161bf95028d91e
            'disponibilidad': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'contacto', 'correo_electronico', 'vehiculo']
<<<<<<< HEAD
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
=======
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
            'vehiculo': forms.Select(attrs={'class': 'form-control'}),
>>>>>>> fc8ba0a41a8635567d5705060d161bf95028d91e
        }