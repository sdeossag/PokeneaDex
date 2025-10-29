# Imagen base ligera de Python
FROM python:3.11-slim

# Evita que Python guarde archivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
# Asegura que los logs se impriman directamente
ENV PYTHONUNBUFFERED=1

# Crea el directorio de trabajo
WORKDIR /app

# Copia los archivos de dependencias
COPY requirements.txt .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el proyecto dentro del contenedor
COPY . .

# Expone el puerto 5000 (donde Flask corre)
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "run.py"]
