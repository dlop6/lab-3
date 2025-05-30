from sqlalchemy import Column, Integer, String, Date, Numeric, Enum, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from database import Base

class EstadoLibro(PyEnum):
    DISPONIBLE = 'disponible'
    PRESTADO = 'prestado'
    EN_REPARACION = 'en_reparacion'

class TipoGenero(PyEnum):
    FICCION = 'ficcion'
    NO_FICCION = 'no_ficcion'
    ACADEMICO = 'academico'

class Libro(Base):
    __tablename__ = 'libros'
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    isbn = Column(String(20), unique=True, nullable=False)
    fecha_publicacion = Column(Date)
    precio = Column(Numeric(10, 2), CheckConstraint('precio >= 0'))
    estado = Column(Enum(EstadoLibro, name='estadolibro'), nullable=False)
    
    autores = relationship("Autor", secondary="libro_autor", back_populates="libros")
    generos = relationship("Genero", secondary="libro_genero", back_populates="libros")

class Autor(Base):
    __tablename__ = 'autores'
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    nacionalidad = Column(String(30))
    
    libros = relationship("Libro", secondary="libro_autor", back_populates="autores")

class Genero(Base):
    __tablename__ = 'generos'
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(30), nullable=False)
    tipo = Column(Enum(TipoGenero, name='tipogenero'), nullable=False)
    
    libros = relationship("Libro", secondary="libro_genero", back_populates="generos")

class LibroAutor(Base):
    __tablename__ = 'libro_autor'
    
    libro_id = Column(Integer, ForeignKey('libros.id'), primary_key=True)
    autor_id = Column(Integer, ForeignKey('autores.id'), primary_key=True)
    rol = Column(String(30))

class LibroGenero(Base):
    __tablename__ = 'libro_genero'
    
    libro_id = Column(Integer, ForeignKey('libros.id'), primary_key=True)
    genero_id = Column(Integer, ForeignKey('generos.id'), primary_key=True)