--psql -U postgres -d biblioteca_orm -f scripts/views.sql

-- Vista para el reporte completo de libros
CREATE OR REPLACE VIEW vista_libros_completos AS
SELECT 
    l.id,
    l.titulo,
    l.isbn,
    l.estado,
    string_agg(DISTINCT a.nombre, ', ' ORDER BY a.nombre) AS autores,
    string_agg(DISTINCT g.nombre, ', ' ORDER BY g.nombre) AS generos
FROM 
    libros l
LEFT JOIN libro_autor la ON l.id = la.libro_id
LEFT JOIN autores a ON la.autor_id = a.id
LEFT JOIN libro_genero lg ON l.id = lg.libro_id
LEFT JOIN generos g ON lg.genero_id = g.id
GROUP BY l.id;