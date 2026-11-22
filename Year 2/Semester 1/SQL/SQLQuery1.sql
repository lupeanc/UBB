drop database VideoGames
create database VideoGames
go

--ce keyboard nice
use VideoGames
go

create table Genres(
	genid int primary key identity,
	genname varchar(50),
	gen_default_difficulty varchar(10)
);

create table Publishers(
	pubid int primary key identity,
	pubname varchar(50)
);

create table Platforms(
	pid int primary key identity,
	pname varchar(50),
	pdevice varchar(50)
);

create table MinRequirements(
	mrid int primary key identity,
	mrtype varchar(10),
	mrsize_gb int
);

--contorller type shi
create table SupportedInputs(
	siid int primary key identity,
	siname varchar(50)
);

create table Graphics(
	grid int primary key identity,
	grname varchar(50),
	grtype varchar(5),
	grpov varchar(50)
);

create table Characters(
	charid int primary key identity,
	charname varchar(50),
	charage int,
	charrole varchar(50)
);

create table Awards(
	aid int primary key identity,
	aname varchar(50),
	ayear int
);

create table AwardCategories(
	acid int primary key identity,
	acname varchar(50),
	acvotes int
);

create table Games(
	gid int primary key identity,
	gname varchar(50),
	gyear int,
	pubid int foreign key references Publishers(pubid),
	mrid int foreign key references MinRequirements(mrid),
	grid int foreign key references Graphics(grid)
);

create table GameGenres(
	gid int foreign key references Games(gid),
	genid int foreign key references Genres(genid),
	constraint pk_GameGenres primary key (gid, genid)
);

create table GamePlatforms(
	gid int foreign key references Games(gid),
	pid int foreign key references Platforms(pid),
	constraint pk_GamePlatforms primary key (gid, pid)
);

create table GameCharacters(
	gid int foreign key references Games(gid),
	charid int foreign key references Characters(charid),
	constraint pk_GameCharacters primary key (gid, charid)
);

create table GameSuppoertedInputs(
	gid int foreign key references Games(gid),
	siid int foreign key references SupportedInputs(siid),
	constraint pk_GameSupportedInputs primary key (gid,siid)
);

create table GameAwards(
	gid int foreign key references Games(gid),
	aid int foreign key references Awards(aid),
	acid int foreign key references AwardCategories(acid),
	constraint pk_GameAwards primary key (gid, aid, acid)
);