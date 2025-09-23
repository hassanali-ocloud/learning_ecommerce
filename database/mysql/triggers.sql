use tutorialdb;
show tables;

drop table person;

create table if not exists person(
	p_id integer primary key auto_increment,
    p_name varchar(255),
    p_age integer,
    p_height float,
    p_gender enum("male", "female")
);

INSERT INTO person (p_name, p_age, p_height, p_gender) VALUES
('Alice', -5, 5.6, 'female');

select * from person;

drop table person_log;
CREATE TABLE IF NOT EXISTS person_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    person_id INT,
    action VARCHAR(50),
    old_name VARCHAR(255),
    new_name VARCHAR(255)
);

select * from person_log;

DELIMITER $$
create trigger before_person_insert
before insert on person
for each row
begin
	if new.p_age < 0 then
		set new.p_age = 0;
	end if;
end$$
DELIMITER ;;

DELIMITER $$
CREATE TRIGGER after_person_insert
AFTER INSERT ON person
FOR EACH ROW
BEGIN
    INSERT INTO person_log (person_id, action, new_name)
    VALUES (NEW.p_id, 'INSERT', NEW.p_name);
END$$
DELIMITER ;;

DELIMITER $$
CREATE TRIGGER after_person_delete
AFTER DELETE ON person
FOR EACH ROW
BEGIN
    INSERT INTO person_log (person_id, action, old_name)
    VALUES (OLD.p_id, 'DELETE', OLD.p_name);
END$$
DELIMITER ;;

delete from person where p_id = 1


