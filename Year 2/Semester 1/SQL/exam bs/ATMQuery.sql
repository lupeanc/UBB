use ATM

create table customer (
	id int primary key identity,
	name varchar(10),
	dob date
)

create table bankaccount(
	id int primary key identity,
	cid int references customer(id),
	iban int,
	balance int,

)

create table card (
	id int primary key identity,
	baid int references bankaccount(id),
	number int,
	cvv int

)

--create table bankcard (
--	baid int references bankaccount(id),
--	cid int references card(id),
--	primary key (baid,cid)
--)


create table atm (
	id int primary key identity,
	addr varchar(10)
)

create table transactions (
	id int primary key identity,
	atmid int references atm(id),
	cid int references card(id),
	money int,
	d datetime

)

-- 2
go
create or alter procedure deletetransactions(@cid int) as
begin
	if not exists (select * from card where @cid=id)
	begin
		raiserror('nf',16,1)
		return -1
	end

	if not exists (select * from transactions where @cid=cid)
	begin
		raiserror('nft',16,1)
		return -1
	end

	delete from transactions
	where @cid=cid

end

-- 3
insert into customer values ('a', null), ('b', null)
insert into bankaccount values (1,1,1), (2,2,100)
insert into card values (1,100,100),(2,10,10)
insert into atm values ('a1'), ('a2')
insert into transactions values (1,1,10, null),(1,2,10,null),(2,1,100,null)

go
create or alter view showcards as
	select c.id, c.number
	from card c inner join transactions t on c.id=t.cid inner join atm a on t.atmid=a.id
	group by c.number, c.id
	having count(distinct t.atmid) = (select count(id) from atm)

go
select * from showcards

-- 4
go
insert into transactions values (1,1,3000, null)
go
create or alter function listcards()
returns table
as
return
	select c.id, c.number,c.cvv
	from card c inner join transactions t on c.id = t.cid
	group by c.id, c.number,c.cvv
	having sum(t.money)>2000

go
select * from listcards()

