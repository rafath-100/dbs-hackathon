CREATE TABLE `order_table` (
  `ticker_id` varchar(45) NOT NULL,
  `user_name` varchar(45) DEFAULT NULL,
  `stock_name` varchar(45) DEFAULT NULL,
  `order_quantity` int DEFAULT NULL,
  `price` double DEFAULT NULL,
  `order_date` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ticker_id`)
) 