-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.1.34-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win32
-- HeidiSQL Version:             11.0.0.5919
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
  PRIMARY KEY (`id`),
  KEY `FK_groups_projects` (`project_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table matchu.groups: ~1 rows (approximately)
/*!40000 ALTER TABLE `groups` DISABLE KEYS */;
INSERT INTO `groups` (`id`, `name`, `project_id`, `solution_desc`) VALUES
	('2oQJ9', 'Group #2', 'LvFxp3vNpOj7OJLyTx0Od6irsNMFWvKuKT4VkMe6QHwCgQ9Yh6', 'Describe your project here!'),
	('3dh1v', 'Auto-Assign Group', 'oLbuz6iDmBwEby19Pf0gPCyVJlPrzr0ipkOk6KzS3U2CBj2acu', 'This is a group that will auto assign you to the group with the best schedule'),
	('5EC6O', 'Auto-Assign Group', 'sdO7cF9y7uTDphQ8mabk7HBNPJxrGxiA2Uxr5LFiiJVf7T3Trq', 'This is a group that will auto assign you to the group with the best schedule'),
	('6Joos', 'Group #2', 'RS9JyPbUO2zI4leO8K2vrlnZiyKQU5IwKaisEie0RP72VgSdOu', 'Describe your project here!'),
	('8g6fx', 'Group #1', 'RS9JyPbUO2zI4leO8K2vrlnZiyKQU5IwKaisEie0RP72VgSdOu', 'Describe your project here!'),
	('Aq8Ym', 'Group #2', 'dzNQiaV2t1QFPzwyYoxlv3MizOEAcA71NHCuQpkFeeuJwTZiHh', 'Describe your project here!'),
	('cHiQa', 'Group #4', 'dzNQiaV2t1QFPzwyYoxlv3MizOEAcA71NHCuQpkFeeuJwTZiHh', 'Describe your project here!'),
	('EkmwR', 'Auto-Assign Group', 'PRvx0JNGYKwjTHMgHx1jRFEuI3by8nJKb2EQzoSQwCuv8aZdtJ', 'This is a group that will auto assign you to the group with the best schedule'),
	('F41nl', 'Group #4', 'XcNhA3S9S0DOepPaYOyx2YYzRvTGonF6wqQuDfD5n8mO5TDZKZ', 'Describe your project here!'),
	('glE53', 'Group #1', 'LvFxp3vNpOj7OJLyTx0Od6irsNMFWvKuKT4VkMe6QHwCgQ9Yh6', 'Describe your project here!'),
	('gmLhj', 'Group #1', 'dzNQiaV2t1QFPzwyYoxlv3MizOEAcA71NHCuQpkFeeuJwTZiHh', 'Describe your project here!'),
	('hfUbt', 'Group #3', 'LvFxp3vNpOj7OJLyTx0Od6irsNMFWvKuKT4VkMe6QHwCgQ9Yh6', 'Describe your project here!'),
	('JzBpC', 'Group #3', 'dzNQiaV2t1QFPzwyYoxlv3MizOEAcA71NHCuQpkFeeuJwTZiHh', 'Describe your project here!'),
	('Kz6W4', 'Auto-Assign Group', 'OJMOVruyQpTqP8pfbjXp7QFtXPTExU3sYnLGfCIWFiNDsxJQkT', 'This is a group that will auto assign you to the group with the best schedule'),
	('MAQ5W', 'Auto-Assign Group', 'wIK08H17kPtpnPHWPUMamr1Xb7kfK9bXKGZdBI6HFJ1tlJ1ouw', 'This is a group that will auto assign you to the group with the best schedule'),
	('oB2Fk', 'Group #0', 'LvFxp3vNpOj7OJLyTx0Od6irsNMFWvKuKT4VkMe6QHwCgQ9Yh6', 'Describe your project here!'),
	('OrF2L', 'Group #3', 'XcNhA3S9S0DOepPaYOyx2YYzRvTGonF6wqQuDfD5n8mO5TDZKZ', 'Describe your project here!'),
	('PlgLO', 'Group #1', 'XcNhA3S9S0DOepPaYOyx2YYzRvTGonF6wqQuDfD5n8mO5TDZKZ', 'Describe your project here!'),
	('q3q1X', 'Auto-Assign Group', 'sDSi6Dhnkkq8FYiXODvcTm7LksIXziAHKKg4dheypNmX2yfBHn', 'This is a group that will auto assign you to the group with the best schedule'),
	('QOdfz', 'Auto-Assign Group', 'dVOh2dpf4v45ONhZve3xAFoNGZCFONaYFyq9Z2dHRIKO33EjL1', 'This is a group that will auto assign you to the group with the best schedule'),
	('T97Sl', 'Group #4', 'RS9JyPbUO2zI4leO8K2vrlnZiyKQU5IwKaisEie0RP72VgSdOu', 'Describe your project here!'),
	('TYrdD', 'Group #3', 'RS9JyPbUO2zI4leO8K2vrlnZiyKQU5IwKaisEie0RP72VgSdOu', 'Describe your project here!'),
	('xQfCA', 'Auto-Assign Group', 'BXBRtF2gAkMxkqABLeLzq09aliAQFUy5572C2P4qKmXSCuVYbc', 'This is a group that will auto assign you to the group with the best schedule'),
	('zdFT8', 'Group #2', 'XcNhA3S9S0DOepPaYOyx2YYzRvTGonF6wqQuDfD5n8mO5TDZKZ', 'Describe your project here!');
/*!40000 ALTER TABLE `groups` ENABLE KEYS */;

-- Dumping structure for table matchu.projects
CREATE TABLE IF NOT EXISTS `projects` (
  `project_id` varchar(80) NOT NULL,
  `project_name` varchar(100) DEFAULT NULL,
  `user_id` varchar(80) NOT NULL DEFAULT '',
  `description` text NOT NULL,
  `nice_url` varchar(8) NOT NULL,
  `autoAssign_group_id` varchar(5) DEFAULT '',
  PRIMARY KEY (`project_id`),
  UNIQUE KEY `nice_url` (`nice_url`),
  KEY `FK_projects_groups` (`autoAssign_group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table matchu.projects: ~0 rows (approximately)
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;

-- Dumping structure for table matchu.students_to_projects
CREATE TABLE IF NOT EXISTS `students_to_projects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` varchar(80) NOT NULL,
  `user_id` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_students_to_projects_projects` (`project_id`),
  KEY `FK_students_to_projects_users` (`user_id`),
  CONSTRAINT `FK_students_to_projects_projects` FOREIGN KEY (`project_id`) REFERENCES `projects` (`project_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_students_to_projects_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=123 DEFAULT CHARSET=latin1;

-- Dumping data for table matchu.students_to_projects: ~0 rows (approximately)
/*!40000 ALTER TABLE `students_to_projects` DISABLE KEYS */;
/*!40000 ALTER TABLE `students_to_projects` ENABLE KEYS */;

-- Dumping structure for table matchu.student_to_groups
CREATE TABLE IF NOT EXISTS `student_to_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(50) NOT NULL DEFAULT '',
  `group_id` varchar(5) NOT NULL DEFAULT '',
  `project_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Index 3` (`user_id`,`group_id`,`project_id`) USING BTREE,
  KEY `FK_student_to_groups_groups` (`group_id`),
  KEY `FK_student_to_groups_projects` (`project_id`),
  CONSTRAINT `FK__users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_student_to_groups_groups` FOREIGN KEY (`group_id`) REFERENCES `groups` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_student_to_groups_projects` FOREIGN KEY (`project_id`) REFERENCES `projects` (`project_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=184 DEFAULT CHARSET=latin1;

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

-- Dumping data for table matchu.users: ~11 rows (approximately)
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`id`, `username`, `password`, `user_type`, `email`, `schedule`, `activation_token`) VALUES
	('74z4hkpTIf2i0D5krDLGgaeMtgPe2Osy6Ul1jTvAaQERbaJhQU', 'stu6', 'pbkdf2:sha256:150000$EB7OrIu9$37f8b63174a058d34391efb29f540798f110469944773a546d09eaf325f9e012', 'student', 'stu6@x.com', '{"mon": ["10:00", "17:00"], "wed": ["16:00", "22:00"], "fri": ["15:00", "20:00"]}', 'yjLlMz9RBQ0FkPqkF5a219itAucprD0VtB4kSNGxG8kWxpOVlf'),
	('8l31cL4ofEE7mbpWiq6rwOSmdYIB8yllAcZco3hUJVGfVn64Ib', 'stu7', 'pbkdf2:sha256:150000$Ce3DvNsE$dd2097ccbf62d600e2f4b8af8bb3e7096e0b182478cbf7f5fce1b810d6afd2f5', 'student', 'stu7@x.com', '{"sun": ["08:00", "17:00"], "mon": ["08:00", "17:00"], "tue": ["08:00", "17:00"], "wed": ["08:00", "17:00"], "thu": ["08:00", "17:00"], "fri": ["08:00", "17:00"], "sat": ["08:00", "17:00"]}', 'WtDXXlVBxwEqxlQN9fgmF6KX6VXR0Qm5EhzAyRz0FOA71Sqryr'),
	('bX3EuPqbY9P5JXwilE9Bfv2L2gliryYggr0dDH2Ci2oXyi6L2l', 'testing', 'pbkdf2:sha256:150000$Ay9avpAl$fd1f6e4309df525d9c784f845a0e28004c13bb4576863c7626d181231cd1391a', 'student', 'hello@example.com', '{}', 'z4ogW5Sco9IxLx1xjpCw5EmUMYeyTbcKhlPAVz4ntroTUhm4h3'),
	('DwH9FJJa5KdSFA5AiuuhXQWBSvwEDxo7ESV7GpRKe5MuNITLlx', 'stu4', 'pbkdf2:sha256:150000$swLijdmP$07d9d1922f70b21e6141e9618e9b0230052daadb2c0aacec846e95acb2a313ca', 'student', 'stu4@x.com', '{"mon": ["10:00", "20:00"], "wed": ["09:00", "17:00"], "fri": ["16:00", "22:00"]}', 'yaweYinSFiqvMWFpR1XolCglcWPOOzK7RuxEeF5dxvDFtAUB9q'),
	('jXrAWx7oDyM1FN9NGDn0QvIlniMT3HTJdJ0j45zUvsVd3qC7QQ', 'stu3', 'pbkdf2:sha256:150000$c8fAkOx9$c94ed660fcaa7a019d93ca853564ef0ad35be6c040c3472700195af30277a53f', 'student', 'stu3@x.com', '{"sun": ["10:00", "14:00"], "mon": ["12:00", "17:00"], "tue": ["11:00", "18:00"]}', 'Rxu9GVXaXjQyo3WzB6I5ODRqAqLjHHBOKXMKuPBAKT1AXWQybC'),
	('laEUTctNSOhlItnOrThLCvmBa8lAER7bna73E521Nxq75cMW7f', 'stu5', 'pbkdf2:sha256:150000$Qg2BAnrV$8d3495059913855f30725650a5626e105c93eb848c5616af9f47fbbd866ec99f', 'student', 'stu5@x.com', '{"mon": ["08:00", "16:00"], "wed": ["11:00", "17:00"], "fri": ["16:00", "22:00"]}', 't6VODJxLeUOLhnZ8AeosFoh4L8kDQ4Gbxrkj2npie5IargpoDT'),
	('Mns3yIbpH3t2dF6Ga6bO4B48TnxhS5mlYqYNCQ9QAlBIjU0pvW', 'stu1', 'pbkdf2:sha256:150000$QWm8TlsJ$114984fb97d05e6771e91342f400e2db1d2e43a19e7488cbe80370f3ac395072', 'student', 'stu1@x.com', '{"sun": ["09:00", "20:00"], "mon": ["09:00", "16:00"], "tue": ["08:00", "20:00"]}', '6d9FYn6PhdXjBU7mwPDhbbnKWiHid0pgYOEjWVAADGrP7tRxl4'),
	('MozwkrnaJUsiyWzJqfEpVndV8YYEH0Kbh2n3m0s1IHgwdAzbZI', 'stu2', 'pbkdf2:sha256:150000$ptrQ5wdM$04a98e3c2df7d45208942cc59bed3a4d90b0c66048eb8d9b2df8489ea1551ca6', 'student', 'stu2@x.com', '{"sun": ["13:00", "17:00"], "mon": ["11:00", "16:00"], "tue": ["10:00", "18:00"]}', 'YmdmZi6AutgmygmsGM0JrctwCz2dDPYSqUGjCi1Aw1pyd1v3IJ'),
	('mw9YNqZ8BlqwQMZDTaAC3OxpfTwMlYJRUtDc13OcJtOI1lB7Wa', 'stu9', 'pbkdf2:sha256:150000$2s9QMI4G$d1d763873a94559ec7cd0d2a5f3d1be2f55ddbf63a3ab97ed97e80fe0c3c75f4', 'student', 'stu9@x.com', '{"sun": ["08:00", "15:00"], "thu": ["11:00", "18:00"], "sat": ["14:00", "18:00"]}', 'y8rqy0ZOh8OmwJC4KiyOg2pMMtpJvjSqFEEt86Soam6bONGdcp'),
	('wnqwJX1D1VKbblXfix1K3BYLt8xrt5ZIRkFvM9iihPvx6TxZRM', 'stu8', 'pbkdf2:sha256:150000$6LaAqa6A$7bcf545ee1bc43c4d762df69d0f2acb0f6a923aac21721e1a1d4fb55ca289af2', 'student', 'stu8@x.com', '{"sun": ["09:00", "20:00"], "mon": ["13:00", "17:00"], "tue": ["09:00", "17:00"], "fri": ["13:00", "20:00"], "sat": ["10:00", "17:00"]}', '3sx1oV7uNvDBA41kuBB2WQZae2vsTzS1CcinCDzuet12NzghCn'),
	('YI5CNptpejWDM1Te7UDf3jvVlek1XEAuQuHNCoWJCkKxgner7J', 'test', 'pbkdf2:sha256:150000$MZTTfKan$1ec3c97e23dcdc420679a737aa1f09ae111e70f2af99ce4d997945f15b918e34', 'teacher', 'test@example.com', '{}', 'Gb5Cs4FFEDfvwFmRLInW3yJwnBkLEaj2ampKWSW1IUt6HwQy7V');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
