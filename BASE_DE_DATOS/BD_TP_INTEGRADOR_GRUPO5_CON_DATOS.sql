-- -----------------------------------------------------
-- Schema db_inm_brf
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_inm_brf` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `db_inm_brf` ;

-- -----------------------------------------------------
-- Table `db_inm_brf`.`estado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_inm_brf`.`estado` (
  `Id_Estado` INT NOT NULL,
  `Nombre_Estado` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`Id_Estado`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci
COMMENT = 'Tabla de Estados';
-------------------------------------------------------
-- Tabla ESTADO - INSERTANDO DATOS 
-------------------------------------------------------
insert into `db_inm_brf`.`estado` values (1,'DISPONIBLE');
insert into `db_inm_brf`.`estado` values (2,'NO DISPONIBLE');
-- -----------------------------------------------------
-- Table `db_inm_brf`.`operatoria comercial`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_inm_brf`.`operatoria comercial` (
  `Id_Operatoria_Comercial` INT NOT NULL,
  `Nombre_Operatoria_Comercial` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`Id_Operatoria_Comercial`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci
COMMENT = 'Tabla de Operatoria Comercial';

-------------------------------------------------------
-- Tabla OPERATORIA COMERCIAL - INSERTANDO DATOS 
-------------------------------------------------------
insert into `db_inm_brf`.`operatoria comercial` values (1,'VENTA');
insert into `db_inm_brf`.`operatoria comercial` values (2,'ALQUILER');

-- -----------------------------------------------------
-- Table `db_inm_brf`.`propietario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_inm_brf`.`propietario` (
  `Id_Propietario` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Apellido` VARCHAR(45) NOT NULL,
  `Dirección` VARCHAR(100) NOT NULL,
  `Telefono` INT NOT NULL,
  `Email` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`Id_Propietario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci
COMMENT = 'Tabla de Propietarios';

-------------------------------------------------------
-- Tabla PROPIETARIO - INSERTANDO DATOS 
-------------------------------------------------------
insert into `db_inm_brf`.`propietario` values (1,'CARLA','WAYAR','SANTA CATALINA 100','388444444','carla@gmail.com');
insert into `db_inm_brf`.`propietario` values (2,'OSCAR','GAZZOLA ','CHACO','38814443','oscar@gmail.com');
insert into `db_inm_brf`.`propietario` values (3,'Miguel','Segnana','CHACO','12345678','msegnana@gmail.com');
-- -----------------------------------------------------
-- Table `db_inm_brf`.`tipo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_inm_brf`.`tipo` (
  `Id_Tipo` INT NOT NULL,
  `Nombre_Tipo` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`Id_Tipo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci
COMMENT = 'Tabla Tipo de Propiedad';

-------------------------------------------------------
-- Tabla TIPO - INSERTANDO DATOS 
-------------------------------------------------------
insert into `db_inm_brf`.`tipo` values (1,'LOCAL COMERCIAL');
insert into `db_inm_brf`.`tipo` values (2,'DEPARTAMENTO ');
insert into `db_inm_brf`.`tipo` values (3,'CASA ');
insert into `db_inm_brf`.`tipo` values (4,'CABAÑA');
insert into `db_inm_brf`.`tipo` values (5,'MONOAMBIENTE');
-- -----------------------------------------------------
-- Table `db_inm_brf`.`propiedad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_inm_brf`.`propiedad` (
  `Id_Propiedad` INT NOT NULL,
  `Id_Tipo` INT NOT NULL,
  `Id_Estado` INT NOT NULL,
  `Id_Operacion_Comercial` INT NOT NULL,
  `Id_Propietario` INT NOT NULL,
  `Localidad` VARCHAR(45) NOT NULL,
  `Provincia` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Id_Propiedad`),
  CONSTRAINT `IdEstado`
    FOREIGN KEY (`Id_Estado`)
    REFERENCES `db_inm_brf`.`estado` (`Id_Estado`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `IdOperacionComercial`
    FOREIGN KEY (`Id_Operacion_Comercial`)
    REFERENCES `db_inm_brf`.`operatoria comercial` (`Id_Operatoria_Comercial`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `IdPropietario`
    FOREIGN KEY (`Id_Propietario`)
    REFERENCES `db_inm_brf`.`propietario` (`Id_Propietario`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `IdTipo`
    FOREIGN KEY (`Id_Tipo`)
    REFERENCES `db_inm_brf`.`tipo` (`Id_Tipo`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci
COMMENT = 'Tabla de Propiedad';

CREATE INDEX `IdTipo_idx` ON `db_inm_brf`.`propiedad` (`Id_Tipo` ASC) VISIBLE;

CREATE INDEX `IdEstado_idx` ON `db_inm_brf`.`propiedad` (`Id_Estado` ASC) VISIBLE;

CREATE INDEX `IdOperacionComercial_idx` ON `db_inm_brf`.`propiedad` (`Id_Operacion_Comercial` ASC) VISIBLE;

CREATE INDEX `IdPropietario_idx` ON `db_inm_brf`.`propiedad` (`Id_Propietario` ASC) VISIBLE;
-------------------------------------------------------
-- Tabla PROPIEDAD - INSERTANDO DATOS 
-------------------------------------------------------
USE `db_inm_brf` ;

insert into `db_inm_brf`.`propiedad`  values ('1', '5', '1', '2', '1', 'SAN SALVADOR DE JUJUY', 'JUJUY');
insert into `db_inm_brf`.`propiedad`  values ('2', '4', '2', '1', '2', 'RESISTENCIA', 'CHACO');
insert into `db_inm_brf`.`propiedad`  values ('3', '5', '1', '2', '3', 'Formosa', 'Formosa');
insert into `db_inm_brf`.`propiedad`  values ('4', '5', '2', '2', '3', 'Clorinda', 'Formosa');
insert into `db_inm_brf`.`propiedad`  values ('5', '5', '2', '2', '1', 'Tafi del Valle', 'Tucuman');
insert into `db_inm_brf`.`propiedad`  values ('6', '2', '1', '1', '1', 'Cachi', 'Salta');
-- ------------------------------------------------------------------------------
-- Listado de propiedades TOTALES, sin distinción de estados
-- 
select * from propiedad
-- ---------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------
-- Listado de propiedades DISPONIBLES para la venta
-- 
select * from propiedad where Id_Operacion_Comercial= 1 and Id_Estado= 1
-- -----------------------------------------------------------------------------------

-- --------------------------------------------------------------------------------
-- Listado de propiedades DISPONIBLES para alquiler
-- 
select * from propiedad where Id_Operacion_Comercial= 2 and Id_Estado= 1
-- -----------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------
-- Listado de propiedades vendidas
-- 
select * from propiedad where Id_Operacion_Comercial= 1 and Id_Estado= 2
-- ---------------------------------------------------------------------------------

- --------------------------------------------------------------------------------
-- Listado de propiedades alquiladas
-- 
select * from propiedad where Id_Operacion_Comercial= 2 and Id_Estado= 2
-- ---------------------------------------------------------------------------------

-- select * from estado
-- select * from `operatoria comercial`
-- select * FROM propietario
-- select * FROM tipo
