use tutorialdb;

drop table people;

CREATE TABLE IF NOT EXISTS people (
	p_id int(32) PRIMARY KEY auto_increment,
	p_firstname VARCHAR(255),
    p_lastname varchar(255),
    constraint name_constraint unique (p_firstname, p_lastname)
);
insert into people (p_firstname, p_lastname) values ("Mike", "Smith"), ("Jonn", "Smote");
select * from people;
alter table people modify column p_id int(32) auto_increment;
insert into people (p_id, p_name, p_age, p_ssn) values (3, 'Jimmy', 25, "HA2344");
insert into people (p_name) values ("Kalli");

truncate table people;
alter table people add constraint unique_lastname unique(p_lastname)