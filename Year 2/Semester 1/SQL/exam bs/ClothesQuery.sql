use Clothing

create table type (
	id int primary key identity,
	name varchar(10),
	season varchar(10),
	descr varchar(10),
)

insert into type values ('name', 's1', 'd1'),('name2', 's1', 'd1')

create table brand (
	id int primary key identity,
	title varchar(10),
	logo image,
	style varchar(10),
	colors varchar(10),
	fabric varchar(10),
	theme varchar(10),
	fyear int,
	country varchar(10)

)

insert into brand values ('b1',null,'s1','c1','f1','t1',2020,'country1'), ('b2',null,'s2','c2','f2','t2',2010,'country2')

drop table clothes
create table clothes(
	id int primary key identity,
	tid int references type(id),
	bid int references brand(id),
	name varchar(10),
	model varchar(100),
	color varchar(10),
	rd date,
	price int
	
)

insert into clothes values (1,1,'c1','French Flowers', 'color1', '2020-1-1', 100),
(2,1,'c1','f', 'color1', '2020-1-1', 100),
(2,2,'c1','f', 'color1', '2020-1-1', 100);

create table shopper(
	id int primary key identity,
	name varchar(10),
	lcard varchar(3) check (lcard like 'yes' or lcard like 'no'),
	points int,
	gender varchar(1),
	dob date

)

insert into shopper values ('s1','yes',100,'f','2000-1-1'),('s2','no', 0,'m','2000-1-1')

create table purchase(
	id int primary key identity,
	sid int references shopper(id),
	cid int references clothes(id),
	d date,
	amount int
)

insert into purchase values (1,1,'2020-1-1',10)

-- 2
go
create or alter procedure addupdate(@sid int, @cid int, @d date, @amount int)
as
begin
	if not exists (select * from shopper where @sid=id)
	begin
		raiserror('nf',16,1)
		return -1
	end

	if not exists (select * from clothes where @cid=id)
	begin
		raiserror('nf',16,1)
		return -1
	end

	if exists (select * from purchase where @cid=cid and @sid=sid)
	begin
		update purchase
		set amount=@amount, d=@d
		where @cid=cid and @sid=sid
	end

	if not exists (select * from purchase where @cid=cid and @sid=sid)
	begin
		insert into purchase values (@sid,@cid,@d, @amount)
	end

end

go
exec addupdate 1,1,'2020-1-1',100
exec addupdate 2,2,'2020-1-1',10
select * from purchase
-- 3
go
create or alter view showbrands as
	select b.title
	from brand b inner join clothes c on b.id = c.bid
	where c.model like 'French flowers'

go
select * from showbrands

-- 4
go
create or alter function showshoppers()
returns table
as
return
		select s.name
		from shopper s inner join purchase p on s.id=p.sid inner join clothes c on p.cid=c.id
		group by s.name
		having count(p.cid) = (select count(id) from clothes)

go
select * from showshoppers()

select * from clothes
select * from purchase
insert into purchase values (1,2,'2020-1-1',10),(1,3,'2020-1-1',10)