"""
🧾 Script: main.py  
🧠 Propósito: Crear todas las tablas en Supabase usando el modelo definido en schema.py  
✍️ Autoría: Ana Sposito  
🗓️ Fecha: Octubre 2025  
"""

# 🇪🇸 Importar el modelo relacional (tablas y relaciones)
# 🇬🇧 Import the relational model (tables and relationships)
from models.schema import Base

# 🇪🇸 Importar el motor de conexión a Supabase
# 🇬🇧 Import the Supabase connection engine
from conexion_supabase import engine

# 🇪🇸 Crear todas las tablas en la base de datos
# 🇬🇧 Create all tables in the database
Base.metadata.create_all(engine)

print("✅ Tablas creadas exitosamente en Supabase.")

