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
INSERT INTO `student` VALUES ('1','Abhishek H','1DB21CS001','CSE','B.E','4th','2021-Batch','A','Male','21/05/2003','6366274544','Bengaluru','Yes'),('10','Ashwin R','1DB21CS010','CSE','B.E','4th','2021-Batch','A','Male','15/08/2003','9383782964','Bengaluru','Yes'),('11','Ayush P Nair','1DB21CS011','CSE','B.E','4th','2021-Batch','A','Male','21/05/2003','8945843787','Bengaluru','Yes'),('12','Balaji M','1DB21CS012','CSE','B.E','4th','2021-Batch','A','Male','14/10/2003','9967566798','Bengaluru','Yes'),('13','BN Kushal','1DB21CS013','CSE','B.E','4th','2021-Batch','A','Male','04/06/2003','8653529797','Bengaluru','Yes'),('14','Choman','1DB21CS014','CSE','B.E','4th','2021-Batch','A','Male','17/11/2003','9485475118','Bengaluru','Yes'),('15','Darshan','1DB21CS015','CSE','B.E','4th','2021-Batch','A','Male','05/12/2003','9484657578','Bengaluru','Yes'),('16','DhanuKumar TN','1DB21CS016','CSE','B.E','4th','2021-Batch','A','Male','14/10/2003','9967566798','Bengaluru','Yes'),('17','Dhanyashree M','1DB21CS017','CSE','B.E','4th','2021-Batch','A','Female','10/12/2003','7383787349','Bengaluru','Yes'),('18','Dhruthi DM','1DB21CS018','CSE','B.E','4th','2021-Batch','A','Female','20/08/2003','9797928276','Bengaluru','Yes'),('19','G Manu','1DB21CS019','CSE','B.E','4th','2021-Batch','A','Male','04/06/2003','8653529797','Bengaluru','Yes'),('2','Adeeb Ahemd','1DB21CS002','CSE','B.E','4th','2021-Batch','A','Male','17/11/2003','8618225118','Bengaluru','Yes'),('20','Gayathri J','1DB21CS020','CSE','B.E','4th','2021-Batch','A','Female','10/12/2003','7383787349','Bengaluru','Yes'),('21','Goutham SK','1DB21CS021','CSE','B.E','4th','2021-Batch','A','Male','12/08/2003','8345677858','Bengaluru','Yes'),('22','Gunasagr G Megharaj','1DB21CS022','CSE','B.E','4th','2021-Batch','A','Male','15/08/2003','9383782964','Bengaluru','Yes'),('23','Harshitha J','1DB21CS023','CSE','B.E','4th','2021-Batch','A','Female','20/08/2003','7397979282','Bengaluru','Yes'),('24','Himanshu Kumar','1DB21CS024','CSE','B.E','4th','2021-Batch','A','Male','21/05/2003','6836873973','Bengaluru','Yes'),('25','Jaishritha','1DB21CS025','CSE','B.E','4th','2021-Batch','A','Female','20/08/2003','7383787349','Bengaluru','Yes'),('26','Jeevaraj Shetty S','1DB21CS026','CSE','B.E','4th','2021-Batch','A','Male','17/11/2003','9876542378','Bengaluru','Yes'),('27','Jishnu K','1DB21CS027','CSE','B.E','4th','2021-Batch','A','Male','04/06/2003','8653529797','Bengaluru','Yes'),('28','Nirmita','1DB21CS028','CSE','B.E','4th','2021-Batch','A','Female','20/08/2003','9834609237','Bengaluru','Yes'),('29','Noore Saba','1DB21CS029','CSE','B.E','4th','2021-Batch','A','Female','06/07/2002','7829393598','Bengaluru','Yes'),('3','Afza Sharff','1DB21CS003','CSE','B.E','4th','2021-Batch','A','Female','20/08/2003','7397979282','Bengaluru','Yes'),('30','P Abhishek','1DB21CS030','CSE','B.E','4th','2021-Batch','A','Male','21/05/2003','8923892198','Bengaluru','Yes'),('31','Pandey A','1DB21CS031','CSE','B.E','4th','2021-Batch','A','Male','21/05/2003','8368739736','Bengaluru','Yes'),('4','Akash DS','1DB21CS004','CSE','B.E','4th','2021-Batch','A','Male','04/06/2003','8653529797','Bengaluru','Yes'),('5','Amish P','1DB21CS005','CSE','B.E','4th','2021-Batch','A','Male','21/05/2003','6836873973','Bengaluru','Yes'),('6','Aniza','1DB21CS006','CSE','B.E','4th','2021-Batch','A','Female','20/08/2003','7383787349','Bengaluru','Yes'),('7','Anu Ramanji','1DB21CS007','CSE','B.E','4th','2021-Batch','A','Female','10/12/2003','7383787349','Bengaluru','Yes'),('8','Anush A','1DB21CS008','CSE','B.E','4th','2021-Batch','A','Male','12/08/2003','8618225118','Bengaluru','Yes'),('9','Ashritha S','1DB21CS009','CSE','B.E','4th','2021-Batch','A','Female','20/08/2003','9834609237','Bengaluru','Yes');
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

-- Dump completed on 2024-12-23 12:36:58
