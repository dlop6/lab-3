-- TIPOS ENUM PERSONALIZADOS
CREATE TYPE estadolibro AS ENUM ('disponible', 'prestado', 'en_reparacion');
CREATE TYPE tipogenero AS ENUM ('ficcion', 'no_ficcion', 'academico');

-- TABLAS

CREATE TABLE autores (
	id SERIAL NOT NULL, 
	nombre VARCHAR(50) NOT NULL, 
	nacionalidad VARCHAR(30), 
	PRIMARY KEY (id)
)

;

CREATE INDEX ix_autores_id ON autores (id);


CREATE TABLE generos (
	id SERIAL NOT NULL, 
	nombre VARCHAR(30) NOT NULL, 
	tipo tipogenero NOT NULL, 
	PRIMARY KEY (id)
)

;

CREATE INDEX ix_generos_id ON generos (id);


CREATE TABLE libros (
	id SERIAL NOT NULL, 
	titulo VARCHAR(100) NOT NULL, 
	isbn VARCHAR(20) NOT NULL, 
	fecha_publicacion DATE, 
	precio NUMERIC(10, 2) CHECK (precio >= 0), 
	estado estadolibro NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (isbn)
)

;

CREATE INDEX ix_libros_id ON libros (id);


CREATE TABLE libro_autor (
	libro_id INTEGER NOT NULL, 
	autor_id INTEGER NOT NULL, 
	rol VARCHAR(30), 
	PRIMARY KEY (libro_id, autor_id), 
	FOREIGN KEY(libro_id) REFERENCES libros (id), 
	FOREIGN KEY(autor_id) REFERENCES autores (id)
)

;



CREATE TABLE libro_genero (
	libro_id INTEGER NOT NULL, 
	genero_id INTEGER NOT NULL, 
	PRIMARY KEY (libro_id, genero_id), 
	FOREIGN KEY(libro_id) REFERENCES libros (id), 
	FOREIGN KEY(genero_id) REFERENCES generos (id)
)

;


-- FIN DEL SCHEMA
