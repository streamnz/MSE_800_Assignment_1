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

 Date: 29/08/2024 20:35:40
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for USERS
-- ----------------------------
DROP TABLE IF EXISTS `USERS`;
CREATE TABLE `USERS` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `role` varchar(50) NOT NULL,
  `is_del` tinyint(1) DEFAULT '0',
  `create_date` datetime NOT NULL,
  `create_by` varchar(255) DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  `update_by` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of USERS
-- ----------------------------
BEGIN;
INSERT INTO `USERS` (`user_id`, `username`, `password`, `email`, `role`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (1, 'Customer1', 'Customer1', 'kristalopez@example.org', 'customer', 0, '2024-05-07 00:00:00', 'admin', '2024-02-03 00:00:00', 'admin');
INSERT INTO `USERS` (`user_id`, `username`, `password`, `email`, `role`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (2, 'Customer2', 'Customer2', 'melanie58@example.com', 'customer', 0, '2024-04-18 00:00:00', 'admin', '2024-08-09 00:00:00', 'admin');
INSERT INTO `USERS` (`user_id`, `username`, `password`, `email`, `role`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (3, 'Customer3', 'Customer3', 'yvaldez@example.net', 'customer', 0, '2024-05-08 00:00:00', 'admin', '2024-03-19 00:00:00', 'admin');
INSERT INTO `USERS` (`user_id`, `username`, `password`, `email`, `role`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (4, 'Customer4', 'Customer4', 'karen56@example.net', 'customer', 0, '2024-06-05 00:00:00', 'admin', '2024-06-23 00:00:00', 'admin');
INSERT INTO `USERS` (`user_id`, `username`, `password`, `email`, `role`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (5, 'Customer5', 'Customer5', 'robertjackson@example.org', 'customer', 0, '2024-08-15 00:00:00', 'admin', '2024-05-02 00:00:00', 'admin');
INSERT INTO `USERS` (`user_id`, `username`, `password`, `email`, `role`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (6, 'Customer6', 'Customer6', 'heathermorales@example.com', 'customer', 0, '2024-04-05 00:00:00', 'admin', '2024-07-13 00:00:00', 'admin');
INSERT INTO `USERS` (`user_id`, `username`, `password`, `email`, `role`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (7, 'Customer7', 'Customer7', 'shawn63@example.com', 'customer', 0, '2024-02-24 00:00:00', 'admin', '2024-06-15 00:00:00', 'admin');
INSERT INTO `USERS` (`user_id`, `username`, `password`, `email`, `role`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (8, 'Customer8', 'Customer8', 'gravesandrew@example.com', 'customer', 0, '2024-02-22 00:00:00', 'admin', '2024-08-17 00:00:00', 'admin');
INSERT INTO `USERS` (`user_id`, `username`, `password`, `email`, `role`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (9, 'Customer9', 'Customer9', 'morganspencer@example.com', 'customer', 0, '2024-06-27 00:00:00', 'admin', '2024-01-02 00:00:00', 'admin');
INSERT INTO `USERS` (`user_id`, `username`, `password`, `email`, `role`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (10, 'Customer10', 'Customer10', 'lori80@example.com', 'customer', 0, '2024-01-27 00:00:00', 'admin', '2024-03-18 00:00:00', 'admin');
INSERT INTO `USERS` (`user_id`, `username`, `password`, `email`, `role`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (11, 'Customer11', 'Customer11', 'ebrown@example.com', 'customer', 0, '2024-03-24 00:00:00', 'admin', '2024-07-17 00:00:00', 'admin');
INSERT INTO `USERS` (`user_id`, `username`, `password`, `email`, `role`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (12, 'Customer12', 'Customer12', 'solomonjodi@example.com', 'customer', 0, '2024-05-20 00:00:00', 'admin', '2024-04-24 00:00:00', 'admin');
INSERT INTO `USERS` (`user_id`, `username`, `password`, `email`, `role`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (13, 'Customer13', 'Customer13', 'schultzmichelle@example.com', 'customer', 0, '2024-02-14 00:00:00', 'admin', '2024-04-02 00:00:00', 'admin');
INSERT INTO `USERS` (`user_id`, `username`, `password`, `email`, `role`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (14, 'Customer14', 'Customer14', 'iwilson@example.org', 'customer', 0, '2024-05-30 00:00:00', 'admin', '2024-02-02 00:00:00', 'admin');
INSERT INTO `USERS` (`user_id`, `username`, `password`, `email`, `role`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (15, 'Customer15', 'Customer15', 'anna99@example.org', 'customer', 0, '2024-08-22 00:00:00', 'admin', '2024-06-02 00:00:00', 'admin');
INSERT INTO `USERS` (`user_id`, `username`, `password`, `email`, `role`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (16, 'Customer16', 'Customer16', 'ebowman@example.com', 'customer', 0, '2024-03-16 00:00:00', 'admin', '2024-07-17 00:00:00', 'admin');
INSERT INTO `USERS` (`user_id`, `username`, `password`, `email`, `role`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (17, 'Customer17', 'Customer17', 'antonio38@example.net', 'customer', 0, '2024-02-12 00:00:00', 'admin', '2024-05-01 00:00:00', 'admin');
INSERT INTO `USERS` (`user_id`, `username`, `password`, `email`, `role`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (18, 'Customer18', 'Customer18', 'amyfloyd@example.com', 'customer', 0, '2024-08-23 00:00:00', 'admin', '2024-06-06 00:00:00', 'admin');
INSERT INTO `USERS` (`user_id`, `username`, `password`, `email`, `role`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (19, 'Customer19', 'Customer19', 'travis12@example.org', 'customer', 0, '2024-05-02 00:00:00', 'admin', '2024-02-20 00:00:00', 'admin');
INSERT INTO `USERS` (`user_id`, `username`, `password`, `email`, `role`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (20, 'Customer20', 'Customer20', 'walexander@example.org', 'customer', 0, '2024-02-18 00:00:00', 'admin', '2024-07-14 00:00:00', 'admin');
INSERT INTO `USERS` (`user_id`, `username`, `password`, `email`, `role`, `is_del`, `create_date`, `create_by`, `update_date`, `update_by`) VALUES (21, 'admin', 'admin', 'admin@example.org', 'admin', 0, '2024-08-28 22:14:20', 'admin', NULL, NULL);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
