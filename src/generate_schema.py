from sqlalchemy.schema import CreateTable, CreateIndex
from database import engine
from models import Base

def generate_schema():
    with open('scripts/schema.sql', 'w', encoding='utf-8') as f:
        f.write("-- TIPOS ENUM PERSONALIZADOS\n")
        f.write("CREATE TYPE estadolibro AS ENUM ('disponible', 'prestado', 'en_reparacion');\n")
        f.write("CREATE TYPE tipogenero AS ENUM ('ficcion', 'no_ficcion', 'academico');\n\n")
        
        f.write("-- TABLAS\n")
        for table in Base.metadata.sorted_tables:
            f.write(str(CreateTable(table).compile(engine)) + ";\n\n")
            for index in table.indexes:
                f.write(str(CreateIndex(index).compile(engine)) + ";\n")
            f.write("\n")
        
        f.write("-- FIN DEL SCHEMA\n")
    
    print(".sql generado correctamente en scripts/schema.sql")

if __name__ == "__main__":
    generate_schema()