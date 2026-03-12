Create Database shopDB;
drop database shopDB;

use shopdb;
create table student(
   Hakbun int primary key,
   name varchar(20),
   dt datetime 
);

desc student;
drop table student; 
select * from student;
insert into student values(1, '이상원', '2026-03-10');
insert into student(hakbun, name, dt) values(2, '홍길동', '2026-03-10');
update student set name='박길동' where hakbun = 1;
delete from student where hakbun = 2;