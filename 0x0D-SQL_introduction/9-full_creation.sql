-- Create second table and insert values
-- create table with id (int)
-- , name (varchar)
CREATE TABLE IF NOT EXISTS second_table (
id INT,
name VARCHAR(255),
score INT
);
INSERT INTO second_table
       values (1, 'John', 10),
       	      (2, 'Alex', 3),
	      (3, 'Bob', 14),
	      (4, 'George', 8);
