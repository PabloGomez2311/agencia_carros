# Generated by Django 5.1.1 on 2024-11-28 09:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('pais_origen', models.CharField(default='Desconocido', max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='marcas/')),
                ('bandera', models.ImageField(blank=True, null=True, upload_to='banderas/')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('año', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=0, max_digits=14)),
                ('disponibilidad', models.BooleanField(default=True)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concesionario.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('contacto', models.CharField(default='N/A', max_length=100)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('vehiculo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='concesionario.vehiculo')),
            ],
        ),
    ]
