from sqlalchemy import Column, String, Float, Text, Date, Time, DateTime, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()

# 👤 Dueños de mascotas
class Duenio(Base):
    __tablename__ = 'duenios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    telefono = Column(String)
    email = Column(String)
    direccion = Column(String)
    dni = Column(String)

    pacientes = relationship("Paciente", back_populates="duenio")

# 🐾 Pacientes (mascotas)
class Paciente(Base):
    __tablename__ = 'pacientes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    especie = Column(String)
    raza = Column(String)
    edad = Column(Integer)
    peso = Column(Float)
    duenio_id = Column(Integer, ForeignKey('duenios.id'))

    duenio = relationship("Duenio", back_populates="pacientes")
    turnos = relationship("Turno", back_populates="paciente")
    historia_clinica = relationship("HistoriaClinica", back_populates="paciente")

# 🧑⚕️ Roles del personal
class Rol(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)

    personal = relationship("Personal", back_populates="rol")

# 👩‍⚕️ Personal del centro veterinario
class Personal(Base):
    __tablename__ = 'personal'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String)
    email = Column(String)
    rol_id = Column(Integer, ForeignKey('roles.id'))

    rol = relationship("Rol", back_populates="personal")
    disponibilidad = relationship("Disponibilidad", back_populates="personal")
    especialidades = relationship("PersonalEspecialidad", back_populates="personal")
    sedes = relationship("PersonalSede", back_populates="personal")
    turnos = relationship("Turno", foreign_keys='Turno.profesional_id', back_populates="profesional")
    creados = relationship("Turno", foreign_keys='Turno.creado_por', back_populates="creador")
    modificados = relationship("Turno", foreign_keys='Turno.modificado_por', back_populates="modificador")
    historias = relationship("HistoriaClinica", back_populates="profesional")

# 🏥 Sedes físicas
class Sede(Base):
    __tablename__ = 'sedes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    ciudad = Column(String)

    personal = relationship("PersonalSede", back_populates="sede")

# 🔗 Relación entre personal y sedes
class PersonalSede(Base):
    __tablename__ = 'personal_sede'

    id = Column(Integer, primary_key=True, autoincrement=True)
    personal_id = Column(UUID(as_uuid=True), ForeignKey('personal.id'))
    sede_id = Column(Integer, ForeignKey('sedes.id'))

    personal = relationship("Personal", back_populates="sedes")
    sede = relationship("Sede", back_populates="personal")

# 🩺 Especialidades médicas
class Especialidad(Base):
    __tablename__ = 'especialidades'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)

    personal = relationship("PersonalEspecialidad", back_populates="especialidad")

# 🔗 Relación entre personal y especialidades
class PersonalEspecialidad(Base):
    __tablename__ = 'personal_especialidad'

    id = Column(Integer, primary_key=True, autoincrement=True)
    personal_id = Column(UUID(as_uuid=True), ForeignKey('personal.id'))
    especialidad_id = Column(Integer, ForeignKey('especialidades.id'))

    personal = relationship("Personal", back_populates="especialidades")
    especialidad = relationship("Especialidad", back_populates="personal")

# 📆 Disponibilidad semanal del personal
class Disponibilidad(Base):
    __tablename__ = 'disponibilidad'

    id = Column(Integer, primary_key=True, autoincrement=True)
    personal_id = Column(UUID(as_uuid=True), ForeignKey('personal.id'))
    dia_semana = Column(String)
    hora_inicio = Column(Time)
    hora_fin = Column(Time)

    personal = relationship("Personal", back_populates="disponibilidad")

# 📌 Tipos de turno
class TipoTurno(Base):
    __tablename__ = 'tipo_turno'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)

    turnos = relationship("Turno", back_populates="tipo")

# 📌 Estado del turno
class EstadoTurno(Base):
    __tablename__ = 'estado_turno'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)

    turnos = relationship("Turno", back_populates="estado")

# 📅 Turnos agendados
class Turno(Base):
    __tablename__ = 'turnos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    paciente_id = Column(Integer, ForeignKey('pacientes.id'))
    tipo_turno_id = Column(Integer, ForeignKey('tipo_turno.id'))
    estado_id = Column(Integer, ForeignKey('estado_turno.id'))
    fecha = Column(Date)
    hora = Column(Time)
    profesional_id = Column(UUID(as_uuid=True), ForeignKey('personal.id'))
    creado_por = Column(UUID(as_uuid=True), ForeignKey('personal.id'))
    modificado_por = Column(UUID(as_uuid=True), ForeignKey('personal.id'))
    fecha_cancelacion = Column(DateTime)

    paciente = relationship("Paciente", back_populates="turnos")
    tipo = relationship("TipoTurno", back_populates="turnos")
    estado = relationship("EstadoTurno", back_populates="turnos")
    profesional = relationship("Personal", foreign_keys=[profesional_id], back_populates="turnos")
    creador = relationship("Personal", foreign_keys=[creado_por], back_populates="creados")
    modificador = relationship("Personal", foreign_keys=[modificado_por], back_populates="modificados")

# 📋 Historia clínica
class HistoriaClinica(Base):
    __tablename__ = 'historia_clinica'

    id = Column(Integer, primary_key=True, autoincrement=True)
    paciente_id = Column(Integer, ForeignKey('pacientes.id'))
    fecha = Column(Date)
    profesional_id = Column(UUID(as_uuid=True), ForeignKey('personal.id'))
    diagnostico = Column(Text)
    tratamiento = Column(Text)
    observaciones = Column(Text)

    paciente = relationship("Paciente", back_populates="historia_clinica")
    profesional = relationship("Personal", back_populates="historias")
    adjuntos = relationship("Adjunto", back_populates="historia")

# 📎 Archivos adjuntos
class Adjunto(Base):
    __tablename__ = 'adjuntos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    historia_id = Column(Integer, ForeignKey('historia_clinica.id'))
    nombre_archivo = Column(String)
    tipo = Column(String)
    ruta = Column(String)
    fecha_subida = Column(DateTime)

    historia = relationship("HistoriaClinica", back_populates="adjuntos")
