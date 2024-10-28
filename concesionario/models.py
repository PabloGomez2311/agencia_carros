from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100, default='Desconocido')  # Agrega un valor predeterminado aquí

    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    año = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad = models.BooleanField(default=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.modelo} ({self.marca.nombre})"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100, default='N/A')
    correo_electronico = models.EmailField()
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre