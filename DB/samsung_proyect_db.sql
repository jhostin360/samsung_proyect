-- Crear la base de datos
CREATE DATABASE proyecto_samsung;
GO

-- Usar la base de datos
USE proyecto_samsung;
GO

-- Crear la tabla alumnos
CREATE TABLE alumnos 
(
    id_alumnos int IDENTITY(1,1) PRIMARY KEY,
    nombre varchar(45) NULL,
    apellido varchar(45) NULL,
    sexo varchar(45) NULL,
    usuario varchar(45) NOT NULL,
    contrasena varchar(45) NOT NULL,
    fk_id_profesores int NULL,
    FOREIGN KEY (fk_id_profesores) REFERENCES profesores(id_profesores)
);
-- Crear la tabla profesores 
CREATE TABLE profesores 
(
    id_profesores int IDENTITY(1,1) PRIMARY KEY,
    nombre varchar(45) NULL,
    apellido varchar(45) NULL,
    usuario varchar(45) NOT NULL,
    contrasena varchar(45) NOT NULL
);

-- Crear la tabla calificaciones
CREATE TABLE calificaciones 
(
    id_calificaciones int IDENTITY(1,1) PRIMARY KEY,
    id_alumnos int FOREIGN KEY REFERENCES alumnos(id_alumnos),
    Primer_examen int NULL,
    Segundo_examen int NULL,
    Tercer_examen int NULL,
    Examen_final int NULL
);

-- Agregar la columna Promedio a la tabla calificaciones
ALTER TABLE calificaciones ADD Promedio AS (Primer_examen + Segundo_examen + Tercer_examen + Examen_final) / 4 PERSISTED;

-- Insertar datos en la tabla profesores
INSERT INTO profesores (nombre, apellido, usuario, contrasena)
VALUES ('Juan', 'Perez', 'juan123', '123456');

INSERT INTO profesores (nombre, apellido, usuario, contrasena)
VALUES ('Maria', 'Lopez', 'maria456', '789012');

INSERT INTO profesores (nombre, apellido, usuario, contrasena)
VALUES ('Carlos', 'Gomez', 'carlos789', '345678');

-- Insertar un estudiante y asignarle un profesor (reemplaza los valores de ejemplo)
INSERT INTO alumnos (nombre, apellido, sexo, usuario, contrasena, fk_id_profesores)
VALUES ('prueba3', '333', 'Femenina', '333', '123', 3);

select * from profesores
select * from alumnos