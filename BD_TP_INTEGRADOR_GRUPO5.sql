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

