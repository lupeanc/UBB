use Pizza

create table droneman(
	id int primary key identity,
	name varchar(10)
)

create table dronemodel(
	id int primary key identity,
	mid int references droneman(id),
	name varchar(10),
	battery int,
	speed int
)

create table drone (
	id int primary key identity,
	mid int references dronemodel(id),
	serial int
)

create table pizzashop(
	id int primary key identity,
	name varchar(10),
	addr varchar(100)
)

create table customer(
	id int primary key identity,
	name varchar(10),
	score int
)

create table delivery(
	pid int references pizzashop(id),
	cid int references customer(id),
	did int references drone(id),
	d date,
	t time
	primary key(pid,cid,did)
)

-- 2
go
create or alter procedure addupdate(@cname varchar(10), @pname varchar(10), @did int, @d date, @t time)
as
begin
	declare @cid int = (select id from customer where name = @cname)
	declare @pid int = (select id from pizzashop where name=@pname)
	
	if not exists (select * from customer where name = @cname)
	begin
		raiserror('not found', 16,1)
		return -1
	end

	if not exists (select * from pizzashop where name = @pname)
	begin
		raiserror('not found', 16,1)
		return -1
	end

	if not exists (select * from drone where id = @did)
	begin
		raiserror('not found', 16,1)
		return -1
	end

	if exists (select * from delivery where cid=@cid and pid=@pid and did=@did)
	begin
		update delivery
		set d=@d, t=@t
		where cid=@cid and pid=@pid and did=@did
	end

	if not exists (select * from delivery where cid=@cid and pid=@pid and did=@did)
	begin
		insert into delivery values (@cid, @pid, @did, @d, @t)
	end

end

go
insert into customer values ('c1', 123),('c2', 123);
insert into pizzashop values ('p1','addr1');
insert into droneman values ('manuf1');
insert into dronemodel values (1,'model1',1,1);
insert into drone values (1, 12345)

exec addupdate 'c1','p1',1,'2021-1-1','1:00'
select * from delivery

exec addupdate 'c1','p1',1,'2022-1-1','2:00'
select * from delivery

-- 3
go
create or alter view showfavs as
	select dman.id, dman.name
	from droneman dman inner join dronemodel dmodel on dman.id=dmodel.mid inner join drone d on d.mid=dmodel.id
	group by dman.id, dman.name
	having count(*) >= all (select count(*)
							from droneman dman1 inner join dronemodel dmodel1 on dman1.id=dmodel1.mid inner join drone d1 on d1.mid=dmodel1.id
							)

go
select * from showfavs

--4
go
create or alter function listcustomers(@d int)
returns table
as
return
	select c.name
	from customer c inner join delivery d on c.id=d.cid
	group by c.name
	having count(*)>=@d

go
select * from listcustomers(1)
