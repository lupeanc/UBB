use Plants
go

create table category (
	id int primary key identity,
	name varchar(10),
	descr varchar(100)
)

create table location (
	id int primary key identity,
	name varchar(10),
	descr varchar(100)
)

create table plant (
	id int primary key identity,
	lid int references location(id),
	name varchar(10),
	descr varchar(100),
	aqdate date,
	wdate date,
)

create table image (
	id int primary key identity,
	pid int references plant(id),
	path varchar(10),
	caption varchar(100),
	upload date
)

create table palntcategory (
	pid int references plant(id),
	cid int references category(id),
	primary key(pid,cid)
)

create table carehistory(
	id int primary key identity,
	pid int references plant(id),
	d date,
	t time,
	notes varchar(100)
)

-- 2

insert into location values ('l1', null);

go
create or alter procedure addupdateplant(@lid int, @name varchar(10), @descr varchar(100), @aqdate date, @wdate date)
as
	begin
		if exists (select * from location where @lid = id)
		begin
			if exists (select * from plant where @name = name)
			begin
				update plant
				set aqdate=@aqdate
				where name=@name
			end

			if not exists (select * from plant where @name = name)
			begin
				insert into plant(lid, name, descr, aqdate,wdate) values (@lid, @name, @descr, @aqdate, @wdate);
			end
		end

		if not exists (select * from location where @lid = id)
		begin
			raiserror('not found', 16,1)
			return -1
		end

	end

go
exec addupdateplant 1, 'p1', null, '2020-1-1', '2020-1-1'
select * from plant

exec addupdateplant 1, 'p1', null, '2021-1-1', '2020-1-1'
select * from plant

exec addupdateplant 2, 'p1', null, '2021-1-1', '2020-1-1'
select * from plant

-- 3

insert into location values ('l2', null)
insert into plant values
(1,'p2', null, '2026-1-1', '2020-1-1'),
(2,'p2', null, '2020-1-1', '2020-1-1');

select * from plant

go
create or alter view showplants as
	select p.lid location, count(p.id) counts, max(p.aqdate) aqdate
	from plant p
	group by p.lid

go
select * from showplants

-- 4
insert into image values
(4,null,null,null),
(3,null,null,null),
(3,null,null,null),
(4,null,null,null);

select * from image

go
create or alter function showplantimg(@x int)
returns table
as
return
	
	select a.id
	from
		(select p.id, p.wdate
		from plant p inner join image i on p.id = i.pid
		group by p.id, p.wdate
		having count(i.pid) > @x) a
	where a.wdate = (select max(b.wdate)
					from (select p.id, p.wdate
		from plant p inner join image i on p.id = i.pid
		group by p.id, p.wdate
		having count(i.pid) > @x) b)
	
	

go
select * from showplantimg(1)
