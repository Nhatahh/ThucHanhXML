
-- Cấu trúc bảng categories
DROP TABLE IF EXISTS `categories`;
CREATE TABLE `categories` (
  `id` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `categories` (id, name) VALUES ('c1', 'Electronics');
INSERT INTO `categories` (id, name) VALUES ('c2', 'Smartphone');
INSERT INTO `categories` (id, name) VALUES ('c3', 'Accessories');


-- Cấu trúc bảng products
DROP TABLE IF EXISTS `products`;
CREATE TABLE `products` (
  `id` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `currency` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `stock` int DEFAULT NULL,
  `categoryRef` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `categoryRef` (`categoryRef`),
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`categoryRef`) REFERENCES `categories` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `products` (id, name, price, currency, stock, categoryRef) VALUES ('p001', 'Laptop Dell Inspiron', '750.00', 'USD', '120', 'c1');
INSERT INTO `products` (id, name, price, currency, stock, categoryRef) VALUES ('p002', 'iPhone 15 Pro', '1200.00', 'USD', '50', 'c2');
INSERT INTO `products` (id, name, price, currency, stock, categoryRef) VALUES ('p003', 'Tai nghe Bluetooth Sony', '99.00', 'USD', '300', 'c3');

