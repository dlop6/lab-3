# Modelo de Base de Datos

## Tablas
### Libro
- **id**: Clave primaria.
- **titulo**: Nombre del libro (no nulo).
- **isbn**: Código único de 13 dígitos.
- **año_public**: Año validado con `tipo_fecha`.
- **rating**: Calificación de 1 a 5 (`tipo_rating`).
- **genero_id**: Clave foránea a Género.

### Autor
- **id**: Clave primaria.
- **nombre**: Nombre del autor (no nulo).
- **nacionalidad**: Opcional.

### Género
- **id**: Clave primaria.
- **nombre**: Nombre único (ej: "Ciencia Ficción").

## Relaciones
- Un libro puede tener **múltiples autores** (tabla `libro_autor`).
- Un libro pertenece a **un género**.