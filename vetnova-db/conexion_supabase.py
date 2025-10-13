"""
📦 Módulo: conexion_supabase.py  
🧠 Propósito: Conexión segura y centralizada a Supabase usando SQLAlchemy  
✍️ Autoría: Ana Sposito  
🗓️ Fecha: Octubre 2025  
"""

# 🇪🇸 Seguridad: carga de credenciales desde archivo .env
# 🇬🇧 Security: load credentials from .env file
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os
from sqlalchemy import create_engine

# 🇪🇸 Cargar variables desde .env
# 🇬🇧 Load variables from .env
load_dotenv()
user = os.getenv("DB_USER")
raw_password = os.getenv("DB_PASSWORD")
encoded_password = quote_plus(raw_password)
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
db = os.getenv("DB_NAME")

# 🇪🇸 Construir URI segura
# 🇬🇧 Build secure URI
uri = f"postgresql://{user}:{encoded_password}@{host}:{port}/{db}"

# 🇪🇸 Crear motor de conexión
# 🇬🇧 Create connection engine
engine = create_engine(uri)
