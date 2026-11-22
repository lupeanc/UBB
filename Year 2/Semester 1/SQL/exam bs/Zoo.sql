use Zoo

create table zoo (
	id int primary key identity,
	adminis varchar(10),
)

insert into zoo values ('name')
insert into zoo values ('name2')
insert into zoo values ('name3')
select * from zoo

--create table zooanimals (
--	id int primary key identity,
--	zid int foreign key references zoo(id),
--	aid int references animal(id)
--)

create table animal (
	id int primary key identity,
	zid int references zoo(id),
	name varchar(10),
	d date
)

insert into animal values (1,'a1','2020-1-1')
insert into animal values (3,'a2','2020-1-1')
insert into animal values (3,'a3','2020-1-1')

create table food (
	id int primary key identity,
	name varchar(10)
)

insert into food values ('f1')

create table animalfood(
	aid int references animal(id),
	fid int references food(id),
	quota int,
	primary key (aid,fid)
)

insert into animalfood values (1,1,100)

create table visitor(
	id int primary key identity,
	name varchar(10),
	age int
)

insert into visitor values ('v1', 10)
insert into visitor values ('v2', 10)

create table visits(
	id int primary key identity,
	vid int references visitor(id),
	zid int references zoo(id),
	day int,
	price int
)

insert into visits values (1,1,7,100)
insert into visits values (1,2,7,100)
insert into visits values (1,2,7,100)
insert into visits values (2,3,7,100)
select * from visits

-- 2
go
create or alter procedure deleteanimal(@aid int)
as
begin
	if not exists (select * from animal where @aid = id)
	begin
		raiserror('nf',16,1)
		return -1
	end

	if exists (select * from animalfood where @aid=aid)
	begin
		delete from animalfood
		where aid=@aid
	end

end

go
exec deleteanimal 1
select * from animalfood

-- 3
go
create or alter view showzoos as
	select z.id
	from zoo z inner join visits v on z.id=v.zid
	group by z.id
	having count(v.id) <= all (select count(id) from visits group by zid)

go
select * from showzoos

-- 4
go
create or alter function showvisitor(@n int)
returns table
as
return
	select v.id
	from visitor v inner join visits vi on v.id=vi.vid inner join animal a on a.zid=vi.zid
	where vi.zid in (select zoo.id
					from zoo inner join animal on zoo.id=animal.zid
					group by zoo.id
					having count(animal.id)>@n)

go
select * from showvisitor(1)