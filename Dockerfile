# Usa la imagen base de Python 3.10 con Alpine Linux
FROM python:3.10-alpine

# Actualiza los paquetes e instala el cliente de PostgreSQL y bash
RUN apk update \
 && apk add --no-cache \
      postgresql-client \
      bash

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de dependencias
COPY requirements.txt .
# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos al contenedor
COPY . .
# Da permisos de ejecución al script de espera de la base de datos
RUN chmod +x scripts/wait-for-db.sh

# Comando por defecto: espera a la base de datos y luego ejecuta models.py
CMD ["./scripts/wait-for-db.sh", "db", "python3", "models.py"]
