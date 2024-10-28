from django.contrib import admin
from django.urls import path
from concesionario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('vehiculos/', views.vehiculo_list, name='vehiculo_list'),
    path('vehiculos/create/', views.vehiculo_create, name='vehiculo_create'),
    path('vehiculos/<int:pk>/update/', views.vehiculo_update, name='vehiculo_update'),
    path('vehiculos/<int:pk>/delete/', views.vehiculo_delete, name='vehiculo_delete'),
    path('marcas/', views.marca_list, name='marca_list'),
    path('marcas/create/', views.marca_create, name='marca_create'),
    path('marcas/<int:pk>/update/', views.marca_update, name='marca_update'),
    path('marcas/<int:pk>/delete/', views.marca_delete, name='marca_delete'),
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/create/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/update/', views.cliente_update, name='cliente_update'),
    path('clientes/<int:pk>/delete/', views.cliente_delete, name='cliente_delete'),
]