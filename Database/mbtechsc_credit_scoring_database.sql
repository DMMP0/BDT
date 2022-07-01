-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 30, 2022 at 10:21 PM
-- Server version: 5.7.33
-- PHP Version: 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mbtechsc_credit_scoring_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `assets`
--

CREATE TABLE `assets` (
  `asset_id` int(11) NOT NULL,
  `total_amount_of_house` float NOT NULL,
  `monthly_income` float NOT NULL,
  `savings` float NOT NULL,
  `other_savings` float NOT NULL,
  `last_updated_time_stamp` date NOT NULL,
  `fiscal_code_fk` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `bank_data`
--

CREATE TABLE `bank_data` (
  `bank_data_id` int(11) NOT NULL,
  `bank_name` varchar(2000) NOT NULL,
  `bank_country` varchar(2000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `bank_person_relationships`
--

CREATE TABLE `bank_person_relationships` (
  `bank_person_relationships_id` int(11) NOT NULL,
  `bank_id` int(11) NOT NULL,
  `person_id` varchar(200) NOT NULL,
  `last_update_time_stamp` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `credit_data`
--

CREATE TABLE `credit_data` (
  `credit_data_id` int(11) NOT NULL,
  `firm_registeration_number` varchar(200) NOT NULL,
  `amount_of_credit` float NOT NULL,
  `purpose` varchar(200) NOT NULL,
  `duration_in_months` int(11) NOT NULL,
  `last_update_time_stamp` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `credit_history`
--

CREATE TABLE `credit_history` (
  `credit_history_id` int(11) NOT NULL,
  `from30to60` int(11) NOT NULL,
  `from60to90` int(11) NOT NULL,
  `more_than_90` int(11) NOT NULL,
  `insolvent_ammount` float NOT NULL,
  `last_update_time_stamp` date NOT NULL,
  `fiscal_code_fk` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `credit_mix`
--

CREATE TABLE `credit_mix` (
  `credit_mix_id` int(11) NOT NULL,
  `installment` varchar(200) NOT NULL,
  `house_mortgage` float NOT NULL,
  `credit_card_number` varchar(200) NOT NULL,
  `last_update_time_stamp` date NOT NULL,
  `fiscal_code_fk` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `criminal_records`
--

CREATE TABLE `criminal_records` (
  `criminal_id` int(11) NOT NULL,
  `bankrupty` tinyint(4) NOT NULL,
  `investigation` tinyint(4) NOT NULL,
  `accused` tinyint(4) NOT NULL,
  `condemned` tinyint(4) NOT NULL,
  `civ_pass` tinyint(4) NOT NULL,
  `last_updated_time_stamp` date NOT NULL,
  `fiscal_code_fk` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `firm_data`
--

CREATE TABLE `firm_data` (
  `firm_data_id` int(11) NOT NULL,
  `registeration_number` varchar(200) NOT NULL,
  `firm_name` varchar(200) NOT NULL,
  `established_date` varchar(200) NOT NULL,
  `number_of_employes` int(11) NOT NULL,
  `country` varchar(200) NOT NULL,
  `last_update_time_stamp` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `losses`
--

CREATE TABLE `losses` (
  `losses_id` int(11) NOT NULL,
  `actual_debit_credit_cards` int(11) NOT NULL,
  `amount_due_mortgage` float NOT NULL,
  `last_update_time_stamp` date NOT NULL,
  `fiscal_code_fk` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `new_credit`
--

CREATE TABLE `new_credit` (
  `new_credit_id` int(11) NOT NULL,
  `amount_in_12_months` float NOT NULL,
  `amount_in_6_months` float NOT NULL,
  `amount_in_18_months` float NOT NULL,
  `last_update_time_stamp` date NOT NULL,
  `fiscal_code_fk` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `personal_data`
--

CREATE TABLE `personal_data` (
  `person_id` int(11) NOT NULL,
  `fiscal_code` varchar(200) NOT NULL,
  `first_name` varchar(200) NOT NULL,
  `last_name` varchar(200) NOT NULL,
  `sex` int(11) NOT NULL,
  `date_of_birth` varchar(200) NOT NULL,
  `ethnicity` varchar(200) NOT NULL,
  `highest_degree` varchar(200) NOT NULL,
  `address` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `phone_number` varchar(200) NOT NULL,
  `state` varchar(200) NOT NULL,
  `firm_registration` varchar(200) NOT NULL,
  `last_update_time_stamp` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `assets`
--
ALTER TABLE `assets`
  ADD PRIMARY KEY (`asset_id`),
  ADD KEY `A_fiscal_code_idx` (`fiscal_code_fk`);

--
-- Indexes for table `bank_data`
--
ALTER TABLE `bank_data`
  ADD PRIMARY KEY (`bank_data_id`);

--
-- Indexes for table `bank_person_relationships`
--
ALTER TABLE `bank_person_relationships`
  ADD PRIMARY KEY (`bank_person_relationships_id`),
  ADD KEY `bp_fiscal_code_idx` (`person_id`),
  ADD KEY `BPD_FK` (`bank_id`);

--
-- Indexes for table `credit_data`
--
ALTER TABLE `credit_data`
  ADD PRIMARY KEY (`credit_data_id`),
  ADD KEY `firm_registeration_number_idx` (`firm_registeration_number`);

--
-- Indexes for table `credit_history`
--
ALTER TABLE `credit_history`
  ADD PRIMARY KEY (`credit_history_id`),
  ADD KEY `CH_fiscal_code_idx` (`fiscal_code_fk`);

--
-- Indexes for table `credit_mix`
--
ALTER TABLE `credit_mix`
  ADD PRIMARY KEY (`credit_mix_id`),
  ADD KEY `CM_fiscal_code_idx` (`fiscal_code_fk`);

--
-- Indexes for table `criminal_records`
--
ALTER TABLE `criminal_records`
  ADD PRIMARY KEY (`criminal_id`),
  ADD KEY `CR_fiscal_code_idx` (`fiscal_code_fk`);

--
-- Indexes for table `firm_data`
--
ALTER TABLE `firm_data`
  ADD PRIMARY KEY (`registeration_number`);

--
-- Indexes for table `losses`
--
ALTER TABLE `losses`
  ADD PRIMARY KEY (`losses_id`),
  ADD KEY `L_fical_code_idx` (`fiscal_code_fk`);

--
-- Indexes for table `new_credit`
--
ALTER TABLE `new_credit`
  ADD PRIMARY KEY (`new_credit_id`),
  ADD KEY `fk_idx` (`fiscal_code_fk`);

--
-- Indexes for table `personal_data`
--
ALTER TABLE `personal_data`
  ADD PRIMARY KEY (`fiscal_code`),
  ADD KEY `PD_firm_id_idx` (`firm_registration`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `assets`
--
ALTER TABLE `assets`
  ADD CONSTRAINT `A_FK` FOREIGN KEY (`fiscal_code_fk`) REFERENCES `personal_data` (`fiscal_code`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `bank_person_relationships`
--
ALTER TABLE `bank_person_relationships`
  ADD CONSTRAINT `BPD_FK` FOREIGN KEY (`bank_id`) REFERENCES `bank_data` (`bank_data_id`),
  ADD CONSTRAINT `PI_FK` FOREIGN KEY (`person_id`) REFERENCES `personal_data` (`fiscal_code`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `credit_data`
--
ALTER TABLE `credit_data`
  ADD CONSTRAINT `CD_FC` FOREIGN KEY (`firm_registeration_number`) REFERENCES `firm_data` (`registeration_number`);

--
-- Constraints for table `credit_history`
--
ALTER TABLE `credit_history`
  ADD CONSTRAINT `CH_FC` FOREIGN KEY (`fiscal_code_fk`) REFERENCES `personal_data` (`fiscal_code`);

--
-- Constraints for table `credit_mix`
--
ALTER TABLE `credit_mix`
  ADD CONSTRAINT `CM_FC` FOREIGN KEY (`fiscal_code_fk`) REFERENCES `personal_data` (`fiscal_code`);

--
-- Constraints for table `criminal_records`
--
ALTER TABLE `criminal_records`
  ADD CONSTRAINT `CR_FC` FOREIGN KEY (`fiscal_code_fk`) REFERENCES `personal_data` (`fiscal_code`);

--
-- Constraints for table `losses`
--
ALTER TABLE `losses`
  ADD CONSTRAINT `L_FC` FOREIGN KEY (`fiscal_code_fk`) REFERENCES `personal_data` (`fiscal_code`);

--
-- Constraints for table `new_credit`
--
ALTER TABLE `new_credit`
  ADD CONSTRAINT `NC_FC` FOREIGN KEY (`fiscal_code_fk`) REFERENCES `personal_data` (`fiscal_code`);

--
-- Constraints for table `personal_data`
--
ALTER TABLE `personal_data`
  ADD CONSTRAINT `PD_firm_id` FOREIGN KEY (`firm_registration`) REFERENCES `firm_data` (`registeration_number`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
