use tutorialdb;
drop table if exists people;
show tables;
create table if not exists people(
	p_id integer primary key auto_increment,
    p_name varchar(255),
    p_age integer,
    p_height float,
    p_gender enum("male", "female")
);
INSERT INTO people (p_name, p_age, p_height, p_gender) VALUES
('Alice', 28, 5.6, 'female'),
('Bob', 34, 5.9, 'male'),
('Charlie', 22, 6.1, 'male'),
('Diana', 45, 5.5, 'female'),
('Ethan', 30, 5.8, 'male');

update people
set p_gender = case p_id
	when 1 then 'male'
    when 2 then 'male'
    when 3 then 'male'
end
where p_id in (1, 2, 3);
select * from people;