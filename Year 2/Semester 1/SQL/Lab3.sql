USE VideoGames
GO

--a. modify the type of a column
CREATE OR ALTER PROCEDURE changeMRSizeTinyInt AS
BEGIN
	ALTER TABLE MinRequirements
	ALTER COLUMN mrsize_gb tinyint NOT NULL
END
GO

CREATE OR ALTER PROCEDURE changeMRSizeInt AS
BEGIN
	ALTER TABLE MinRequirements
	ALTER COLUMN mrsize_gb int
END
GO

--b. add/remove column
CREATE OR ALTER PROCEDURE addCharactersColumnIsPopular AS
BEGIN
	ALTER TABLE Characters
	ADD isPopular varchar(5)
END
GO

CREATE OR ALTER PROCEDURE removeCharactersColumnIsPopular AS
BEGIN
	ALTER TABLE Characters
	DROP COLUMN isPopular
END
GO

--c. add/remove default constraint
CREATE OR ALTER PROCEDURE addCharactersDefaultConstraintUnknown AS
BEGIN
	ALTER TABLE Characters
	ADD CONSTRAINT df_unknownRole DEFAULT 'Unknown' FOR charrole
END
GO

CREATE OR ALTER PROCEDURE removeCharactersDefaultConstraintUnknown AS
BEGIN
	ALTER TABLE Characters
	DROP CONSTRAINT df_unknownRole
END
GO


-- g. create/drop table
CREATE OR ALTER PROCEDURE createTablePacks AS
BEGIN
	create table Packs(
		packid int primary key identity,
		packName varchar(100),
		packGoodieCounter int not null
	)
END
GO

CREATE OR ALTER PROCEDURE dropTablePacks AS
BEGIN
	DROP TABLE Packs
END
GO

--d. add/remove primary key
CREATE OR ALTER PROCEDURE addPrimaryKeyPacks AS
BEGIN
	ALTER TABLE Packs
	ADD CONSTRAINT Packs_PrimaryKey PRIMARY KEY (packid)
END
GO

CREATE OR ALTER PROCEDURE removePrimaryKeyPacks AS
BEGIN
	ALTER TABLE Packs
	DROP CONSTRAINT Packs_PrimaryKey
END
GO

-- e. add/remove candidate key
CREATE OR ALTER PROCEDURE addCandidateKeyPacks AS
BEGIN
	ALTER TABLE Packs
	ADD CONSTRAINT Packs_CandidateKey UNIQUE (packName)
END
GO

CREATE OR ALTER PROCEDURE addCandidateKeyPacks AS
BEGIN
	ALTER TABLE Packs
	DROP CONSTRAINT Packs_CandidateKey
END
GO


-- f. add/remove foreign key
CREATE OR ALTER PROCEDURE addForeignKeyPacks AS
BEGIN
	ALTER TABLE Packs
	ADD CONSTRAINT FK_GameID FOREIGN KEY(gid) REFERENCES Games(gid)
END
GO

CREATE OR ALTER PROCEDURE removeForeignKeyPacks AS
BEGIN
	ALTER TABLE Packs
	DROP CONSTRAINT FK_GameID
END
GO

----d. add/remove primary key
--CREATE OR ALTER PROCEDURE addPrimaryKeyPlatforms AS
--BEGIN
--	ALTER TABLE Platforms
--	ADD CONSTRAINT Platforms_PrimaryKey PRIMARY KEY (Pid)
--END
--GO

--CREATE OR ALTER PROCEDURE removePrimaryKeyPlatforms AS
--BEGIN
--	ALTER TABLE Platforms
--	DROP CONSTRAINT Platforms_PrimaryKey
--END
--GO

---- e. add/remove candidate key
--CREATE OR ALTER PROCEDURE addCandidateKeyGames AS
--BEGIN
--	ALTER TABLE Games
--	ADD CONSTRAINT Games_CandidateKey UNIQUE (gname)
--END
--GO

--CREATE OR ALTER PROCEDURE addCandidateKeyGames AS
--BEGIN
--	ALTER TABLE Games
--	DROP CONSTRAINT Games_CandidateKey
--END
--GO

----select * from Games
---- f. add/remove foreign key
--CREATE OR ALTER PROCEDURE addForeignKeyGames AS
--BEGIN
--	ALTER TABLE Games
--	ADD CONSTRAINT FK_PublisherID FOREIGN KEY(pubid) REFERENCES Publishers(pubid)
--END
--GO

--CREATE OR ALTER PROCEDURE removeForeignKeyGames AS
--BEGIN
--	ALTER TABLE Games
--	DROP CONSTRAINT FK_PublisherID
--END
--GO
