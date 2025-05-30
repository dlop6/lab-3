from database import engine, Base
from models import Libro, Autor, Genero, EstadoLibro, TipoGenero

def init_db():
    print("Creando tablas...")
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas exitosamente")

if __name__ == "__main__":
    init_db()