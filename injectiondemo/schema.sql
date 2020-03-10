DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS products;

CREATE TABLE users (
  id serial PRIMARY KEY,
  username text UNIQUE NOT NULL,
  password text NOT NULL,
  type text NOT NULL
);

CREATE TABLE products (
  id serial PRIMARY KEY,
  name text UNIQUE NOT NULL,
  price text NOT NULL,
  quantity text NOT NULL
);

INSERT INTO users (username, password, type)
VALUES ('alice', '2bd806c97f0e00af1a1fc3328fa763a9269723c8db8fac4f93af71db186d6e90', 'admin'),
  ('bob', '81b637d8fcd2c6da6359e6963113a1170de795e4b725b84d1e0b4cfd9ec58ce9', 'user'),
  ('carol', '4c26d9074c27d89ede59270c0ac14b71e071b15239519f75474b2f3ba63481f5', 'user'),
  ('dave', '61ea0803f8853523b777d414ace3130cd4d3f92de2cd7ff8695c337d79c2eeee', 'user');


INSERT INTO products (name, price, quantity)
VALUES ('Claw Hammer', '$12.05', '19'),
  ('Sledge Hammer', '$13.55', '6'),
  ('4d Nails x 100', '$2.49', '4'),
  ('8d Nails x 100', '$2.79', '37'),
  ('10d Nails x 100', '$3.19', '24'),
  ('12d Nails x 100', '$3.49', '13'),
  ('16d Nails x 100', '$4.09', '19'),
  ('1/2" Screws x 75', '$2.49', '4'),
  ('3/4" Screws x 75', '$2.79', '37'),
  ('1" Screws x 75', '$3.19', '24'),
  ('1 1/2" Screws x 75', '$3.49', '13'),
  ('2" Screws x 75', '$4.09', '19'),
  ('Paint Brushes x 5', '$18.99', '20'),
  ('Paint Brushes x 3', '$12.99', '13'),
  ('1/2" Chisel', '$6.99', '4'),
  ('3/4" Chisel', '$7.99', '5'),
  ('1" Chisel', '$8.99', '6'),
  ('12v Cordless Drill', '$71.50', '12');
