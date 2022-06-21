-- TODO:  just an example to remember the syntax, must be rewritten

-- CREATE DB

CREATE DATABASE IF NOT EXISTS `BDT_PROJECT_2022` DEFAULT CHARACTER SET utf8;
USE `FLOW_DB`;

CREATE TABLE IF NOT EXISTS `BANK`(
	`ID` INT AUTO_INCREMENT NOT NULL COMMENT 'Primary key', -- PRIMARY KEY
	`PROFILE` VARCHAR(45) NOT NULL COMMENT 'Bank user code',
	`NAME` VARCHAR(45) NOT NULL COMMENT 'Bank name',
    `COUNTRY` VARCHAR(45) NOT NULL COMMENT 'Bank country',

	`last_updated` DATE NOT NULL COMMENT 'last time the record was updated',

	PRIMARY KEY(`ID`),
	UNIQUE INDEX `ID_UNIQUE`(`ID`),
	key(`NOME`)
	);

CREATE TABLE IF NOT EXISTS `BANK_USER`(
    `ID` INT AUTO_INCREMENT NOT NULL COMMENT 'Primary key', -- PRIMARY KEY
    `NAME` VARCHAR(45) NOT NULL COMMENT 'Bank client name',
	`PROFILE` VARCHAR(45) NOT NULL COMMENT 'Bank registration number',
	`EMPLOYEES` INT DEFAULT 10 COMMENT 'N° of employees of the bank user',
    `EMAIL` VARCHAR(45) NOT NULL COMMENT 'Bank client email',
	`last_updated` DATE NOT NULL COMMENT 'last time the record was updated',

	PRIMARY KEY(`ID`),
	UNIQUE INDEX `ID_UNIQUE`(`ID`),
	key(`NOME`)
	);
`DATE` DATE NOT NULL 'Established date',
