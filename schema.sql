-- Tipos personalizados
CREATE TYPE tipo_rating AS ENUM ('1', '2', '3', '4', '5');
CREATE TYPE tipo_estado AS ENUM ('borrador', 'publicado', 'archivado');

CREATE TABLE IF NOT EXISTS genero (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(20) UNIQUE NOT NULL
);

-- Tabla autor
CREATE TABLE IF NOT EXISTS autor (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    nacionalidad VARCHAR(30) NOT NULL
);

-- Tabla libro
CREATE TABLE IF NOT EXISTS libro (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    isbn VARCHAR(13) UNIQUE NOT NULL,
    año_public INTEGER,
    rating tipo_rating NOT NULL,
    estado tipo_estado NOT NULL DEFAULT 'publicado',
    genero_id INTEGER NOT NULL REFERENCES genero(id),
    CONSTRAINT check_año CHECK (año_public <= EXTRACT(YEAR FROM CURRENT_DATE))
);

-- Tabla intermedia libro_autor
CREATE TABLE IF NOT EXISTS libro_autor (
    libro_id INTEGER NOT NULL REFERENCES libro(id),
    autor_id INTEGER NOT NULL REFERENCES autor(id),
    PRIMARY KEY (libro_id, autor_id)
);

-- Vista para libros con autores y género
CREATE OR REPLACE VIEW vista_libros_autores AS
SELECT
    l.id AS libro_id,
    l.titulo,
    l.isbn,
    l.rating,
    l.estado,
    g.nombre AS genero,
    STRING_AGG(a.nombre, ', ') AS autores
FROM libro l
JOIN genero g ON l.genero_id = g.id
JOIN libro_autor la ON l.id = la.libro_id
JOIN autor a ON la.autor_id = a.id
GROUP BY l.id, g.nombre, l.estado;