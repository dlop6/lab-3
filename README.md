# Laboratorio 3 - Sistema de Gestión de Biblioteca

## Requisitos previos
- PostgreSQL 17 instalado y en ejecución
- Python 3.8+

## Configuración inicial

1. **Configurar la base de datos**:
```bash
psql -U postgres -c "CREATE DATABASE biblioteca_orm;"
```

2. **Instalar las dependencias**
```bash
pip install requirements.txt
```

## Ejecución paso a paso

1. **Crear la estructura de la base de datos**
```bash
python src/seed.py
```

2. **Poblar los datos iniciales**
```bash
python src/data_initializer.py
```
3. **Crear la vista**
```bash
python src/views.py
```
o
```bash
--psql -U postgres -d biblioteca_orm -f scripts/views.sql
```

4. **Correr el programa**
```bash
python src/main.py
```

## Comandos útiles
Reiniciar completamente la BD:

```bash
psql -U postgres -c "DROP DATABASE biblioteca_orm;"
psql -U postgres -c "CREATE DATABASE biblioteca_orm;"
```
Generar archivos SQL:

```bash
python scripts/generate_schema.py  # Genera schema.sql
python scripts/generate_data.py    # Genera data.sql
```
## Estructura del proyecto
biblioteca_orm/
├── src/
│   ├── models.py         # Modelos SQLAlchemy
│   ├── database.py       # Configuración DB
│   ├── seed.py           # Crea tablas
│   ├── data_initializer.py # Datos demo
│   ├── views.py          # Vistas SQL
│   └── main.py           # CLI principal
├── scripts/
│   ├── schema.sql        # DDL generado
│   ├── data.sql          # Datos demo
│   └── views.sql         # SQL de vistas
├── .env                  # Configuración
└── requirements.txt      # Dependencias

