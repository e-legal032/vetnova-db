"""
📄 Script: validar_relaciones.py  
🧠 Propósito: Validar relaciones entre tablas mediante consultas JOIN explícitas  
✍️ Autoría: Ana Sposito  
🗓️ Fecha: Octubre 2025  
"""

# 🇪🇸 Importar librerías y modelos
# 🇬🇧 Import libraries and models
from sqlalchemy.orm import Session, aliased
from conexion_supabase import engine
from models.schema import (
    Duenio, Paciente, Personal, Turno,
    EstadoTurno, TipoTurno
)

# 🇪🇸 Crear sesión de conexión
# 🇬🇧 Create connection session
session = Session(bind=engine)

# 🐾 Consulta 1: Pacientes con sus dueños
# 🐾 Query 1: Pets with their owners
print("\n🐾 Pacientes y sus dueños:")
result1 = session.query(Paciente.nombre, Duenio.nombre)\
    .join(Duenio, Paciente.duenio_id == Duenio.id)\
    .limit(5).all()
for paciente, duenio in result1:
    print(f"Paciente: {paciente} — Dueño: {duenio}")

# 📅 Consulta 2: Turnos con profesional y paciente
# 📅 Query 2: Appointments with professional and patient
print("\n📅 Turnos con profesional y paciente:")
result2 = session.query(
    Turno.fecha,
    Turno.hora,
    Paciente.nombre,
    Personal.nombre
).join(Paciente, Turno.paciente_id == Paciente.id)\
 .join(Personal, Turno.profesional_id == Personal.id)\
 .limit(5).all()
for fecha, hora, paciente, profesional in result2:
    print(f"Fecha: {fecha} — Hora: {hora} — Paciente: {paciente} — Profesional: {profesional}")

# 🔍 Consulta 3: Turnos con estado y tipo
# 🔍 Query 3: Appointments with status and type
print("\n🔍 Turnos con estado y tipo:")
result3 = session.query(
    Turno.fecha,
    EstadoTurno.nombre,
    TipoTurno.nombre
).join(EstadoTurno, Turno.estado_id == EstadoTurno.id)\
 .join(TipoTurno, Turno.tipo_turno_id == TipoTurno.id)\
 .limit(5).all()
for fecha, estado, tipo in result3:
    print(f"Fecha: {fecha} — Estado: {estado} — Tipo: {tipo}")

# 🧾 Consulta 4: Turnos con creado_por y modificado_por
# 🧾 Query 4: Appointments with created_by and modified_by
creador = aliased(Personal)
modificador = aliased(Personal)

print("\n🧾 Turnos con autoría:")
result4 = session.query(
    Turno.fecha,
    creador.nombre.label("creado_por"),
    modificador.nombre.label("modificado_por")
).join(creador, Turno.creado_por == creador.id)\
 .join(modificador, Turno.modificado_por == modificador.id)\
 .limit(5).all()
for fecha, creado_por, modificado_por in result4:
    print(f"Fecha: {fecha} — Creado por: {creado_por} — Modificado por: {modificado_por}")

# 🇪🇸 Cerrar sesión
# 🇬🇧 Close session
session.close()
