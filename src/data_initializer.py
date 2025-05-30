from database import SessionLocal
from models import Libro, Autor, Genero, LibroAutor, LibroGenero, EstadoLibro, TipoGenero
from datetime import date

def init_data():
    db = SessionLocal()
    
    try:
        # Limpiar tablas
        db.query(LibroAutor).delete()
        db.query(LibroGenero).delete()
        db.query(Libro).delete()
        db.query(Autor).delete()
        db.query(Genero).delete()
        db.commit()
        # Autores
        autores = [
            Autor(nombre="Gabriel García Márquez", nacionalidad="Colombiano"),
            Autor(nombre="J.K. Rowling", nacionalidad="Británica"),
            Autor(nombre="Stephen King", nacionalidad="Estadounidense")
        ]
        db.add_all(autores)
        db.commit()

        # Géneros
        generos = [
            Genero(nombre="Realismo mágico", tipo=TipoGenero.FICCION),
            Genero(nombre="Fantasía", tipo=TipoGenero.FICCION),
            Genero(nombre="Terror", tipo=TipoGenero.FICCION),
            Genero(nombre="Biografía", tipo=TipoGenero.NO_FICCION)
        ]
        db.add_all(generos)
        db.commit()

        # Libros
        libros = [
            Libro(
                titulo="Cien años de soledad",
                isbn="9780307350428",
                fecha_publicacion=date(1967, 5, 30),
                precio=25.99,
                estado=EstadoLibro.DISPONIBLE
            ),
            Libro(
                titulo="Harry Potter y la piedra filosofal",
                isbn="9788478884452",
                fecha_publicacion=date(1997, 6, 26),
                precio=19.99,
                estado=EstadoLibro.DISPONIBLE
            ),
            Libro(
                titulo="It",
                isbn="9780450411434",
                fecha_publicacion=date(1986, 9, 15),
                precio=22.50,
                estado=EstadoLibro.PRESTADO
            )
        ]
        db.add_all(libros)
        db.commit()

        # Obtener IDs reales
        libro1 = db.query(Libro).filter_by(titulo="Cien años de soledad").first()
        libro2 = db.query(Libro).filter_by(titulo="Harry Potter y la piedra filosofal").first()
        libro3 = db.query(Libro).filter_by(titulo="It").first()
        autor1 = db.query(Autor).filter_by(nombre="Gabriel García Márquez").first()
        autor2 = db.query(Autor).filter_by(nombre="J.K. Rowling").first()
        autor3 = db.query(Autor).filter_by(nombre="Stephen King").first()
        genero1 = db.query(Genero).filter_by(nombre="Realismo mágico").first()
        genero2 = db.query(Genero).filter_by(nombre="Fantasía").first()
        genero3 = db.query(Genero).filter_by(nombre="Terror").first()

        # Relaciones
        db.add_all([
            LibroAutor(libro_id=libro1.id, autor_id=autor1.id, rol="Principal"),
            LibroAutor(libro_id=libro2.id, autor_id=autor2.id, rol="Principal"),
            LibroAutor(libro_id=libro3.id, autor_id=autor3.id, rol="Principal"),
            LibroGenero(libro_id=libro1.id, genero_id=genero1.id),
            LibroGenero(libro_id=libro2.id, genero_id=genero2.id),
            LibroGenero(libro_id=libro3.id, genero_id=genero3.id)
        ])
        
        db.commit()
        print("Datos iniciales insertados exitosamente")
        
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    init_data()