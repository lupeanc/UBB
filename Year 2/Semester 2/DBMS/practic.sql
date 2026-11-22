--CREATE DATABASE practicdbms

USE practicdbms

CREATE TABLE Neighborhood(
	id int primary key identity,
	name varchar(100),
	location varchar(100)
)

CREATE TABLE MainResident(
	id int primary key identity,
	name varchar(100),
	phone varchar(12)
)

CREATE TABLE SmartHomes(
	id int primary key identity,
	name varchar(100),
	address varchar(100),
	nid int foreign key references Neighborhood(id),
	mrid int foreign key references MainResident(id)
)
--USE practicdbms
--DROP TABLE SmartHomeDevices
--DROP TABLE SmartDevices

CREATE TABLE SmartDevices(
	id int primary key identity,
	-- added a name here in order to use it for non-rep read so we dont mess with the tables for ex 2
	name varchar(100)
)

CREATE TABLE SmartHomeDevices(
	id int primary key identity,
	shid int foreign key references SmartHomes(id),
	sdid int foreign key references SmartDevices(id)
)

INSERT INTO Neighborhood(name, location) VALUES ('n1', 'l1'), ('n2', 'l2')

INSERT INTO MainResident(name, phone) VALUES ('r1', '09983131')

INSERT INTO SmartHomes(name, address, nid, mrid) VALUES ('s1', 'a1', 1, 1), ('s2', 'a2', 1, 1)

select * from SmartHomes