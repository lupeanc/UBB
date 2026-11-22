use Shoes

create table pshop (
	id int primary key identity,
	name varchar(10),
	city varchar(10)
)

create table woman (
	id int primary key identity,
	name varchar(10),
	amount int
)

create table model (
	id int primary key identity,
	name varchar(10),
	season varchar(10)
)

create table shoe (
	id int primary key identity,
	mid int references model(id),
	price int,
)

create table shoepshop(
	sid int references shoe(id),
	pid int references pshop(id),
	nb int,
	primary key(sid,pid)
)

create table womanshoe(
	sid int references shoe(id),
	wid int references woman(id),
	nb int,
	amount int,
	primary key(sid,wid)	
)

-- 2 + if shoe exists in that pshop, update nb
go
create or alter procedure addshoe(@shoeid int, @pshopid int, @nb int) as
begin
	if not exists (select * from shoe where @shoeid = id)
	begin
		raiserror('not found', 16,1)
		return -1
	end
	
	if not exists (select * from pshop where @pshopid = id)
	begin
		raiserror('not found', 16,1)
		return -1
	end

	if exists (select * from shoepshop where @shoeid=sid and @pshopid=pid)
	begin
		update shoepshop
		set nb=@nb
		where sid=@shoeid and pid=@pshopid
	end

	if not exists (select * from shoepshop where @shoeid=sid and @pshopid=pid)
	begin
		insert into shoepshop values (@shoeid, @pshopid, @nb)
	end

end

go

insert into shoe values
	(1,100),
	(1,200),
	(2,100);

insert into model values
	('caca', null),
	('m', null);

insert into pshop values
	('caca', null),
	('m', null);


exec addshoe 1,1,1
select * from shoepshop

exec addshoe 1,1,2
--exec addshoe 1,2,100
select * from shoepshop

exec addshoe 2,1,100
select * from shoepshop


-- 3
insert into woman values 
	('a', 1000),
	('b',1000);

insert into womanshoe values
	(1,1,2,100)

go
create or alter view showwomen as
	select w.id, w.name
	from woman w
	where w.id in (select ws.wid
					from womanshoe ws inner join shoe s on ws.sid=s.id
					where s.mid = 1
					group by ws.wid
					having sum(ws.nb)>=2)
go
select * from showwomen

-- 4
go
create or alter function showshoes(@t int)
returns table
as
return
	select s.id
	from shoe s inner join shoepshop sps on s.id=sps.sid
	group by s.id
	having count(sps.pid) > @t

go
select * from showshoes(1)