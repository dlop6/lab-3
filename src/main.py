from database import SessionLocal, get_db
from models import Libro, EstadoLibro
from datetime import date

def crear_libro():
    db = next(get_db())
    try:
        titulo = input("Título: ")
        isbn = input("ISBN: ")
        fecha_str = input("Fecha de publicación (YYYY-MM-DD): ")
        fecha_publicacion = date.fromisoformat(fecha_str)
        precio = float(input("Precio: "))
        estado = EstadoLibro.DISPONIBLE 

        nuevo_libro = Libro(
            titulo=titulo,
            isbn=isbn,
            fecha_publicacion=fecha_publicacion,
            precio=precio,
            estado=estado
        )
        db.add(nuevo_libro)
        db.commit()
        print(f"Libro creado: {nuevo_libro.titulo}")
        return nuevo_libro
    except Exception as e:
        db.rollback()
        print(f" Error al crear libro: {e}")
    finally:
        db.close()

def obtener_libros():
    db = next(get_db())
    try:
        libros = db.query(Libro).all()
        print("\nListado de libros:")
        for libro in libros:
            print(f"ID: {libro.id} - {libro.titulo} ({libro.estado})")
        return libros
    except Exception as e:
        print(f" Error al obtener libros: {e}")
    finally:
        db.close()

def actualizar_libro():
    db = next(get_db())
    try:
        libro_id = int(input("ID del libro a actualizar: "))
        libro = db.query(Libro).filter(Libro.id == libro_id).first()
        if libro:
            print(f"Estado actual: {libro.estado}")
            print("Estados posibles:")
            for estado in EstadoLibro:
                print(f"- {estado.value}")
            nuevo_estado = input("Nuevo estado: ")
            if nuevo_estado in [e.value for e in EstadoLibro]:
                libro.estado = EstadoLibro(nuevo_estado) 
                db.commit()
                print(f"Libro actualizado: {libro.titulo} ahora está {libro.estado.value}")
            else:
                print(" Estado no válido")
        else:
            print(" Libro no encontrado")
    except Exception as e:
        db.rollback()
        print(f" Error al actualizar libro: {e}")
    finally:
        db.close()

def eliminar_libro():
    db = next(get_db())
    try:
        libro_id = int(input("ID del libro a eliminar: "))
        libro = db.query(Libro).filter(Libro.id == libro_id).first()
        if libro:
            db.delete(libro)
            db.commit()
            print(f"Libro eliminado: {libro.titulo}")
        else:
            print(" Libro no encontrado")
    except Exception as e:
        db.rollback()
        print(f" Error al eliminar libro: {e}")
    finally:
        db.close()

def menu():
    while True:
        print("\n--- Menú de Libros ---")
        print("1. Crear libro")
        print("2. Listar libros")
        print("3. Actualizar libro")
        print("4. Eliminar libro")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_libro()
        elif opcion == "2":
            obtener_libros()
        elif opcion == "3":
            actualizar_libro()
        elif opcion == "4":
            eliminar_libro()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()