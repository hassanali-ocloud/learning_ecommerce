SHOW DATABASES;
create database if not EXISTS tutorialdb;

use tutorialdb;
SHOW TABLES;

CREATE TABLE IF NOT EXISTS people (
	p_id VARCHAR(32) PRIMARY KEY,
	p_name VARCHAR(255),
	p_age INTEGER,
	p_height FLOAT
);
select * from people
where p_height > 180 ;