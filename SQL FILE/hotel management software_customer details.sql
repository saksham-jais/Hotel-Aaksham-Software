-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: hotel management software
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer details`
--

DROP TABLE IF EXISTS `customer details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer details` (
  `S No.` char(5) NOT NULL,
  `Guest ID` char(5) NOT NULL,
  `Guest Name` varchar(20) NOT NULL,
  `Gender` varchar(11) NOT NULL,
  `Religion` varchar(7) NOT NULL,
  `Address` varchar(25) NOT NULL,
  `City` varchar(20) NOT NULL,
  `Country` varchar(20) NOT NULL,
  `Contact No.` varchar(13) NOT NULL,
  `ID Type` varchar(20) NOT NULL,
  `ID Number` varchar(15) NOT NULL,
  `Status` varchar(10) NOT NULL,
  `Email ID` varchar(50) NOT NULL,
  `Image` varchar(83) DEFAULT NULL,
  PRIMARY KEY (`Guest ID`),
  UNIQUE KEY `S No.` (`S No.`),
  UNIQUE KEY `ID Number` (`ID Number`),
  UNIQUE KEY `Email ID` (`Email ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer details`
--

LOCK TABLES `customer details` WRITE;
/*!40000 ALTER TABLE `customer details` DISABLE KEYS */;
/*!40000 ALTER TABLE `customer details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-19  5:05:07
