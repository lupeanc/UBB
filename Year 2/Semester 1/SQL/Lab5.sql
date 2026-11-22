USE A5
DROP TABLE Tc
DROP TABLE Tb
DROP TABLE Ta

-- Tables creation
CREATE TABLE Ta (
	aid INT PRIMARY KEY,
	a2 INT UNIQUE,
	a3 INT
)
DELETE FROM Ta

CREATE TABLE Tb (
	bid INT PRIMARY KEY,
	b2 INT
)

CREATE TABLE Tc (
	cid INT PRIMARY KEY,
	aid INT FOREIGN KEY REFERENCES Ta(aid),
	bid INT FOREIGN KEY REFERENCES Tb(bid)
)

-- Procedure to generate and insert random data into Ta
GO
CREATE OR ALTER PROCEDURE insertIntoTa(@rows INT) AS
BEGIN
	DECLARE @max INT
	SET @max = @rows*2 + 100
	WHILE @rows > 0
	BEGIN
		INSERT INTO Ta VALUES (@rows, @max, @max%210)
		SET @rows = @rows - 1
		SET @max = @max - 2
	END
END

-- Procedure to generate and insert random data into Tb
GO
CREATE OR ALTER PROCEDURE insertIntoTb(@rows INT) AS
BEGIN
	WHILE @rows > 0 
	BEGIN
		INSERT INTO Tb VALUES(@rows, @rows%542)
		SET @rows = @rows - 1
	END
END

-- Procedure to generate and insert random data into Tc
GO
CREATE OR ALTER PROCEDURE insertIntoTc(@rows INT) AS
BEGIN
	DECLARE @aid INT
	DECLARE @bid INT
	WHILE @rows > 0
	BEGIN
		SET @aid = (SELECT TOP 1 aid FROM Ta ORDER BY NEWID())
		SET @bid = (SELECT TOP 1 bid FROM Tb ORDER BY NEWID())
		INSERT INTO Tc VALUES(@rows, @aid, @bid)
		SET @rows = @rows - 1
	END
END

-- Inserting data
EXEC insertIntoTa 1000
EXEC insertIntoTb 1000
EXEC insertIntoTc 1000

SELECT *
FROM Ta

SELECT *
FROM Tb

SELECT *
FROM Tc

/* 
TASKS
OBS: 
- We have a clustered index automatically created for the aid column from Ta
- We have a nonclustered index automatically created for the a2 column from Ta
- We have a clustered index automatically created for the bid column from Tb
- We have a clustered index automatically created for the cid column from Tc
*/

-- a) Write queries on Ta such that their execution plans contain the following operators:
-- clustered index scan - scan the entire table 
SELECT *
FROM Ta

-- clustered index seek - return a specific subset of rows from a clustered index
SELECT *
FROM Ta
WHERE aid < 152

-- nonclustered index scan - scan the entire nonclustered index
--DROP INDEX IF EXISTS nonClusteredIndexTa ON Ta
--CREATE NONCLUSTERED INDEX nonClusteredIndexTa ON Ta (a2)

SELECT a2
FROM Ta
ORDER BY a2

-- nonclustered index seek - return a specific subset of rows from a nonclustered index
SELECT a2
FROM Ta
WHERE a2 BETWEEN 120 AND 130

-- key lookup - nonclustered index seek + key lookup - the data is found in a nonclustered index, but additional data is needed
SELECT a3, a2
FROM Ta
WHERE a2 = 544

-- b) Write a query on table Tb with a WHERE clause of the form WHERE b2 = value and analyze its execution plan. Create a nonclustered index that can speed up the query. Examine the execution plan again.
-- Before creating a nonclustered index we have a clustered index scan
IF EXISTS (SELECT name FROM sys.indexes WHERE name = N'Tb_b2_index')
	DROP INDEX Tb_b2_index ON Tb
GO

CREATE NONCLUSTERED INDEX Tb_b2_index ON Tb (b2)
GO
-- After creating the nonclustered index on b2, we have a noclustered index seek
SELECT *
FROM Tb
WHERE b2 = 123

-- c) Create a view that joins at least 2 tables. Check whether existing indexes are helpful; if not, reassess existing indexes / examine the cardinality of the tables.

GO
CREATE OR ALTER VIEW View1 AS
	SELECT A.aid, B.bid, C.cid
	FROM Tc C
	INNER JOIN Ta A ON A.aid = C.aid
	INNER JOIN Tb B ON B.bid = C.bid
	WHERE B.b2 > 500 AND A.a3 < 150

GO
SELECT *
FROM View1

IF EXISTS (SELECT name FROM sys.indexes WHERE name = N'Ta_a3_index')
	DROP INDEX Ta_a3_index ON Ta
GO

CREATE NONCLUSTERED INDEX Ta_a3_index ON Ta(a3) --0.0035944
GO

IF EXISTS (SELECT name FROM sys.indexes WHERE name = N'Tc_index')
	DROP INDEX Tc_index ON Tc
GO

CREATE NONCLUSTERED INDEX Tc_index ON Tc(aid, bid)
GO