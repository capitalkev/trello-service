# Usa una imagen oficial de Python ligera
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Evita que Python genere archivos .pyc y fuerza a que los logs se muestren en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copia solo el archivo de requerimientos primero (aprovecha la caché de Docker)
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código fuente (la carpeta src)
COPY src/ ./src/

# Expone el puerto que usará Cloud Run (por defecto 8080)
EXPOSE 8080

# Comando para ejecutar la aplicación (Usamos el puerto 8080 para Cloud Run)
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]