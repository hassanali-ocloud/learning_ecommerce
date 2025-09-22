use tutorialdb;
# describe people;

select * from people;

set sql_safe_updates = 0;
# UPDATE people SET p_height = 30 where p_id = 'peoplepeople1';
# delete from people where p_id <> '1';

# alter table people modify column p_id integer;

# insert into people values
# (2, "Ali", 25, 110); 

# alter table people rename column p_heighted to p_height;

# alter table people add column p_weight float;

# alter table people drop column p_weight

# truncate table people

drop table if exists people
