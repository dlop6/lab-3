# Dockerfile (Alpine-based, sin apt ni sources list)

# 1) Partimos de Python 3.10 Alpine
FROM python:3.10-alpine

# 2) Instalamos el cliente psql y bash (necesario para tu script)
RUN apk update \
 && apk add --no-cache \
      postgresql-client \
      bash

# 3) Directorio de trabajo
WORKDIR /app

# 4) Copiamos e instalamos dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5) Copiamos todo el código y damos permiso de ejecución al script
COPY . .
RUN chmod +x scripts/wait-for-db.sh

# 6) Comando por defecto: espera a DB y crea tablas
CMD ["./scripts/wait-for-db.sh", "db", "python", "models.py"]
