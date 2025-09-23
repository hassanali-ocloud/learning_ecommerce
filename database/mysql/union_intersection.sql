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

drop table if exists things;
create table if not exists things(
	t_id integer primary key auto_increment,
    t_name varchar(255) not null,
    t_description varchar(255),
    t_owner integer,
    foreign key (t_owner) references people (p_id)
);
INSERT INTO things (t_name, t_description, t_owner) VALUES
('Laptop', 'Dell XPS 15', 1),   -- owned by Alice
('Bicycle', 'Mountain bike', 2),-- owned by Bob
('Guitar', 'Acoustic guitar', 3),
('Camera', 'DSLR Canon', 1),
('Car', 'Tesla Model 3', 5),
('Car', 'Tesla Model 3', 5);

create table if not exists ownership(
	o_owner integer,
    o_thing integer,
    primary key(o_owner, o_thing),
    foreign key (o_owner) references people (p_id),
    foreign key (o_thing) references things (t_id)
);
INSERT INTO ownership (o_owner, o_thing) VALUES
(1, 1),  -- Alice owns Laptop
(2, 2),  -- Bob owns Bicycle
(3, 3),  -- Charlie owns Guitar
(1, 4),  -- Alice owns Camera
(5, 5),  -- Ethan owns Car
(2, 5),  -- Bob also co-owns Car
(4, 3);  -- Diana also co-owns Guitar

create table if not exists friendships(
	f_friend1 int,
    f_friend2 int,
    primary key (f_friend1, f_friend2),
    foreign key (f_friend1) references people (p_id),
    foreign key (f_friend2) references people (p_id)
);
INSERT INTO friendships (f_friend1, f_friend2) VALUES
(1, 2), -- Alice ↔ Bob
(1, 3), -- Alice ↔ Charlie
(2, 4), -- Bob ↔ Diana
(3, 5), -- Charlie ↔ Ethan
(4, 5); -- Diana ↔ Ethan

select * from people;
select * from things;
select * from ownership;
select * from friendships;

select p_name from people
union
select t_name from things;

select p_name from people
union all
select t_name from things;

select p_name from people
except
select p_name from people where p_name <> "Diana";
