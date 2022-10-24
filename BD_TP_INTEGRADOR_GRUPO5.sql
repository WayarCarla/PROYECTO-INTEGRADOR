use CREATE DATABASE IF NOT EXISTS db_inm_brf DEFAULT CHARACTER SET UTF8MB4; 
--- TABLA PROPIEDAD ---

CREATE TABLE db_inm_brf.propiedad (
Id_Propiedad INT NOT NULL,
Id_Tipo VARCHAR(45) NOT NULL,
Id_Estado VARCHAR(45) NOT NULL,
Id_Operacion_Comercial VARCHAR(45) NOT NULL,
Id_Propietario VARCHAR(45) NOT NULL,
Nombre VARCHAR(45) NOT NULL,
Direccion VARCHAR(45) NOT NULL,
Contacto VARCHAR(45) NOT NULL,
Propiedadcol VARCHAR(45) NOT NULL,
PRIMARY KEY (Id_Propiedad),
UNIQUE INDEX Id_Propiedad_UNIQUE (Id_Propiedad ASC) VISIBLE,
UNIQUE INDEX Id_Operacion_Comercial_UNIQUE (Id_Operacion_Comercial ASC) VISIBLE,
UNIQUE INDEX Id_Propietario_UNIQUE (Id_Propietario ASC) VISIBLE)
COMMENT = 'Tabla de Propiedad ';

--- TABLA ESTADO ---
CREATE TABLE db_inm_brf.ESTADO (
Id_Estado VARCHAR(45) NOT NULL,
Nombre_Estado VARCHAR(45) NOT NULL,
PRIMARY KEY (Id_Estado) );

--- TABLA OPERATORIA COMERCIAL ---
CREATE TABLE db_inm_brf.OperatoriaComercial (
Id_Operatoria_Comercial VARCHAR(45) NOT NULL,
Nombre_Operatoria_Comercial VARCHAR(45) NOT NULL,
PRIMARY KEY (Id_Operatoria_Comercial) );

