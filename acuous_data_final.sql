-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema acuous_data
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema acuous_data
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `acuous_data` DEFAULT CHARACTER SET utf8 ;
USE `acuous_data` ;

-- -----------------------------------------------------
-- Table `acuous_data`.`urinalysis_information`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `acuous_data`.`urinalysis_information` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `blood` TINYINT(1) NOT NULL,
  `bilirubin` TINYINT(1) NOT NULL,
  `urobilinogen` TINYINT(1) NOT NULL,
  `ketones` TINYINT(1) NOT NULL,
  `protein` TINYINT(1) NOT NULL,
  `glucose` TINYINT(1) NOT NULL,
  `pH` ENUM('Acid', 'Neutral', 'Base') NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `acuous_data`.`patients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `acuous_data`.`patients` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `patient_number` INT NOT NULL,
  `age` INT NOT NULL,
  `sex` ENUM('M', 'F') NOT NULL,
  `medical_diagnosis` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `acuous_data`.`urine_information`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `acuous_data`.`urine_information` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `datetime` DATETIME NOT NULL,
  `volume` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
