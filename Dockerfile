# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo Python a la imagen de Docker
COPY edad.py /app

# Comando por defecto para ejecutar el programa
CMD ["python", "edad.py"]