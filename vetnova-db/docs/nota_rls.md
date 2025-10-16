# 🔐 Nota Técnica — Aplicación de Políticas RLS en VetNova LATAM  
# 🔐 Technical Note — RLS Policy Implementation in VetNova LATAM

---

## 📌 Objetivo / Objective

Este proyecto implementa políticas de seguridad a nivel de fila (Row Level Security, RLS) en Supabase para proteger datos sensibles, clínicos y operativos del sistema VetNova LATAM. Las políticas fueron diseñadas para reflejar escenarios reales de acceso según roles (`Veterinario`, `Recepcionista`, `Administrador`), garantizando trazabilidad, privacidad y control de acceso.  
This project implements Row Level Security (RLS) policies in Supabase to protect sensitive, clinical, and operational data in the VetNova LATAM system. Policies were designed to reflect real-world access scenarios based on roles (`Veterinarian`, `Receptionist`, `Administrator`), ensuring traceability, privacy, and access control.

---

## 🧱 Alcance / Scope

Se aplicaron políticas RLS en 14 tablas expuestas por la API REST de Supabase. Las políticas cubren:  
RLS policies were applied to 14 tables exposed via Supabase’s REST API. Policies cover:

- `SELECT`: acceso controlado a datos según rol y relación  
  `SELECT`: controlled data access based on role and relationship  
- `INSERT`: validación de permisos al crear registros  
  `INSERT`: permission validation when creating records  
- No se aplicaron `UPDATE` ni `DELETE` por decisión curatorial en esta etapa  
  `UPDATE` and `DELETE` were not applied at this stage by curatorial decision

---

## 🧠 Criterios de diseño / Design Criteria

- Se usó `auth.uid()` como identificador seguro de usuario autenticado  
  `auth.uid()` was used as a secure identifier for authenticated users  
- Se respetaron las relaciones entre tablas (`turnos`, `pacientes`, `duenios`, etc.)  
  Table relationships (`turnos`, `pacientes`, `duenios`, etc.) were respected  
- Se documentó cada política en `docs/politicas_rls.sql` con comentarios bilingües  
  Each policy was documented in `docs/politicas_rls.sql` with bilingual comments  
- Se aplicaron manualmente desde el SQL Editor de Supabase para garantizar trazabilidad  
  Policies were manually applied via Supabase’s SQL Editor to ensure traceability

---

## 🛠️ Aplicación / Implementation

1. Se activó RLS en cada tabla desde el panel de Supabase  
   RLS was enabled on each table from the Supabase panel  
2. Se ejecutó el archivo `docs/politicas_rls.sql` completo desde el SQL Editor  
   The full `docs/politicas_rls.sql` file was executed from the SQL Editor  
3. Se verificó la aplicación correcta de cada política en la pestaña RLS de cada tabla  
   Each policy’s correct application was verified in the RLS tab of each table

---

## 📁 Ubicación del archivo / File Location

El archivo [`docs/politicas_rls.sql`](politicas_rls.sql) forma parte de la entrega y puede reutilizarse, versionarse o adaptarse en producción.
  
The file [`docs/politicas_rls.sql`](politicas_rls.sql) is part of the delivery and can be reused, versioned, or adapted for production.

---

## ✅ Resultado / Outcome

El sistema quedó protegido por políticas RLS alineadas con buenas prácticas de seguridad, listas para integrarse con Supabase Auth y un frontend real.  
The system is now protected by RLS policies aligned with security best practices, ready to integrate with Supabase Auth and a real frontend.
