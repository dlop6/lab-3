from database import SessionLocal
from models import Libro, Autor, Genero, LibroAutor, LibroGenero, EstadoLibro, TipoGenero
from datetime import date

def generate_data_sql():
    with open('scripts/data.sql', 'w', encoding='utf-8') as f:
        # Encabezado del archivo
        f.write("-- Datos iniciales para la base de datos biblioteca_orm\n")
        f.write("-- Generado automáticamente desde SQLAlchemy\n\n")
        
        # Insertar autores
        f.write("-- AUTORES\n")
        autores = [
            (1, "'Gabriel García Márquez'", "'Colombiano'"),
            (2, "'J.K. Rowling'", "'Británica'"),
            (3, "'Stephen King'", "'Estadounidense'"),
            (4, "'Mario Vargas Llosa'", "'Peruano'"),
            (5, "'Isabel Allende'", "'Chilena'")
        ]
        for id, nombre, nacionalidad in autores:
            f.write(f"INSERT INTO autores (id, nombre, nacionalidad) VALUES ({id}, {nombre}, {nacionalidad});\n")
        f.write("\n")
        
        # Insertar géneros
        f.write("-- GÉNEROS\n")
        generos = [
            (1, "'Realismo mágico'", "'ficcion'"),
            (2, "'Fantasía'", "'ficcion'"),
            (3, "'Terror'", "'ficcion'"),
            (4, "'Biografía'", "'no_ficcion'"),
            (5, "'Ciencia Ficción'", "'ficcion'"),
            (6, "'Histórica'", "'ficcion'")
        ]
        for id, nombre, tipo in generos:
            f.write(f"INSERT INTO generos (id, nombre, tipo) VALUES ({id}, {nombre}, {tipo});\n")
        f.write("\n")
        
        # Insertar libros
        f.write("-- LIBROS\n")
        libros = [
            (1, "'Cien años de soledad'", "'9780307350428'", "'1967-05-30'", "25.99", "'disponible'"),
            (2, "'Harry Potter y la piedra filosofal'", "'9788478884452'", "'1997-06-26'", "19.99", "'disponible'"),
            (3, "'It'", "'9780450411434'", "'1986-09-15'", "22.50", "'prestado'"),
            (4, "'La ciudad y los perros'", "'9788437601965'", "'1963-10-10'", "20.00", "'disponible'"),
            (5, "'La casa de los espíritus'", "'9788401359250'", "'1982-01-01'", "18.75", "'disponible'")
        ]
        for id, titulo, isbn, fecha, precio, estado in libros:
            f.write(f"INSERT INTO libros (id, titulo, isbn, fecha_publicacion, precio, estado) VALUES ({id}, {titulo}, {isbn}, {fecha}, {precio}, {estado});\n")
        f.write("\n")
        
        # Insertar relaciones libro-autor
        f.write("-- RELACIONES LIBRO-AUTOR\n")
        relaciones_autor = [
            (1, 1, "'Principal'"),
            (2, 2, "'Principal'"),
            (3, 3, "'Principal'"),
            (4, 4, "'Principal'"),
            (5, 5, "'Principal'"),
            (1, 5, "'Influencia'")
        ]
        for libro_id, autor_id, rol in relaciones_autor:
            f.write(f"INSERT INTO libro_autor (libro_id, autor_id, rol) VALUES ({libro_id}, {autor_id}, {rol});\n")
        f.write("\n")
        
        # Insertar relaciones libro-genero
        f.write("-- RELACIONES LIBRO-GÉNERO\n")
        relaciones_genero = [
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 6),
            (5, 1),
            (1, 6)
        ]
        for libro_id, genero_id in relaciones_genero:
            f.write(f"INSERT INTO libro_genero (libro_id, genero_id) VALUES ({libro_id}, {genero_id});\n")
        
        f.write("\n-- FIN DE LOS DATOS INICIALES\n")
    
    print("data.sql generado correctamente en scripts/data.sql")

if __name__ == "__main__":
    generate_data_sql()