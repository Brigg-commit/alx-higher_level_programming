-- Creates the database hbtn_0d_usa
-- If database  already exists, script should not fail
CREATE TABLE IF NOT EXISTS hbtn_0d_usa

-- Creates table cities in the database hbtn_0d_usa
-- id INT unique, auto generated, can’t be null and is a primary key
-- state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
-- name VARCHAR(256) can’t be null
-- if table exists, script should not fail.
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT UNIQUE AUTO_INCREMENT NOT NULL,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(state_id) REFERENCES states(id));
