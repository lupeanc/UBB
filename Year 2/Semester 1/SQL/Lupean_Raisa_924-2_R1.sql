use Practic

create table genre(
	id int primary key identity,
	name varchar(10),
	descr varchar(100)
)

insert into genre values ('g1',null)
insert into genre values ('g2',null)

create table movie (
	id int primary key identity,
	gid int references genre(id),
	title varchar(100),
	yearp int,
	d int
)

insert into movie values (2,'movieDifGenre', 2020, 120)
insert into movie values (1,'movie3', 2020, 120), (1,'movie1', 2020, 120),(1,'movie2', 2000, 180);

create table cinema(
	id int primary key identity,
	name varchar(10) unique,
)

insert into cinema values ('cinema1')
insert into cinema values ('cinema2')

-- could have made pair cid,mid the primary key
create table cinemafilm(
	id int primary key identity,
	cid int references cinema(id),
	mid int references movie(id),
	t time,
)
insert into cinemafilm values (1,1,'20:00')
insert into cinemafilm values (2,1,'20:00')
select * from cinemafilm

create table ticket(
	id int primary key identity,
	cfid int references cinemafilm(id),
	seat int,
	price int,

)
insert into ticket values (1,13,10)
insert into ticket values (3,123,10)
insert into ticket values (1,123,10)


-- 2
go
create or alter procedure addupdatemovie(@mid int, @cname varchar(10), @t time)
as
begin
	declare @cid int = (select id from cinema where @cname = name)

	if not exists (select * from cinema where @cid=id)
	begin
		raiserror('cinema nf', 16,1)
		return -1
	end

	if not exists (select * from movie where @mid=id)
	begin
		raiserror('movie nf', 16,1)
		return -1
	end

	if exists (select * from cinemafilm where @cid=cid and @mid=mid)
	begin
		update cinemafilm
		set t=@t
		where @cid=cid and @mid=mid
	end

	if not exists (select * from cinemafilm where @cid=cid and @mid=mid)
	begin
		insert into cinemafilm values (@cid, @mid, @t)
	end

end

go
-- error
exec addupdatemovie 5,'cinema1', '1:00'
select * from cinemafilm

-- UPDATE
exec addupdatemovie 1,'cinema1', '10:00'
select * from cinemafilm

-- NOT INSERTED YET - DONT INSERT IT
exec addupdatemovie 3,'cinema1', '2:00'
select * from cinemafilm

-- 3
go
create or alter view showtickets as
	select c.id as cinema, count(t.id) as noOfTickets
	from cinema c inner join cinemafilm cf on c.id=cf.cid inner join ticket t on cf.id = t.cfid
	group by c.id

go
select * from showtickets

select * from cinema
select * from cinemafilm
select * from ticket

-- cinema 1 has 2 tickets, cinema 2 has 1 ticket

-- 4
go
create or alter function showmovies(@g int, @y int)
returns table
as
return
	select *
	from movie m
	where @g = m.gid and m.yearp > @y

go
select * from showmovies(1,2010)
select * from movie

-- movie 2 should not be visible (year), movieDifGenre should not be visible, the others should
