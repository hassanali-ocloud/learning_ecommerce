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

# write query to see the names of all the people that are friends
select p1.p_name as Friend1, p2.p_name as Friend2
from friendships f
join people p1 on f.f_friend1 = p1.p_id
join people p2 on f.f_friend2 = p2.p_id;

select p_name, t_name from people inner join things on people.p_id = things.t_owner;
select p_name, t_name from people left join things on people.p_id = things.t_owner;

# write query where we can see persons as columns who share the same thing along with that thing.
SELECT p1.p_name AS Person1,
       p2.p_name AS Person2,
       t.t_name   AS SharedThing
FROM ownership o1
JOIN ownership o2
    ON o1.o_thing = o2.o_thing
   AND o1.o_owner < o2.o_owner
JOIN people p1 ON o1.o_owner = p1.p_id
JOIN people p2 ON o2.o_owner = p2.p_id
JOIN things t  ON o1.o_thing = t.t_id;

-- select p1.p_name as Person1, p2.p_name as Person2, t_name as SharedThings
-- from ownership o1
-- join ownership o2 on o1.o_thing = o2.o_thing and o1.o_owner <> o2.o_owner
-- join people p1 on p1.p_id = o1.o_owner
-- join people p2 on p2.p_id = o2.o_owner
-- join things t on t.t_id = o1.o_thing

















