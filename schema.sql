CREATE TYPE tipo_rating AS ENUM ('1', '2', '3', '4', '5');

CREATE TABLE IF NOT EXISTS genero (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(20) UNIQUE NOT NULL
);

-- Añadir restricción CHECK al año_public en la tabla libro
ALTER TABLE libro ADD CONSTRAINT check_año CHECK (año_public <= EXTRACT(YEAR FROM CURRENT_DATE));