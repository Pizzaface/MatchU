-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.1.34-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win32
-- HeidiSQL Version:             10.3.0.5771
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for matchu
CREATE DATABASE IF NOT EXISTS `matchu` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `matchu`;

-- Dumping structure for table matchu.alembic_version
CREATE TABLE IF NOT EXISTS `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table matchu.alembic_version: ~0 rows (approximately)
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;

-- Dumping structure for table matchu.groups
CREATE TABLE IF NOT EXISTS `groups` (
  `id` varchar(5) NOT NULL,
  `name` varchar(25) NOT NULL,
  `project_id` varchar(50) NOT NULL,
  `solution_desc` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table matchu.groups: ~0 rows (approximately)
/*!40000 ALTER TABLE `groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `groups` ENABLE KEYS */;

-- Dumping structure for table matchu.projects
CREATE TABLE IF NOT EXISTS `projects` (
  `project_id` varchar(80) NOT NULL,
  `project_name` varchar(100) DEFAULT NULL,
  `user_id` varchar(80) NOT NULL DEFAULT '',
  `description` text NOT NULL,
  PRIMARY KEY (`project_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table matchu.projects: ~1 rows (approximately)
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
INSERT INTO `projects` (`project_id`, `project_name`, `user_id`, `description`) VALUES
	('ntqyDyReQMffiKOlDdyyNKLglyYDap2gt75OQwH7y1ZZ3bBRGX', 'Hello world!', 'YI5CNptpejWDM1Te7UDf3jvVlek1XEAuQuHNCoWJCkKxgner7J', 'testing! ');
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;

-- Dumping structure for table matchu.students_to_projects
CREATE TABLE IF NOT EXISTS `students_to_projects` (
  `id` int(11) DEFAULT NULL,
  `project_id` varchar(80) DEFAULT NULL,
  `user_id` varchar(80) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table matchu.students_to_projects: ~0 rows (approximately)
/*!40000 ALTER TABLE `students_to_projects` DISABLE KEYS */;
/*!40000 ALTER TABLE `students_to_projects` ENABLE KEYS */;

-- Dumping structure for table matchu.student_to_groups
CREATE TABLE IF NOT EXISTS `student_to_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(50) NOT NULL DEFAULT '',
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK__users` (`user_id`),
  CONSTRAINT `FK__users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table matchu.student_to_groups: ~0 rows (approximately)
/*!40000 ALTER TABLE `student_to_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `student_to_groups` ENABLE KEYS */;

-- Dumping structure for table matchu.users
CREATE TABLE IF NOT EXISTS `users` (
  `id` varchar(50) NOT NULL,
  `username` varchar(80) NOT NULL,
  `password` text NOT NULL,
  `user_type` varchar(20) NOT NULL,
  `email` varchar(120) NOT NULL,
  `schedule` text NOT NULL,
  `activation_token` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table matchu.users: ~1 rows (approximately)
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`id`, `username`, `password`, `user_type`, `email`, `schedule`, `activation_token`) VALUES
	('YI5CNptpejWDM1Te7UDf3jvVlek1XEAuQuHNCoWJCkKxgner7J', 'test', 'pbkdf2:sha256:150000$MZTTfKan$1ec3c97e23dcdc420679a737aa1f09ae111e70f2af99ce4d997945f15b918e34', 'teacher', 'test@example.com', '{}', 'Gb5Cs4FFEDfvwFmRLInW3yJwnBkLEaj2ampKWSW1IUt6HwQy7V');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
