from django.contrib import admin
from django.urls import path
from concesionario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Ruta para la URL raíz
    path('index/', views.index, name='index'),  # Ruta explícita para /index
]