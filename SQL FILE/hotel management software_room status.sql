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
-- Table structure for table `room status`
--

DROP TABLE IF EXISTS `room status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `room status` (
  `Room No.` varchar(15) NOT NULL,
  `Room Type` varchar(25) NOT NULL,
  `Status` varchar(10) NOT NULL,
  `Price` int NOT NULL,
  PRIMARY KEY (`Room No.`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room status`
--

LOCK TABLES `room status` WRITE;
/*!40000 ALTER TABLE `room status` DISABLE KEYS */;
INSERT INTO `room status` VALUES ('R100','Double Bed','Dirty',4000),('R101','Single Bed','Repair',2000),('R102','Super Dulex','Dirty',16000),('R103','Luxury','Dirty',10000),('R104','Super Dulex','Dirty',8000),('R105','Double Bed','Dirty',4000),('R106','Super Dulex','Dirty',8000),('R107','Luxury','Dirty',20000),('R108','Dulex','Vacant',6000),('R109','Luxury','Dirty',10000),('R110','Super Dulex','Dirty',8000),('R111','Dulex','Dirty',6000),('R112','Dulex','Repair',6000),('R113','Dulex','Dirty',6000),('R114','Super Dulex','Dirty',8000),('R115','Luxury','Repair',10000),('R116','Dulex','Repair',6000),('R117','Double Bed','Dirty',8000),('R118','Super Dulex','Repair',8000),('R119','Super Dulex','Dirty',8000),('R120','Super Dulex','Vacant',8000),('R121','Super Dulex','Dirty',8000),('R122','Single Bed','Vacant',2000),('R123','Luxury','Dirty',10000),('R124','Double Bed','Dirty',4000),('R125','Double Bed','Repair',4000),('R126','Luxury','Repair',10000),('R127','Dulex','Repair',6000),('R128','Luxury','Vacant',10000),('R129','Double Bed','Dirty',4000),('R130','Double Bed','Vacant',4000),('R131','Super Dulex','Vacant',8000),('R132','Super Dulex','Repair',8000),('R133','Dulex','Dirty',6000),('R134','Luxury','Dirty',10000),('R135','Dulex','Dirty',6000),('R136','Luxury','Vacant',20000),('R137','Luxury','Repair',10000),('R138','Double Bed','Repair',4000),('R139','Luxury','Vacant',10000),('R140','Single Bed','Dirty',2000),('R141','Super Dulex','Repair',8000),('R142','Super Dulex','Dirty',8000),('R143','Super Dulex','Repair',8000),('R144','Luxury','Repair',10000),('R145','Luxury','Vacant',10000),('R146','Luxury','Vacant',10000),('R147','Dulex','Dirty',6000),('R148','Single Bed','Vacant',2000),('R149','Single Bed','Repair',2000),('R150','Single Bed','Vacant',2000);
/*!40000 ALTER TABLE `room status` ENABLE KEYS */;
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
