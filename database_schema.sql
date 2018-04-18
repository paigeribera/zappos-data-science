DROP TABLE IF EXISTS `items_on_menu`;
DROP TABLE IF EXISTS `restaurant_menus`;
DROP TABLE IF EXISTS `menu`;
DROP TABLE IF EXISTS `restaurant`;
DROP TABLE IF EXISTS `menu_items`;

CREATE TABLE menu (
  id int NOT NULL AUTO_INCREMENT,
  name varchar(255) NOT NULL,
  description text,
  PRIMARY KEY (id)
);

CREATE TABLE restaurant (
  id int AUTO_INCREMENT NOT NULL ,
  name varchar(255) NOT NULL,
  category varchar(255),
  PRIMARY KEY (id)
);

CREATE TABLE menu_item (
  id int NOT NULL AUTO_INCREMENT,
  name varchar(255) NOT NULL,
  cost int NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE items_on_menu (
  menu_item_id int NOT NULL,
  menu_id int NOT NULL,
  PRIMARY KEY (menu_item_id, menu_id),
  FOREIGN KEY (menu_item_id) REFERENCES menu_item(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  FOREIGN KEY (menu_id) REFERENCES menu(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE restaurant_menus (
  restaurant_id int NOT NULL,
  menu_id int NOT NULL,
  PRIMARY KEY (restaurant_id, menu_id),
  FOREIGN KEY (restaurant_id) REFERENCES restaurant(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  FOREIGN KEY (menu_id) REFERENCES menu(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

INSERT INTO restaurant (name, category)
VALUES ('Carrabba''s', 'Italian');

INSERT INTO restaurant (name, category)
VALUES ('Roberto''s', 'Mexican');

INSERT INTO restaurant (name, category)
VALUES ('Denny''s', 'American');

INSERT INTO restaurant (name, category)
VALUES ('Raising Canes', 'Fastfood');

INSERT INTO menu (name, description)
VAlUES ('Denny''s Breakfast menu', 'Don''t forget breakfast. And second breakfast!');

INSERT INTO menu (name, description)
VALUES ('Carrabba''s Dinner menu', 'Make sure to eat as much as you can so it''s uncomfortable when you try to sleep.');

INSERT INTO menu (name, description)
VALUES ('Raising Canes 24/7 menu', 'Chicken fingers! Chicken sandwich! Chicken!!!');

INSERT INTO menu (name, description)
VALUES ('Roberto''s 24/7 menu', 'Lots of mexican food. Including cow tongue.');

INSERT INTO menu_item (name, cost)
VALUES ('Burrito', 6.50);

INSERT INTO menu_item (name, cost)
VALUES ('Pasta primavera', 14.75);

INSERT INTO menu_item (name, cost)
VALUES ('Chicken fingers meal', 8.00);

INSERT INTO menu_item (name, cost)
VALUES ('Texas toast', 1.50);

INSERT INTO menu_item (name, cost)
VALUES ('Enchilada', 7.00);

INSERT INTO menu_item (name, cost)
VALUES ('Waffles', 8.75);

INSERT INTO menu_item (name, cost)
VALUES ('Pancakes', 6.00);

INSERT INTO menu_item (name, cost)
VALUES ('Coke Zero', 2.00);

INSERT INTO items_on_menu (menu_item_id, menu_id)
VALUES (1, 3);

INSERT INTO items_on_menu (menu_item_id, menu_id)
VALUES (8, 3);

INSERT INTO items_on_menu (menu_item_id, menu_id)
VALUES (5, 3);

INSERT INTO items_on_menu (menu_item_id, menu_id)
VALUES (3, 4);

INSERT INTO items_on_menu (menu_item_id, menu_id)
VALUES (8, 4);

INSERT INTO items_on_menu (menu_item_id, menu_id)
VALUES (4, 4);

INSERT INTO items_on_menu (menu_item_id, menu_id)
VALUES (3, 2);

INSERT INTO items_on_menu (menu_item_id, menu_id)
VALUES (8, 2);

INSERT INTO items_on_menu (menu_item_id, menu_id)
VALUES (6, 1);

INSERT INTO items_on_menu (menu_item_id, menu_id)
VALUES (7, 1);

INSERT INTO items_on_menu (menu_item_id, menu_id)
VALUES (8, 1);
