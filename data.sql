-- Insertar géneros
INSERT INTO genero (nombre) VALUES 
('Ciencia Ficción'),
('Fantasía'),
('Terror'),
('Romance'),
('Aventura'),
('Misterio'),
('Drama'),
('Histórico'),
('Biografía'),
('Poesía');

-- Insertar autores
INSERT INTO autor (nombre, nacionalidad) VALUES 
('J.K. Rowling', 'Británica'),
('George R.R. Martin', 'Estadounidense'),
('Stephen King', 'Estadounidense'),
('Isabel Allende', 'Chilena'),
('Gabriel García Márquez', 'Colombiano'),
('Haruki Murakami', 'Japonés'),
('Jane Austen', 'Británica'),
('Agatha Christie', 'Británica'),
('J.R.R. Tolkien', 'Británico'),
('Dan Brown', 'Estadounidense');

-- Insertar libros y relaciones
INSERT INTO libro (titulo, isbn, año_public, rating, genero_id) VALUES 
('Harry Potter 1', '1234567890123', 1997, '5', 2),
('Juego de Tronos', '2345678901234', 1996, '4', 2),
('El Resplandor', '3456789012345', 1977, '5', 3),
('Cien Años de Soledad', '4567890123456', 1967, '5', 7),
('Kafka en la Orilla', '5678901234567', 2002, '4', 1),
('Orgullo y Prejuicio', '6789012345678', 1813, '5', 4),
('El Hobbit', '7890123456789', 1937, '5', 2),
('Los Pilares de la Tierra', '8901234567890', 1989, '4', 8),
('La Sombra del Viento', '9012345678901', 2001, '5', 6),
('El Código Da Vinci', '0123456789012', 2003, '4', 6);

-- 10 libros más
INSERT INTO libro (titulo, isbn, año_public, rating, genero_id) VALUES 
('Crónica de una Muerte Anunciada', '1123456789012', 1981, '4', 7),
('La Casa de los Espíritus', '1223456789012', 1982, '5', 7),
('Carrie', '1323456789012', 1974, '4', 3),
('Matar a un Ruiseñor', '1423456789012', 1960, '5', 7),
('El Gran Gatsby', '1523456789012', 1925, '4', 7),
('1984', '1623456789012', 1949, '5', 1),
('El Señor de los Anillos', '1723456789012', 1954, '5', 2),
('Asesinato en el Orient Express', '1823456789012', 1934, '4', 6),
('Rayuela', '1923456789012', 1963, '4', 7),
('El Amor en los Tiempos del Cólera', '2023456789012', 1985, '5', 4);

-- 10 libros más
INSERT INTO libro (titulo, isbn, año_public, rating, genero_id) VALUES 
('Don Quijote de la Mancha', '2123456789012', 1605, '5', 5),
('La Odisea', '2223456789012', -800, '5', 5),
('Hamlet', '2323456789012', 1603, '5', 7),
('Drácula', '2423456789012', 1897, '4', 3),
('Frankenstein', '2523456789012', 1818, '4', 3),
('El Principito', '2623456789012', 1943, '5', 5),
('La Metamorfosis', '2723456789012', 1915, '4', 7),
('Fahrenheit 451', '2823456789012', 1953, '4', 1),
('Crimen y Castigo', '2923456789012', 1866, '5', 7),
('Poemas de Pablo Neruda', '3023456789012', 1950, '5', 10);

-- Relacionar libros con autores (al menos 30 relaciones)
INSERT INTO libro_autor (libro_id, autor_id) VALUES 
(1, 1), (1, 2),
(2, 2), (2, 3),
(3, 3), (3, 1),
(4, 5), (4, 4),
(5, 6), (5, 2),
(6, 7), (6, 1),
(7, 9), (7, 2),
(8, 4), (8, 5),
(9, 4), (9, 8),
(10, 10), (10, 8),
(11, 5), (11, 4),
(12, 4), (12, 5),
(13, 3), (13, 2),
(14, 7), (14, 1),
(15, 7), (15, 8),
(16, 2), (16, 6),
(17, 9), (17, 2),
(18, 8), (18, 10),
(19, 5), (19, 4),
(20, 5), (20, 4),
(21, 4), (21, 5),
(22, 4), (22, 5),
(23, 7), (23, 8),
(24, 3), (24, 2),
(25, 3), (25, 2),
(26, 4), (26, 5),
(27, 5), (27, 6),
(28, 2), (28, 6),
(29, 5), (29, 4),
(30, 4), (30, 5);