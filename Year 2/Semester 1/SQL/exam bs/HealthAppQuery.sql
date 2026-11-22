use HealthApp

go
create table users(
	id int primary key identity,
	name varchar(10),
	age int,
	gender varchar(1)
)

create table activities(
	id int primary key identity,
	name varchar(10),
	calories int
)

create table meals(
	id int primary key identity,
	name varchar(10),
	calories int
)

create table healthmetrics(
	id int primary key identity,
	userid int references users(id),
	d date,
	weight int,
	bp int,
	hr int
)

create table usersctivities(
	id int primary key identity,
	userid int references users(id),
	aid int references activities(id),
	d date,
	t int
)

insert users values
	('u1', 21, 'F'),
	('u2', 22, 'M'),
	('u3', 24, 'M');

insert into activities values
	('a1', 100),
	('a2', 200);

insert into meals values
	('a1', 100),
	('a2', 200);

insert into healthmetrics values 
	(1,'2024-1-12',2,3,4),
	(1,'2024-2-12',2,3,4),
	(2,'2025-1-12',2,3,4);

insert into usersctivities values
	(1,2,'2024-1-3', 4),
	(1,2,'2025-1-12',3),
	(1,2,'2024-1-12',2),
	(1,1,'2024-1-12',2),
	(2,2,'2024-1-12',2);

	-- 2
	go
	create or alter procedure addupdatemetric(@userid int,@d date,
	@weight int,
	@bp int,
	@hr int)
	as
		begin
			declare @datetoday date = (select cast(GETDATE() as date))
			if @d > @datetoday
			begin
				raiserror('date not allowed', 16,1)
				return -1
			end

			insert into healthmetrics values (@userid, @d, @weight, @bp, @hr)

		end

	go
	exec addupdatemetric 1,'2028-12-2',1,2,3

	exec addupdatemetric 3,'2024-1-1',1,2,3
	select * from healthmetrics


	-- 3
	go
	create or alter view avgWmaxBP
	as
		select userid, avg(weight) average, max(bp) m
		from healthmetrics
		where d like '2024%'
		group by userid
	go

	select * from avgWmaxBP
	select * from healthmetrics

	-- 4
	go
	create or alter function avgactivity(@a int, @u int)
	returns table
	as
	return
		select userid, avg(t) average, count (*) nb
		from usersctivities ua
		where @a = ua.aid and @u = ua.userid
		group by userid

go

select * from avgactivity(2, 1)
select * from usersctivities
