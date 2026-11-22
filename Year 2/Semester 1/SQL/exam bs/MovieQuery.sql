use Movie

create table company(
	id int primary key identity,
	name varchar(10)
)

create table director(
	id int primary key identity,
	name varchar(10),
	awards int
)

create table movie(
	id int primary key identity,
	cid int references company(id),
	did int references director(id),
	name varchar(10),
	rd date,
)

create table production(
	id int primary key identity,
	mid int references movie(id),
	title varchar(10)
)

create table actor(
	id int primary key identity,
	name varchar(10),
	ranking int
)

--drop table productionactors
create table productionactors(
	id int primary key identity,
	pid int references production(id),
	aid int references actor(id),
	entrymom int,

)

-- 2
go
select * from company
insert into company values ('company2')
insert into director values ('d2', 10)
insert into movie(cid, did, name, rd) values (2,2,'movie1', '2020-1-1')
select * from movie
insert into production(mid, title) values (4,'prod1'),(4,'prod2')
select * from production
insert into actor values ('a1', 1), ('a2',2)
select * from actor
delete from actor
insert into productionactors(pid,aid,entrymom) values (5,5,100),(6,6,10)
select * from productionactors
delete from productionactors

go
create or alter procedure addupdateactor(@aname varchar(10), @entrymom int, @pid int)
as
begin
	if not exists (select * from actor where @aname = name)
	begin
		raiserror('nf',16,1)
		return -1
	end

	if not exists (select * from production where @pid = id)
	begin
		raiserror('nf',16,1)
		return -1
	end

	declare @aid int = (select id from actor where @aname=name)

	if exists (select * from productionactors where @aid=aid and @pid = pid)
	begin
		update productionactors
		set entrymom=@entrymom
		where @aid=aid and @pid=pid
	end

	if not exists (select * from productionactors where @aid=aid and @pid = pid)
	begin
		insert into productionactors values (@pid, @aid, @entrymom)
	end

end

go
exec addupdateactor 'a1', 10, 6
select * from productionactors

-- 3
go
create or alter view showactors as
	select a.name
	from actor a inner join productionactors pa on a.id=pa.aid inner join production p on pa.pid=p.id
	group by a.name
	having count(pa.pid) = (select count(id) from production)

go
select * from showactors

-- 4
go
create or alter function showmovies(@p int)
returns table
as
return
	select m.name
	from movie m inner join production p on m.id=p.mid
	where m.rd > '2018-1-1'
	group by m.name
	having count(p.id)>@p

go
select * from production
select * from showmovies(2)


