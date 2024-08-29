/*
 Navicat MySQL Dump SQL

 Source Server         : docker_mysql
 Source Server Type    : MySQL
 Source Server Version : 90001 (9.0.1)
 Source Host           : localhost:3306
 Source Schema         : MSE800

 Target Server Type    : MySQL
 Target Server Version : 90001 (9.0.1)
 File Encoding         : 65001

 Date: 29/08/2024 20:35:19
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for CARS
-- ----------------------------
DROP TABLE IF EXISTS `CARS`;
CREATE TABLE `CARS` (
  `car_id` int NOT NULL AUTO_INCREMENT,
  `make` varchar(255) NOT NULL,
  `model` varchar(255) NOT NULL,
  `year` int NOT NULL,
  `license_plate` varchar(255) NOT NULL,
  `mileage` float NOT NULL,
  `status` varchar(50) NOT NULL,
  `is_del` tinyint(1) DEFAULT '0',
  `create_date` datetime NOT NULL,
  `create_by` varchar(255) DEFAULT NULL,
  `update_date` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `update_by` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`car_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of CARS
-- ----------------------------
BEGIN;
INSERT INTO `CARS` (`car_id`, `make`, `model`, `year`, `license_plate`, `mileage`, `status`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (1, 'Wright-Baker', 'under', 2008, '810 QRZ', 86371.7, 'Booked', 0, '2024-08-26 00:00:00', 'admin', '2024-04-22 00:00:00', 'admin');
INSERT INTO `CARS` (`car_id`, `make`, `model`, `year`, `license_plate`, `mileage`, `status`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (2, 'Lee Group', 'generation', 2012, '2E 5T6DCM', 87384.2, 'Maintenance', 0, '2024-05-27 00:00:00', 'admin', '2024-01-18 00:00:00', 'admin');
INSERT INTO `CARS` (`car_id`, `make`, `model`, `year`, `license_plate`, `mileage`, `status`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (3, 'Owen-Johnson', 'so', 2007, '5O R2444', 172919, 'Rented', 0, '2024-07-21 00:00:00', 'admin', '2024-02-27 00:00:00', 'admin');
INSERT INTO `CARS` (`car_id`, `make`, `model`, `year`, `license_plate`, `mileage`, `status`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (4, 'Salinas, Parker and Hutchinson', 'key', 2000, 'MCQ 843', 191751, 'Maintenance', 0, '2024-07-10 00:00:00', 'admin', '2024-04-27 00:00:00', 'admin');
INSERT INTO `CARS` (`car_id`, `make`, `model`, `year`, `license_plate`, `mileage`, `status`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (5, 'White PLC', 'thought', 2007, '01AZ2', 132646, 'Available', 0, '2024-07-21 00:00:00', 'admin', '2024-06-27 00:00:00', 'admin');
INSERT INTO `CARS` (`car_id`, `make`, `model`, `year`, `license_plate`, `mileage`, `status`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (6, 'Davis, Wright and Lopez', 'local', 2016, 'DNY-9559', 74221.2, 'Maintenance', 0, '2024-05-06 00:00:00', 'admin', '2024-04-11 00:00:00', 'admin');
INSERT INTO `CARS` (`car_id`, `make`, `model`, `year`, `license_plate`, `mileage`, `status`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (7, 'Long-Moreno', 'second', 2008, '015-VWX', 160703, 'Booked', 0, '2024-07-14 00:00:00', 'admin', '2024-02-29 00:00:00', 'admin');
INSERT INTO `CARS` (`car_id`, `make`, `model`, `year`, `license_plate`, `mileage`, `status`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (8, 'Michael-Stone', 'so', 2017, '97FP5', 101160, 'Rented', 0, '2024-01-05 00:00:00', 'admin', '2024-05-08 00:00:00', 'admin');
INSERT INTO `CARS` (`car_id`, `make`, `model`, `year`, `license_plate`, `mileage`, `status`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (9, 'Johnson, King and Byrd', 'money', 2013, 'NUJ-096', 86726.2, 'Available', 0, '2024-06-29 00:00:00', 'admin', '2024-01-29 00:00:00', 'admin');
INSERT INTO `CARS` (`car_id`, `make`, `model`, `year`, `license_plate`, `mileage`, `status`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (10, 'Gibson, West and Chan', 'white', 2019, '8N 26553', 138057, 'Available', 0, '2024-03-13 00:00:00', 'admin', '2024-07-01 00:00:00', 'admin');
INSERT INTO `CARS` (`car_id`, `make`, `model`, `year`, `license_plate`, `mileage`, `status`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (11, 'Andersen, Cohen and Wilkins', 'speech', 2000, 'LFD 184', 48222.5, 'Rented', 0, '2024-03-06 00:00:00', 'admin', '2024-04-26 00:00:00', 'admin');
INSERT INTO `CARS` (`car_id`, `make`, `model`, `year`, `license_plate`, `mileage`, `status`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (12, 'Gregory-Adams', 'pattern', 2017, '4QC1978', 118235, 'Available', 0, '2024-02-03 00:00:00', 'admin', '2024-01-24 00:00:00', 'admin');
INSERT INTO `CARS` (`car_id`, `make`, `model`, `year`, `license_plate`, `mileage`, `status`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (13, 'Fuller and Sons', 'wish', 2021, '6-H5122', 198563, 'Booked', 0, '2024-02-29 00:00:00', 'admin', '2024-08-17 00:00:00', 'admin');
INSERT INTO `CARS` (`car_id`, `make`, `model`, `year`, `license_plate`, `mileage`, `status`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (14, 'Castro Group', 'environment', 2015, '403 2LS', 62392.3, 'Available', 0, '2024-01-08 00:00:00', 'admin', '2024-01-30 00:00:00', 'admin');
INSERT INTO `CARS` (`car_id`, `make`, `model`, `year`, `license_plate`, `mileage`, `status`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (15, 'Williams-Tran', 'beat', 2021, '5RF 366', 81057, 'Maintenance', 0, '2024-06-03 00:00:00', 'admin', '2024-07-13 00:00:00', 'admin');
INSERT INTO `CARS` (`car_id`, `make`, `model`, `year`, `license_plate`, `mileage`, `status`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (16, 'Miller, Snyder and Reeves', 'stop', 2011, '3O GG278', 168404, 'Booked', 0, '2024-02-19 00:00:00', 'admin', '2024-03-19 00:00:00', 'admin');
INSERT INTO `CARS` (`car_id`, `make`, `model`, `year`, `license_plate`, `mileage`, `status`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (17, 'Jones, Gregory and Smith', 'for', 2023, '06G 7604', 79010.7, 'Rented', 0, '2024-07-14 00:00:00', 'admin', '2024-07-20 00:00:00', 'admin');
INSERT INTO `CARS` (`car_id`, `make`, `model`, `year`, `license_plate`, `mileage`, `status`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (18, 'Mendoza PLC', 'so', 2009, '469FXH', 63972.6, 'Booked', 0, '2024-08-01 00:00:00', 'admin', '2024-05-30 00:00:00', 'admin');
INSERT INTO `CARS` (`car_id`, `make`, `model`, `year`, `license_plate`, `mileage`, `status`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (19, 'Hernandez, Lin and Singh', 'challenge', 2006, '9IZ S30', 60293.2, 'Rented', 0, '2024-03-04 00:00:00', 'admin', '2024-05-02 00:00:00', 'admin');
INSERT INTO `CARS` (`car_id`, `make`, `model`, `year`, `license_plate`, `mileage`, `status`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (20, 'Dillon, Hill and Velez', 'scientist', 2013, 'MYR 205', 24010.2, 'Rented', 0, '2024-03-27 00:00:00', 'admin', '2024-08-21 00:00:00', 'admin');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
