from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100, default='Desconocido')
    logo = models.ImageField(upload_to='marcas/', blank=True, null=True)
    bandera = models.ImageField(upload_to='banderas/', blank=True, null=True)
<<<<<<< HEAD
    
=======

>>>>>>> fc8ba0a41a8635567d5705060d161bf95028d91e
    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    año = models.IntegerField()
<<<<<<< HEAD
    precio = models.BigIntegerField()
=======
    precio = models.DecimalField(max_digits=14, decimal_places=0)  # Permite hasta 14 dígitos enteros
>>>>>>> fc8ba0a41a8635567d5705060d161bf95028d91e
    disponibilidad = models.BooleanField(default=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.modelo} ({self.marca.nombre})"

    @property
    def precio_formateado(self):
        """Retorna el precio con puntos como separadores de miles."""
<<<<<<< HEAD
        return f"{self.precio:,}".replace(',', '.')
=======
        return f"{self.precio:,.0f}".replace(",", ".")  # Cambia comas por puntos
>>>>>>> fc8ba0a41a8635567d5705060d161bf95028d91e

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100, default='N/A')
    correo_electronico = models.EmailField()
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre