-- 🔐 Row Level Security (RLS) Policies — VetNova LATAM
-- 📁 Archivo curatorial para documentación y aplicación manual en Supabase
-- ✍️ Autoría: Ana Sposito
-- 🗓️ Fecha: Octubre 2025

-- =========================
-- 🧑⚕️ Tabla: turnos
-- =========================

-- Veterinario ve sus propios turnos
CREATE POLICY "Veterinario ve sus turnos"
ON turnos FOR SELECT TO authenticated
USING (profesional_id = auth.uid());

-- Administrador ve todos los turnos
CREATE POLICY "Administrador ve todos los turnos"
ON turnos FOR SELECT TO authenticated
USING (EXISTS (
  SELECT 1 FROM personal WHERE id = auth.uid() AND rol_id = (
    SELECT id FROM roles WHERE nombre = 'Administrador'
  )
));

-- Recepcionista puede insertar turnos
CREATE POLICY "Recepcionista inserta turnos"
ON turnos FOR INSERT TO authenticated
WITH CHECK (EXISTS (
  SELECT 1 FROM personal WHERE id = auth.uid() AND rol_id = (
    SELECT id FROM roles WHERE nombre = 'Recepcionista'
  )
));

-- =========================
-- 🧑⚕️ Tabla: historia_clinica
-- =========================

-- Veterinario ve historia clínica que atendió
CREATE POLICY "Veterinario ve historia clínica"
ON historia_clinica FOR SELECT TO authenticated
USING (profesional_id = auth.uid());

-- =========================
-- 🐾 Tabla: pacientes
-- =========================

-- Veterinario ve sus pacientes
CREATE POLICY "Veterinario ve sus pacientes"
ON pacientes FOR SELECT TO authenticated
USING (EXISTS (
  SELECT 1 FROM turnos
  WHERE turnos.paciente_id = pacientes.id
  AND turnos.profesional_id = auth.uid()
));

-- =========================
-- 👤 Tabla: duenios
-- =========================

-- Veterinario ve dueños de sus pacientes
CREATE POLICY "Veterinario ve dueños de sus pacientes"
ON duenios FOR SELECT TO authenticated
USING (EXISTS (
  SELECT 1 FROM pacientes
  WHERE pacientes.duenio_id = duenios.id
  AND EXISTS (
    SELECT 1 FROM turnos
    WHERE turnos.paciente_id = pacientes.id
    AND turnos.profesional_id = auth.uid()
  )
));

-- =========================
-- 👩⚕️ Tabla: personal
-- =========================

-- Cada usuario ve su perfil
CREATE POLICY "Personal ve su perfil"
ON personal FOR SELECT TO authenticated
USING (id = auth.uid());

-- =========================
-- 📆 Tabla: disponibilidad
-- =========================

-- Veterinario ve su disponibilidad
CREATE POLICY "Veterinario ve su disponibilidad"
ON disponibilidad FOR SELECT TO authenticated
USING (personal_id = auth.uid());

-- =========================
-- 📎 Tabla: adjuntos
-- =========================

-- Veterinario ve adjuntos clínicos que generó
CREATE POLICY "Veterinario ve adjuntos clínicos"
ON adjuntos FOR SELECT TO authenticated
USING (EXISTS (
  SELECT 1 FROM historia_clinica
  WHERE historia_clinica.id = adjuntos.historia_id
  AND historia_clinica.profesional_id = auth.uid()
));

-- =========================
-- 🩺 Tabla: especialidades
-- =========================

-- Lectura general
CREATE POLICY "Lectura general de especialidades"
ON especialidades FOR SELECT TO authenticated
USING (true);

-- =========================
-- 🏥 Tabla: sedes
-- =========================

-- Lectura general
CREATE POLICY "Lectura general de sedes"
ON sedes FOR SELECT TO authenticated
USING (true);

-- =========================
-- 🔗 Tabla: personal_sede
-- =========================

-- Lectura general
CREATE POLICY "Lectura general de personal_sede"
ON personal_sede FOR SELECT TO authenticated
USING (true);

-- =========================
-- 🔗 Tabla: personal_especialidad
-- =========================

-- Lectura general
CREATE POLICY "Lectura general de personal_especialidad"
ON personal_especialidad FOR SELECT TO authenticated
USING (true);

-- =========================
-- 📌 Tabla: tipo_turno
-- =========================

-- Lectura general
CREATE POLICY "Lectura general de tipo_turno"
ON tipo_turno FOR SELECT TO authenticated
USING (true);

-- =========================
-- 📌 Tabla: estado_turno
-- =========================

-- Lectura general
CREATE POLICY "Lectura general de estado_turno"
ON estado_turno FOR SELECT TO authenticated
USING (true);

-- =========================
-- 🧑⚕️ Tabla: roles
-- =========================

-- Lectura general
CREATE POLICY "Lectura general de roles"
ON roles FOR SELECT TO authenticated
USING (true);
