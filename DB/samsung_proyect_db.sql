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

-- Crear la tabla admin
CREATE TABLE admin (
    id_admin int IDENTITY(1,1) PRIMARY KEY,
    nombre varchar(45) NOT NULL,
    apellido varchar(45) NOT NULL,
    usuario varchar(45) NOT NULL,
    contrasena varchar(45) NOT NULL,
    rol varchar(45) NOT NULL
);

INSERT INTO admin (nombre, apellido, usuario, contrasena, rol)
VALUES
    ('Orga', 'Carderor', '123', '123', 'directora'),
    ('Meguelina', 'Guzman', 'miguelina_admin', 'adminpass', 'vice-directora'),
    ('Sergei', 'Diaz', 'sergei_admin', 'password', 'administrador');

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


SELECT a.id_alumnos, a.nombre, a.apellido, a.usuario, a.contrasena,
       CONCAT(p.nombre, ' ', p.apellido) AS profesor
FROM alumnos a
INNER JOIN profesores p ON a.fk_id_profesores = p.id_profesores
WHERE a.id_alumnos = 1;


select * from profesores
select * from alumnos