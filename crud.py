from sqlalchemy.orm import Session
from models import Libro, Autor, Genero

# Crear un libro
def crear_libro(session: Session, titulo, isbn, año_public, rating, genero_id, autor_ids):
    nuevo_libro = Libro(
        titulo=titulo,
        isbn=isbn,
        año_public=año_public,
        rating=rating,
        genero_id=genero_id
    )
    # Agregar autores relacionados
    nuevo_libro.autores = session.query(Autor).filter(Autor.id.in_(autor_ids)).all()

    session.add(nuevo_libro)
    session.commit()
    session.refresh(nuevo_libro)
    return nuevo_libro

# Leer todos los libros
def obtener_libros(session: Session):
    return session.query(Libro).all()

# Editar un libro
def editar_libro(session: Session, libro_id, nuevos_datos):
    libro = session.query(Libro).filter_by(id=libro_id).first()
    if not libro:
        return None
    for key, value in nuevos_datos.items():
        setattr(libro, key, value)
    session.commit()
    return libro

# Eliminar un libro
def eliminar_libro(session: Session, libro_id):
    libro = session.query(Libro).filter_by(id=libro_id).first()
    if libro:
        session.delete(libro)
        session.commit()
