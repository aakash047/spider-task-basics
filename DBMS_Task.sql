create database inventoryDB;
use inventoryDB;
CREATE TABLE products (
  name varchar(100) NOT NULL PRIMARY KEY, 
  description varchar(255),
  price decimal(10,2),
  quantity int NOT NULL,
  category varchar(255)
);
INSERT INTO products (name, description, price, quantity, category)
VALUES ('Laptop', 'A powerful laptop for work and play', 799.99, 10, 'Electronics'),
       ('Headphones', 'Noise-cancelling headphones for immersive sound', 149.99, 25, 'Electronics'),
       ('T-Shirt', 'Comfortable and stylish T-shirt', 19.99, 50, 'Clothing');
SELECT * FROM products;
SELECT * FROM products WHERE price < 100;
SELECT * FROM products WHERE quantity > 20;
UPDATE products SET price = 899.99 WHERE name = 'Laptop';
DELETE FROM products WHERE name = 'Headphones';
