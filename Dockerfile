FROM python:3.10-alpine

# Instala cliente Postgres, bash y dos2unix
RUN apk update \
 && apk add --no-cache \
      postgresql-client \
      bash \
      dos2unix

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código y convierte el script a Unix line endings
COPY . .
RUN dos2unix scripts/wait-for-db.sh \
 && chmod +x scripts/wait-for-db.sh

CMD ["./scripts/wait-for-db.sh", "db", "python3", "models.py"]
