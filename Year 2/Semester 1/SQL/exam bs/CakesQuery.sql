use Cake

create table chef(
	id int primary key identity,
	name varchar(10),
	gender varchar(1),
	dob date
)

create table caketype(
	id int primary key identity,
	name varchar(10),
	descr varchar(10),
)

create table cake(
	id int primary key identity,
	tid int references caketype(id),
	cid int references chef(id),
	name varchar(10),
	shape varchar(10),
	weight int,
	price int,

)

create table ord(
	id int primary key identity,
	d date

)

create table cakeorder(
	oid int references ord(id),
	cid int references cake(id),
	pieces int,
	primary key(oid,cid)
)

--2
go
create or alter procedure addupdateorder(@oid int, @cname varchar(10), @p int)
as
begin
	declare @cid int = (select id from cake where name=@cname)

	if not exists (select * from ord where id=@oid)
	begin
		raiserror('nf',16,1)
		return -1
	end

	if not exists (select * from cake where id=@cid)
	begin
		raiserror('nf',16,1)
		return -1
	end

	if exists (select * from cakeorder where cid=@cid and oid=@oid)
	begin
		update cakeorder
		set pieces=@p
		where cid=@cid and oid=@oid
	end

	if not exists (select * from cakeorder where cid=@cid and oid=@oid)
	begin
		insert into cakeorder values (@oid, @cid, @p)
	end

end

go
insert into chef values ('chef1','F','2000-1-1')
insert into caketype values ('type1',null)
insert into cake values (1,1,'c1', null, 300, 100)
insert into ord values('2020-1-1')

exec addupdateorder 1,'c1',200
select * from cakeorder

-- 3
go
insert into chef values ('chef2','F','2000-1-1')
insert into caketype values ('type2',null)
insert into cake values (1,1,'c2', null, 300, 100)
insert into cake values (2,2,'c2', null, 300, 100)

select * from cake

go

create or alter function showchefs()
returns table
as
return
	select cf.name
	from chef cf inner join cake c on cf.id=c.cid
	group by cf.name
	having count(*) = (select count(distinct c1.name) as nbCakes
						from cake c1
					)

go
select * from showchefs()
	