

CREATE TABLE IF NOT EXISTS `mbtechsc_credit_scoring_database`.`firm_data` (
  `firm_data_id` INT(11) NOT NULL,
  `registeration_number` VARCHAR(200) NOT NULL,
  `firm_name` VARCHAR(200) NOT NULL,
  `established_date` VARCHAR(200) NOT NULL,
  `number_of_employes` INT(11) NOT NULL,
  `country` VARCHAR(200) NOT NULL,
  `last_update_time_stamp` DATE NOT NULL,
  PRIMARY KEY (`registeration_number`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8

CREATE TABLE IF NOT EXISTS `mbtechsc_credit_scoring_database`.`personal_data` (
  `person_id` INT(11) NOT NULL,
  `fiscal_code` VARCHAR(200) NOT NULL,
  `first_name` VARCHAR(200) NOT NULL,
  `last_name` VARCHAR(200) NOT NULL,
  `sex` INT(11) NOT NULL,
  `date_of_birth` VARCHAR(200) NOT NULL,
  `ethnicity` VARCHAR(200) NOT NULL,
  `highest_degree` VARCHAR(200) NOT NULL,
  `address` VARCHAR(200) NOT NULL,
  `email` VARCHAR(200) NOT NULL,
  `phone_number` VARCHAR(200) NOT NULL,
  `state` VARCHAR(200) NOT NULL,
  `firm_registration` VARCHAR(200) NOT NULL,
  `last_update_time_stamp` DATE NOT NULL,
  PRIMARY KEY (`fiscal_code`),
  INDEX `PD_firm_id_idx` (`firm_registration` ASC),
  CONSTRAINT `PD_firm_id`
    FOREIGN KEY (`firm_registration`)
    REFERENCES `mbtechsc_credit_scoring_database`.`firm_data` (`registeration_number`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8

CREATE TABLE IF NOT EXISTS `mbtechsc_credit_scoring_database`.`assets` (
  `asset_id` INT(11) NOT NULL,
  `total_amount_of_house` FLOAT NOT NULL,
  `monthly_income` FLOAT NOT NULL,
  `savings` FLOAT NOT NULL,
  `other_savings` FLOAT NOT NULL,
  `last_updated_time_stamp` DATE NOT NULL,
  `fiscal_code_fk` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`asset_id`),
  INDEX `A_fiscal_code_idx` (`fiscal_code_fk` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8

CREATE TABLE IF NOT EXISTS `mbtechsc_credit_scoring_database`.`assets` (
  `asset_id` INT(11) NOT NULL,
  `total_amount_of_house` FLOAT NOT NULL,
  `monthly_income` FLOAT NOT NULL,
  `savings` FLOAT NOT NULL,
  `other_savings` FLOAT NOT NULL,
  `last_updated_time_stamp` DATE NOT NULL,
  `fiscal_code_fk` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`asset_id`),
  INDEX `A_fiscal_code_idx` (`fiscal_code_fk` ASC),
  CONSTRAINT `A_FC`
    FOREIGN KEY (`fiscal_code_fk`)
    REFERENCES `mbtechsc_credit_scoring_database`.`personal_data` (`fiscal_code`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8

CREATE TABLE IF NOT EXISTS `mbtechsc_credit_scoring_database`.`bank_data` (
  `bank_data_id` INT(11) NOT NULL,
  `bank_name` VARCHAR(2000) NOT NULL,
  `bank_country` VARCHAR(2000) NOT NULL,
  PRIMARY KEY (`bank_data_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1

CREATE TABLE IF NOT EXISTS `mbtechsc_credit_scoring_database`.`bank_person_relationships` (
  `bank_person_relationships_id` INT(11) NOT NULL,
  `bank_id` INT(11) NOT NULL,
  `person_id` VARCHAR(200) NOT NULL,
  `last_update_time_stamp` DATE NOT NULL,
  PRIMARY KEY (`bank_person_relationships_id`),
  INDEX `bp_fiscal_code_idx` (`person_id` ASC),
  INDEX `BPD_FK` (`bank_id` ASC),
  CONSTRAINT `BPD_FK`
    FOREIGN KEY (`bank_id`)
    REFERENCES `mbtechsc_credit_scoring_database`.`bank_data` (`bank_data_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8


CREATE TABLE IF NOT EXISTS `mbtechsc_credit_scoring_database`.`credit_data` (
  `credit_data_id` INT(11) NOT NULL,
  `firm_registeration_number` VARCHAR(200) NOT NULL,
  `amount_of_credit` FLOAT NOT NULL,
  `purpose` VARCHAR(200) NOT NULL,
  `duration_in_months` INT(11) NOT NULL,
  `last_update_time_stamp` TIME NOT NULL,
  PRIMARY KEY (`credit_data_id`),
  INDEX `firm_registeration_number_idx` (`firm_registeration_number` ASC) ,
  CONSTRAINT `CD_FC`
    FOREIGN KEY (`firm_registeration_number`)
    REFERENCES `mbtechsc_credit_scoring_database`.`firm_data` (`registeration_number`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8


CREATE TABLE IF NOT EXISTS `mbtechsc_credit_scoring_database`.`credit_history` (
  `credit_history_id` INT(11) NOT NULL,
  `from30to60` INT(11) NOT NULL,
  `from60to90` INT(11) NOT NULL,
  `more_than_90` INT(11) NOT NULL,
  `insolvent_ammount` FLOAT NOT NULL,
  `last_update_time_stamp` DATE NOT NULL,
  `fiscal_code_fk` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`credit_history_id`),
  INDEX `CH_fiscal_code_idx` (`fiscal_code_fk` ASC),
  CONSTRAINT `CH_FC`
    FOREIGN KEY (`fiscal_code_fk`)
    REFERENCES `mbtechsc_credit_scoring_database`.`personal_data` (`fiscal_code`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8


CREATE TABLE IF NOT EXISTS `mbtechsc_credit_scoring_database`.`credit_mix` (
  `credit_mix_id` INT(11) NOT NULL,
  `installment` VARCHAR(200) NOT NULL,
  `house_mortgage` FLOAT NOT NULL,
  `credit_card_number` VARCHAR(200) NOT NULL,
  `last_update_time_stamp` DATE NOT NULL,
  `fiscal_code_fk` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`credit_mix_id`),
  INDEX `CM_fiscal_code_idx` (`fiscal_code_fk` ASC) ,
  CONSTRAINT `CM_FC`
    FOREIGN KEY (`fiscal_code_fk`)
    REFERENCES `mbtechsc_credit_scoring_database`.`personal_data` (`fiscal_code`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8


CREATE TABLE IF NOT EXISTS `mbtechsc_credit_scoring_database`.`criminal_records` (
  `criminal_id` INT(11) NOT NULL,
  `bankrupty` TINYINT(4) NOT NULL,
  `investigation` TINYINT(4) NOT NULL,
  `accused` TINYINT(4) NOT NULL,
  `condemned` TINYINT(4) NOT NULL,
  `civ_pass` TINYINT(4) NOT NULL,
  `last_updated_time_stamp` DATE NOT NULL,
  `fiscal_code_fk` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`criminal_id`),
  INDEX `CR_fiscal_code_idx` (`fiscal_code_fk` ASC),
  CONSTRAINT `CR_FC`
    FOREIGN KEY (`fiscal_code_fk`)
    REFERENCES `mbtechsc_credit_scoring_database`.`personal_data` (`fiscal_code`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8



CREATE TABLE IF NOT EXISTS `mbtechsc_credit_scoring_database`.`losses` (
  `losses_id` INT(11) NOT NULL,
  `actual_debit_credit_cards` INT(11) NOT NULL,
  `amount_due_mortgage` FLOAT NOT NULL,
  `last_update_time_stamp` DATE NOT NULL,
  `fiscal_code_fk` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`losses_id`),
  INDEX `L_fical_code_idx` (`fiscal_code_fk` ASC) ,
  CONSTRAINT `L_FC`
    FOREIGN KEY (`fiscal_code_fk`)
    REFERENCES `mbtechsc_credit_scoring_database`.`personal_data` (`fiscal_code`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8



CREATE TABLE IF NOT EXISTS `mbtechsc_credit_scoring_database`.`new_credit` (
  `new_credit_id` INT(11) NOT NULL,
  `amount_in_12_months` FLOAT NOT NULL,
  `amount_in_6_months` FLOAT NOT NULL,
  `amount_in_18_months` FLOAT NOT NULL,
  `last_update_time_stamp` DATE NOT NULL,
  `fiscal_code_fk` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`new_credit_id`),
  INDEX `fk_idx` (`fiscal_code_fk` ASC),
  CONSTRAINT `NC_FC`
    FOREIGN KEY (`fiscal_code_fk`)
    REFERENCES `mbtechsc_credit_scoring_database`.`personal_data` (`fiscal_code`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
