CREATE TABLE `transaction_tbl_admin` (
  `transaction_id` int NOT NULL,
  `ticket_id` varchar(45) DEFAULT NULL,
  `t_Price` double DEFAULT NULL,
  `t_quantity` int DEFAULT NULL,
  `t_type` varchar(20) DEFAULT NULL,
  `t_status` varchar(20) DEFAULT NULL,
  `t_Date` datetime DEFAULT NULL,
  PRIMARY KEY (`transaction_id`)
) 