use tutorialdb;

drop table if exists people;

CREATE TABLE IF NOT EXISTS people (
	p_id int PRIMARY KEY auto_increment,
	p_name VARCHAR(255),
    p_age integer,
    p_height float,
    p_gender enum("male", "female")
);

insert into people (p_name, p_age, p_height, p_gender) values
("Mike", 55, 188, "male"),
("Kike", 55, 188, "male"),
("Sike", 55, 188, "male"),
("Like", 55, 188, "male"),
("Tike", 55, 188, "male"),
("Pike", 55, 188, "male"),
("Qike", 55, null, "male");

insert into people (p_name, p_age, p_height, p_gender) values
("Mike", 55, 188, "male");

select * from people;
select p_name, p_age from people
where p_age > 55;

select distinct p_name,  p_age from people;

select * from people
where p_age in (55, 60);

select * from people
where p_name Like 'M%%e';

select p_name as 'name', p_age as 'age' from people;

select avg(p_age) as 'Age Sum' from people where p_name like 'K%';

update people set p_gender = 'female' where p_name = 'Mike';
select * from people;

select p_gender, p_age, count(p_height) from people
group by p_gender, p_age;

select * from people
order by p_gender desc;

select * from people
order by p_gender
limit 5;