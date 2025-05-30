-- Datos iniciales para la base de datos biblioteca_orm
-- Generado automáticamente desde SQLAlchemy

-- AUTORES
INSERT INTO autores (id, nombre, nacionalidad) VALUES (1, 'Gabriel García Márquez', 'Colombiano');
INSERT INTO autores (id, nombre, nacionalidad) VALUES (2, 'J.K. Rowling', 'Británica');
INSERT INTO autores (id, nombre, nacionalidad) VALUES (3, 'Stephen King', 'Estadounidense');
INSERT INTO autores (id, nombre, nacionalidad) VALUES (4, 'Mario Vargas Llosa', 'Peruano');
INSERT INTO autores (id, nombre, nacionalidad) VALUES (5, 'Isabel Allende', 'Chilena');

-- GÉNEROS
INSERT INTO generos (id, nombre, tipo) VALUES (1, 'Realismo mágico', 'ficcion');
INSERT INTO generos (id, nombre, tipo) VALUES (2, 'Fantasía', 'ficcion');
INSERT INTO generos (id, nombre, tipo) VALUES (3, 'Terror', 'ficcion');
INSERT INTO generos (id, nombre, tipo) VALUES (4, 'Biografía', 'no_ficcion');
INSERT INTO generos (id, nombre, tipo) VALUES (5, 'Ciencia Ficción', 'ficcion');
INSERT INTO generos (id, nombre, tipo) VALUES (6, 'Histórica', 'ficcion');

-- LIBROS
INSERT INTO libros (id, titulo, isbn, fecha_publicacion, precio, estado) VALUES (1, 'Cien años de soledad', '9780307350428', '1967-05-30', 25.99, 'disponible');
INSERT INTO libros (id, titulo, isbn, fecha_publicacion, precio, estado) VALUES (2, 'Harry Potter y la piedra filosofal', '9788478884452', '1997-06-26', 19.99, 'disponible');
INSERT INTO libros (id, titulo, isbn, fecha_publicacion, precio, estado) VALUES (3, 'It', '9780450411434', '1986-09-15', 22.50, 'prestado');
INSERT INTO libros (id, titulo, isbn, fecha_publicacion, precio, estado) VALUES (4, 'La ciudad y los perros', '9788437601965', '1963-10-10', 20.00, 'disponible');
INSERT INTO libros (id, titulo, isbn, fecha_publicacion, precio, estado) VALUES (5, 'La casa de los espíritus', '9788401359250', '1982-01-01', 18.75, 'disponible');

-- RELACIONES LIBRO-AUTOR
INSERT INTO libro_autor (libro_id, autor_id, rol) VALUES (1, 1, 'Principal');
INSERT INTO libro_autor (libro_id, autor_id, rol) VALUES (2, 2, 'Principal');
INSERT INTO libro_autor (libro_id, autor_id, rol) VALUES (3, 3, 'Principal');
INSERT INTO libro_autor (libro_id, autor_id, rol) VALUES (4, 4, 'Principal');
INSERT INTO libro_autor (libro_id, autor_id, rol) VALUES (5, 5, 'Principal');
INSERT INTO libro_autor (libro_id, autor_id, rol) VALUES (1, 5, 'Influencia');

-- RELACIONES LIBRO-GÉNERO
INSERT INTO libro_genero (libro_id, genero_id) VALUES (1, 1);
INSERT INTO libro_genero (libro_id, genero_id) VALUES (2, 2);
INSERT INTO libro_genero (libro_id, genero_id) VALUES (3, 3);
INSERT INTO libro_genero (libro_id, genero_id) VALUES (4, 6);
INSERT INTO libro_genero (libro_id, genero_id) VALUES (5, 1);
INSERT INTO libro_genero (libro_id, genero_id) VALUES (1, 6);

-- FIN DE LOS DATOS INICIALES
