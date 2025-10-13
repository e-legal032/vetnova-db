"""
📄 Script: simular_datos.py  
🧠 Propósito: Simular datos ficticios para poblar la base PostgreSQL en Supabase  
✍️ Autoría: Ana Sposito  
🗓️ Fecha: Octubre 2025  
"""

# 🇪🇸 Librerías necesarias
# 🇬🇧 Required libraries
from faker import Faker
from sqlalchemy.orm import Session
from conexion_supabase import engine
from models.schema import Duenio, Paciente, Personal, Turno
from models.schema import Rol, TipoTurno, EstadoTurno


# 🇪🇸 Inicializar generador de datos ficticios
# 🇬🇧 Initialize fake data generator
faker = Faker('es_AR')  # Localización argentina

# 🇪🇸 Crear sesión de conexión
# 🇬🇧 Create connection session
session = Session(bind=engine)

# 🇪🇸 Simular dueños
# 🇬🇧 Simulate pet owners
duenios = []
for _ in range(5):
    d = Duenio(
        nombre=faker.name(),
        telefono=faker.phone_number(),
        email=faker.email(),
        direccion=faker.address(),
        dni=faker.random_number(digits=8)
    )
    duenios.append(d)
    session.add(d)

session.commit()

# 🇪🇸 Simular pacientes
# 🇬🇧 Simulate pets
pacientes = []
for _ in range(10):
    p = Paciente(
        nombre=faker.first_name(),
        especie=faker.random_element(elements=["Perro", "Gato", "Conejo"]),
        raza=faker.word(),
        edad=faker.random_int(min=1, max=15),
        peso=round(faker.random_number(digits=2) / 10, 1),
        duenio_id=faker.random_element(elements=[d.id for d in duenios])
    )
    pacientes.append(p)
    session.add(p)

session.commit()

# 🇪🇸 Simular roles
# 🇬🇧 Simulate roles
roles = []
nombres_roles = ["Veterinario", "Recepcionista", "Administrador"]

for nombre in nombres_roles:
    r = Rol(nombre=nombre)
    roles.append(r)
    session.add(r)

session.commit()

# 🇪🇸 Simular personal
# 🇬🇧 Simulate staff
personal = []
for i in range(4):
    prof = Personal(
        nombre=faker.name(),
        email=faker.email(),
        rol_id=roles[i % len(roles)].id  # Asigna roles rotativos
    )
    personal.append(prof)
    session.add(prof)

session.commit()

# 🇪🇸 Simular tipos de turno
# 🇬🇧 Simulate appointment types
tipos_turno = []
nombres_tipos = ["Consulta", "Cirugía", "Vacunación"]

for nombre in nombres_tipos:
    t = TipoTurno(nombre=nombre)
    tipos_turno.append(t)
    session.add(t)

session.commit()

# 🇪🇸 Simular estados de turno
# 🇬🇧 Simulate appointment statuses
estados_turno = []
nombres_estados = ["Pendiente", "Confirmado", "Cancelado", "Atendido"]

for nombre in nombres_estados:
    e = EstadoTurno(nombre=nombre)
    estados_turno.append(e)
    session.add(e)

session.commit()

# 🇪🇸 Simular turnos
# 🇬🇧 Simulate appointments
for _ in range(8):
    turno = Turno(
        paciente_id=faker.random_element(elements=[p.id for p in pacientes]),
        tipo_turno_id=faker.random_element(elements=[t.id for t in tipos_turno]),
        estado_id=faker.random_element(elements=[e.id for e in estados_turno]),
        fecha=faker.date_between(start_date='-30d', end_date='+30d'),
        hora=faker.time(),
        profesional_id=faker.random_element(elements=[prof.id for prof in personal]),
        creado_por=personal[0].id,
        modificado_por=personal[0].id,
        fecha_cancelacion=None
    )
    session.add(turno)

session.commit()

print("✅ Datos simulados insertados correctamente.")
