DROP TABLE test1
CREATE TABLE test1 (
	id int primary key identity,
	--id2 int references test2(id),
	--id2 int,
	--constraint FK_id2 foreign key(id2) references test2(id),
	name1 varchar(50),
	year1 int,
	--FOREIGN KEY(name1,year1) references test2(name2,year2)


)


DROP TABLE test2
CREATE TABLE test2 (
	id int primary key identity,
	name2 varchar(50),
	year2 int
)

DROP TABLE test3
CREATE TABLE test3 (
	id int,
	name2 varchar(50),
	year2 int,
	constraint pk primary key(name2,year2)
)


ALTER TABLE test1
ADD CONSTRAINT checkYear check (year1 > 2000)


ALTER TABLE test1
DROP CONSTRAINT checkYear

-- --------------------------

INSERT INTO test1(name1, year1) VALUES
	('waw', 2003),
	('minune', 2003),
	('a muie', 2003),
	--('caca', 1990),
	('nu mere', 2009);

select year1
from test1
where name1 like '_%'
--group by year1
--having count (*) > 2

create table R(
rid int primary key,
a1 varchar(10),
k2 int unique,
a2 int,
a3 int,
a4 int,
a5 varchar(10),
a6 int
)



insert into R values
(2, 'a', 100,1,3,3,'M1',22),
(3, 'b', 200,1,3,3,'M1',22),
(4, 'c', 150,2,3,4,'M1',23),
(5, 'd', 700,2,4,4,'M2', 29),
(6, 'e', 300,3,4,5,'M2', 29),
(7, 'f', 350,3,4,5,'M5', 23),
(8, 'g', 400,3,5,7,'M5', 29),
(9, 'h', 500,4,5,7,'M2',30),
(10,'j', 450,4,5,7,'M7',30),
(11,'k',250,4,6,7,'M7',30),
(12,'l',800,5,6,7,'M6',22),
(13,'m',750,5,6,7,'M6',23);

SELECT r1.rid,r2.rid,r3.rid
FROM R r1 INNER JOIN R r2 ON r1.A2 = r2.A3
INNER JOIN R r3 ON r2.A3 = r3.A4
ORDER BY r1.rid


SELECT r1.RID, r1.K2, COUNT(*) NumRows
FROM R r1 INNER JOIN R r2 ON r1.A2 = r2.A3
INNER JOIN R r3 ON r2.A3 = r3.A4
WHERE r1.A1 LIKE '_%'
GROUP BY r1.RID, r1.K2
HAVING COUNT(*) >= 6


SELECT r1.A6, MAX(r1.A2) MaxA2
FROM R r1
WHERE r1.A5 IN ('M1', 'M2')
GROUP BY r1.A6
EXCEPT
SELECT DISTINCT r2.A6, r2.A2
FROM R r2


create table traintypes(
	id int primary key identity,	
	name varchar(10),
	descr varchar(100)
)

CREATE TABLE trains (
	id int primary key identity,
	name varchar(10),
	typeid int references traintypes(id)
)

create table stations(
	id int primary key identity,
	name varchar(10) unique
)
create table routes(
	id int primary key identity,
	name varchar(10) unique,
	trainid int references trains(id),

)

create table droneManufacturers(
	id int primary key identity,

)
create table droneModels ()
create table drones ()
create table pizzaShops()
create table customers ()
create table deliveries ()
