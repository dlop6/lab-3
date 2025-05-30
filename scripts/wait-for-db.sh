#!/bin/sh
set -e

host="$1"
shift

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$host" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
  >&2 echo "PostgreSQL no está disponible - esperando..."
  sleep 100
done

>&2 echo "PostgreSQL está listo - ejecutando comando"
exec "$@"
