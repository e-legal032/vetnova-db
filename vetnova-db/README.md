# 🐾 VetNova LATAM — Gestión de turnos y registros clínicos veterinarios  
# 🐾 VetNova LATAM — Veterinary Appointment and Clinical Record Management System

Sistema de base de datos relacional para una red de clínicas veterinarias en LATAM, diseñado para integrarse con Supabase y proteger datos sensibles mediante políticas RLS. Incluye simulación de datos, validación de relaciones y documentación curatorial.  
Relational database system for a network of veterinary clinics across LATAM, designed to integrate with Supabase and protect sensitive data through RLS policies. Includes data simulation, relationship validation, and curatorial documentation.

---

## 📁 Estructura del proyecto / Project Structure

```
📦 vetnova-latam/
├── models/
│   └── schema.py                 # Modelo relacional con UUID y relaciones / Relational model with UUID and relationships
├── docs/
│   ├── politicas_rls.sql        # Políticas RLS aplicadas manualmente / RLS policies applied manually
│   └── nota_rls.md              # Nota técnica sobre seguridad y aplicación / Technical note on security and implementation
├── main.py                      # Crea todas las tablas en Supabase / Creates all tables in Supabase
├── simular_datos.py             # Inserta datos ficticios con Faker / Inserts simulated data using Faker
├── validar_relaciones.py        # Verifica integridad entre tablas / Verifies integrity between tables
└── README.md                    # Este archivo / This file
```

---
## 🧬 Modelo relacional / Relational Model

![Modelo relacional](docs/modelo_relacional.png)

Este diagrama fue generado en [dbdiagram.io](https://dbdiagram.io) y representa las entidades principales del sistema VetNova LATAM, sus relaciones y claves foráneas.  
Se utiliza como recurso visual para comprender la estructura relacional antes de aplicar los scripts y políticas de seguridad.  

This diagram was generated in [dbdiagram.io](https://dbdiagram.io) and illustrates the main entities of the VetNova LATAM system, their relationships, and foreign keys.  
It serves as a visual reference to understand the relational structure before applying scripts and security policies.

---
## 🧠 Objetivos  
## 🧠 Objectives

- Modelar una base de datos realista para una red veterinaria  
  Model a realistic database for a veterinary network  
- Simular datos clínicos y operativos con trazabilidad  
  Simulate clinical and operational data with traceability  
- Aplicar seguridad a nivel de fila (Row Level Security, RLS) con Supabase Auth  
  Apply Row Level Security (RLS) using Supabase Auth  
- Documentar cada paso con enfoque curatorial y reproducible  
  Document each step with a curatorial and reproducible approach

---

## ⚙️ Requisitos  
## ⚙️ Requirements

- Cuenta en [Supabase](https://supabase.com/)  
  Supabase account  
- Python 3.10+  
- Paquetes / Packages: `sqlalchemy`, `faker`, `psycopg2-binary`

---

## 📦 Instalación de dependencias / Dependency Installation

1. Activar el entorno virtual (si ya está creado)  
   Activate the virtual environment (if already created):

   ```bash
   source venv/bin/activate
   ```

2. Instalar las dependencias desde el archivo `requirements.txt`  
   Install dependencies from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

**Instalación manual / Manual installation:**

```bash
pip install sqlalchemy faker psycopg2-binary
```

---

## 🚀 Ejecución  
## 🚀 Execution

**Crear tablas / Create tables:**

```bash
python main.py
```

**Insertar datos simulados / Insert simulated data:**

```bash
python simular_datos.py
```

**Verificar relaciones / Validate relationships:**

```bash
python validar_relaciones.py
```

**Aplicar políticas RLS / Apply RLS policies:**

- Activar RLS en cada tabla desde el panel de Supabase  
  Enable RLS on each table from the Supabase panel  
- Abrir el SQL Editor  
  Open the SQL Editor  
- Ejecutar el archivo `docs/politicas_rls.sql`  
  Execute the file `docs/politicas_rls.sql`

---

## 🔐 Seguridad y RLS  
## 🔐 Security and RLS

Las políticas de seguridad están documentadas en [docs/politicas_rls.sql](docs/politicas_rls.sql).  
Security policies are documented in [docs/politicas_rls.sql](docs/politicas_rls.sql).

La nota técnica completa sobre su aplicación se encuentra en [docs/nota_rls.md](docs/nota_rls.md).  
The full technical note on their implementation is available in [docs/nota_rls.md](docs/nota_rls.md).

---

## ✍️ Autoría  
## ✍️ Authorship

Ana Sposito  
Octubre 2025  
Proyecto académico y profesional con enfoque curatorial  
Academic and professional project with curatorial focus
