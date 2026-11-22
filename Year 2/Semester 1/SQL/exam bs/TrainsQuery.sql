use Trains
go

drop table routestations
drop table route
drop table train
drop table traintype
drop table station


create table traintype (
	id int primary key identity,
	name varchar(10),
	descr varchar(10)
)

create table train(
	id int primary key identity,
	tid int references traintype(id),
	name varchar(10)
)

create table station(
	id int primary key identity,
	name varchar(10)
)

create table route(
	id int primary key identity,
	tid int references train(id),
	name varchar(10)
)

create table routestations(
	rid int references route(id),
	sid int references station(id),
	a time,
	d time,
	primary key(rid,sid)
)

-- inserts

insert into traintype values
	('a', null),
	('b', null);

insert into train values
	(1,'t1'),
	(1,'t2'),
	(2,'t3');

insert into station values
	('s1'),
	('s2'),
	('s3');

insert into route values
	(1,'r1'),
	(2,'r2'),
	(1, 'r3');

insert into routestations values
	(1,2,'1:00','2:00'),
	(2,3,'1:00','2:00'),
	(3,1,'1:00','2:00');

	select * from routestations


	-- 2
	go
	create or alter procedure addupdateroute(@rname varchar(10), @sname varchar(10), @a time, @d time)
	as
		begin
		declare @rid int = (select id from route where @rname = name)
		declare @sid int = (select id from station where @sname = name)

		if not exists (select * from route where @rid = id)
		begin
			raiserror('caca', 16,1)
			return -1
		end
		if not exists (select * from station where @sid = id)
		begin
			raiserror('caca', 16,1)
			return -1
		end

		if exists (select * from routestations where @rid = rid and @sid =sid)
		begin
			update routestations
			set a=@a, d=@d
			where @rid = rid and @sid = sid
		end

		if not exists (select * from routestations where @rid = rid and @sid =sid)
		begin
			insert into routestations values (@rid, @sid, @a, @d)
		end


	end

go
select * from routestations
select * from route
select * from station

exec addupdateroute 'r1', 's2', '20:00', '21:00'
select * from routestations

exec addupdateroute 'r3', 's2', '20:00', '21:00'
select * from routestations

exec addupdateroute 'r1000', 's2', '20:00', '21:00'


-- 3
go
create or alter view showroutes as
	select r.name as name
	from route r inner join routestations rs on r.id =rs.rid
	group by r.name
	having count(rs.sid) = (select count(id) from station)

go
select * from showroutes

-- 4
go
create or alter function showstations(@r int)
returns table
as
return
	select s.name
	from station s inner join routestations rs on s.id=rs.sid
	group by s.name
	having count(rs.rid) > @r

go
select * from showstations(1)

	



