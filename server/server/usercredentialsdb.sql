-- MySQL dump 10.17  Distrib 10.3.14-MariaDB, for CYGWIN (x86_64)
--
-- Host: usercredentialsdb.c3fbnwkqmhbb.us-east-1.rds.amazonaws.com    Database: usercredentialsdb
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `logincredentialstbl`
--

DROP TABLE IF EXISTS `logincredentialstbl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `logincredentialstbl` (
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logincredentialstbl`
--

LOCK TABLES `logincredentialstbl` WRITE;
/*!40000 ALTER TABLE `logincredentialstbl` DISABLE KEYS */;
INSERT INTO `logincredentialstbl` VALUES ('username','password'),('ausername','apassword'),('testusername','testpassword'),('ausername1','apassword1');
/*!40000 ALTER TABLE `logincredentialstbl` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uploadstbl`
--

DROP TABLE IF EXISTS `uploadstbl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `uploadstbl` (
  `uploadId` int NOT NULL AUTO_INCREMENT,
  `data` blob,
  `uploadname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`uploadId`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uploadstbl`
--

LOCK TABLES `uploadstbl` WRITE;
/*!40000 ALTER TABLE `uploadstbl` DISABLE KEYS */;
/*!40000 ALTER TABLE `uploadstbl` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userinfotbl`
--

DROP TABLE IF EXISTS `userinfotbl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userinfotbl` (
  `firstname` varchar(255) DEFAULT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinfotbl`
--

LOCK TABLES `userinfotbl` WRITE;
/*!40000 ALTER TABLE `userinfotbl` DISABLE KEYS */;
/*!40000 ALTER TABLE `userinfotbl` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usernamexuploadidtbl`
--

DROP TABLE IF EXISTS `usernamexuploadidtbl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usernamexuploadidtbl` (
  `username` varchar(255) DEFAULT NULL,
  `uploadid` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usernamexuploadidtbl`
--

LOCK TABLES `usernamexuploadidtbl` WRITE;
/*!40000 ALTER TABLE `usernamexuploadidtbl` DISABLE KEYS */;
/*!40000 ALTER TABLE `usernamexuploadidtbl` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-02  2:11:54
