from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, CheckConstraint
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.dialects.postgresql import ENUM
import os

# Configuración de la base de datos
db_user = os.getenv("POSTGRES_USER", "postgres")
db_password = os.getenv("POSTGRES_PASSWORD", "postgres")
db_host = os.getenv("DB_HOST", "localhost")
db_name = os.getenv("POSTGRES_DB", "lab3")

database_url = f"postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}"

Base = declarative_base()
engine = create_engine(database_url)

# Tabla intermedia (Libro <-> Autor)
libro_autor = Table(
    'libro_autor',
    Base.metadata,
    Column('libro_id', Integer, ForeignKey('libro.id'), primary_key=True),
    Column('autor_id', Integer, ForeignKey('autor.id'), primary_key=True)
)

# Entidades
class Libro(Base):
    __tablename__ = 'libro'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    isbn = Column(String(13), unique=True, nullable=False)
    año_public = Column(Integer)
    rating = Column(ENUM('1', '2', '3', '4', '5', name='tipo_rating'), nullable=False)
    estado = Column(ENUM('borrador', 'publicado', 'archivado', name='tipo_estado'), nullable=False, server_default='publicado')
    genero_id = Column(Integer, ForeignKey('genero.id'), nullable=False)

    autores = relationship('Autor', secondary=libro_autor, back_populates='libros')
    genero = relationship('Genero', back_populates='libros')

    __table_args__ = (
        CheckConstraint('año_public <= EXTRACT(YEAR FROM CURRENT_DATE)', name='check_año'),
    )

class Autor(Base):
    __tablename__ = 'autor'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    nacionalidad = Column(String(30), nullable=False)

    libros = relationship('Libro', secondary=libro_autor, back_populates='autores')

class Genero(Base):
    __tablename__ = 'genero'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(20), unique=True, nullable=False)

    libros = relationship('Libro', back_populates='genero')

if __name__ == "__main__":
    print("Creando tablas en la base de datos...")
    Base.metadata.create_all(engine)
    print("¡Tablas creadas exitosamente!")