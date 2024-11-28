# Generated by Django 5.1.1 on 2024-10-30 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concesionario', '0002_remove_venta_concesionario_remove_venta_cliente_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='bandera',
            field=models.ImageField(blank=True, null=True, upload_to='banderas/'),
        ),
        migrations.AddField(
            model_name='marca',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='marcas/'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='precio',
            field=models.DecimalField(decimal_places=0, max_digits=14),
        ),
    ]
