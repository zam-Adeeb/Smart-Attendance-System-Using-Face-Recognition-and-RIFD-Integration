-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: face_atd
-- ------------------------------------------------------
-- Server version	8.0.37

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
-- Table structure for table `fc_data`
--

DROP TABLE IF EXISTS `fc_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fc_data` (
  `Id` varchar(45) NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `usn` varchar(45) NOT NULL,
  `Dept` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Id`,`usn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fc_data`
--

LOCK TABLES `fc_data` WRITE;
/*!40000 ALTER TABLE `fc_data` DISABLE KEYS */;
INSERT INTO `fc_data` VALUES ('1','Adeeb','1DB21IS001','CSE'),('2','Abi','1DB21CS002','CSE'),('3','Balaji','1DB21CS021','CSE');
/*!40000 ALTER TABLE `fc_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `register`
--

DROP TABLE IF EXISTS `register`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `register` (
  `Username` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Password` varchar(45) NOT NULL,
  PRIMARY KEY (`Username`,`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register`
--

LOCK TABLES `register` WRITE;
/*!40000 ALTER TABLE `register` DISABLE KEYS */;
INSERT INTO `register` VALUES ('Abhi','abhi@gmial.com','1111'),('Adeeb','zamadeeb@gmail.com','2222'),('balaji','princbalaji@gmail.com','3333'),('dhanukumar','dhanukumar@gmail.com','4444');
/*!40000 ALTER TABLE `register` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `sid` varchar(45) NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `usn` varchar(45) NOT NULL,
  `Dept` varchar(45) DEFAULT NULL,
  `Course` varchar(45) DEFAULT NULL,
  `year` varchar(45) DEFAULT NULL,
  `batch` varchar(45) DEFAULT NULL,
  `section` varchar(45) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `DOB` varchar(45) DEFAULT NULL,
  `Phone` varchar(45) DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  `Photo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`sid`,`usn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('1','Abhishek H','1DB21CS001','CSE','B.E','4th','2021-Batch','A','Male','21/05/2003','6366274544','Bengaluru','Yes'),('10','DhanuKumar TN','1DB21CS016','CSE','B.E','4th','2021-Batch','A','Male','17/09/2003','9976843289','Bengaluru','Yes'),('11','G Manu','1DB21CS019','CSE','B.E','4th','2021-Batch','A','Male','20/08/2003','8653529797','Bengaluru','Yes'),('12','Dhruthi DM','1DB21CS018','CSE','B.E','4th','2021-Batch','A','Female','20/12/2003','3647899997','Bengaluru','Yes'),('13','Adeeb Ahemd','1DB21CS002','CSE','B.E','4th','2021-Batch','A','Male','17/11/2003','8618225118','Bengaluru','Yes'),('14','Afza Sharff','1DB21CS003','CSE','B.E','4th','2021-Batch','A','Female','18/10/2003','7397979282','Bengaluru','Yes'),('15','Akash DS','1DB21CS004','CSE','B.E','4th','2021-Batch','A','Male','20/08/2003','8653529797','Bengaluru','Yes'),('16','Amish P','1DB21CS005','CSE','B.E','4th','2021-Batch','A','Male','16/02/2003','8768661963','Bengaluru','Yes'),('17','Aniza','1DB21CS006','CSE','B.E','4th','2021-Batch','A','Female','20/12/2003','3647899997','Bengaluru','Yes'),('18','Anu Ramanju','1DB21CS007','CSE','B.E','4th','2021-Batch','A','Female','10/12/2002','8274663721','Bengaluru','Yes'),('2','Anush A','1DB21CS008','CSE','B.E','4th','2021-Batch','A','Male','25/06/2003','9799745687','Bengaluru','Yes'),('3','Ashritha S','1DB21CS009','CSE','B.E','4th','2021-Batch','A','Female','22/04/2003','9799745687','Bengaluru','Yes'),('4','Ashwin R','1DB21CS010','CSE','B.E','4th','2021-Batch','A','Male','17/09/2003','9976843289','Bengaluru','Yes'),('5','Ayush','1DB21CS011','CSE','B.E','4th','2021-Batch','A','Male','15/05/2003','5446586709','Bengaluru','Yes'),('6','Balaji M','1DB21CS012','CSE','B.E','4th','2021-Batch','A','Male','15/05/2003','9979536377','Bengaluru','Yes'),('7','BN Kushal','1DB21CS013','CSE','B.E','4th','2021-Batch','A','Male','15/05/2003','6217191727','Bengaluru','Yes'),('8','Choman','1DB21CS014','CSE','B.E','4th','2021-Batch','A','Male','13/06/2003','6217191727','Bengaluru','Yes'),('9','Darshan','1DB21CS015','CSE','B.E','4th','2021-Batch','A','Male','25/06/2003','9799745687','Bengaluru','Yes');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-23 10:31:35
