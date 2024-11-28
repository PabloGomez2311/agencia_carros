# Usa una imagen base de Python 3.11.9
FROM python:3.11.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de tu proyecto al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expone el puerto en el que tu aplicación correrá
EXPOSE 8000

# Comando para correr tu aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]