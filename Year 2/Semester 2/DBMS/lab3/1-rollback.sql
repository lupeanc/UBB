USE Lab3_DBMS
GO

DROP TABLE IF EXISTS LogTable 
CREATE TABLE LogTable(
	Lid INT IDENTITY PRIMARY KEY,
	TypeOperation VARCHAR(50),
	TableOperation VARCHAR(50),
	ExecutionDate DATETIME
);

GO

-- use m:n relation Library - Subscriber

-- a string is valid <=> it is not null AND 2< length < 30
CREATE OR ALTER FUNCTION ufValidateString (@str VARCHAR(30))
RETURNS INT
AS
BEGIN
	DECLARE @return INT
	SET @return = 1
	IF(@str IS NULL OR LEN(@str) < 2 OR LEN(@str) > 30)
	BEGIN
		SET @return = 0
	END
	RETURN @return
END
GO

--int = valid <=> int > 0
CREATE OR ALTER FUNCTION ufValidateInt (@int integer)
RETURNS INT
AS
BEGIN
	DECLARE @return INT
	SET @return = 1
	IF(@int < 0)
	BEGIN
		SET @return = 0
	END
	RETURN @return
END
GO

CREATE OR ALTER PROCEDURE uspAddLibrary(@id integer, @address VARCHAR(30), @nr_Of_Books integer)
AS
	SET NOCOUNT ON
	IF (dbo.ufValidateString(@address) <> 1)
	BEGIN
		RAISERROR('Address is invalid', 14, 1)
	END
	IF (dbo.ufValidateInt(@nr_Of_Books) <> 1)
	BEGIN
		RAISERROR('Number of books is invalid', 14, 1)
	END
	IF EXISTS (SELECT * FROM Library L where L.ID = @id)
	BEGIN
		RAISERROR('Library already exists', 14, 1)
	END
	INSERT INTO Library VALUES (@id, @address, @nr_Of_Books)
	INSERT INTO LogTable VALUES ('add', 'library', GETDATE())
GO

CREATE OR ALTER PROCEDURE uspAddSubscriber(@cnp integer, @name VARCHAR(30), @age integer, @nr_Of_Rented_Books integer)
AS
	SET NOCOUNT ON
	IF (dbo.ufValidateString(@name) <> 1)
	BEGIN
		RAISERROR('Name is invalid', 14, 1)
	END
	IF (dbo.ufValidateInt(@age) <> 1)
	BEGIN
		RAISERROR('Age is invalid', 14, 1)
	END
	IF (dbo.ufValidateInt(@nr_Of_Rented_Books) <> 1)
	BEGIN
		RAISERROR('Number of rented books is invalid', 14, 1)
	END
	IF EXISTS (SELECT * FROM Subscriber S where S.CNP = @cnp)
	BEGIN
		RAISERROR('Subscriber already exists', 14, 1)
	END
	INSERT INTO Subscriber VALUES (@cnp, @name, @age, @nr_Of_Rented_Books)
	INSERT INTO LogTable VALUES ('add', 'subscriber', GETDATE())
GO

		
CREATE OR ALTER PROCEDURE uspAddSubscription(@library_id integer, @sub_cnp integer, @price integer)
AS
	SET NOCOUNT ON
	IF (dbo.ufValidateInt(@price) <> 1)
	BEGIN
		RAISERROR('Price is invalid', 14, 1)
	END
	IF EXISTS (SELECT * FROM Subscription S where S.Library_ID = @library_id AND S.CNP_Sub = @sub_cnp)
	BEGIN
		RAISERROR('Subscription already exists', 14, 1)
	END
	INSERT INTO Subscription VALUES (@library_id, @sub_cnp, @price)
	INSERT INTO LogTable VALUES ('add', 'subscription', GETDATE())
GO

CREATE OR ALTER PROCEDURE uspAddCommitScenario
AS
	BEGIN TRAN
	BEGIN TRY
		EXEC uspAddLibrary 11, 'Street2', 1000
		EXEC uspAddSubscriber 11, 'Success', 20, 3
		EXEC uspAddSubscription 11, 11, 30
		COMMIT TRAN
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
		RETURN
	END CATCH
GO


CREATE OR ALTER PROCEDURE uspAddRollbackScenario
AS 
	BEGIN TRAN
	BEGIN TRY
		EXEC uspAddLibrary 10, 'Fail', 500
		EXEC uspAddSubscriber 10, 'a', 10, 2 -- this will fail due to validation, so everything fails
		EXEC uspAddSubscription 10, 10, 10
		COMMIT TRAN
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
		RETURN
	END CATCH
GO

EXEC uspAddRollbackScenario
EXEC uspAddCommitScenario

SELECT * FROM LogTable

SELECT * FROM Library
SELECT * FROM Subscriber
SELECT * FROM Subscription


DELETE FROM Library WHERE ID = 11
DELETE FROM Subscriber WHERE CNP = 11
DELETE FROM Subscription WHERE Library_ID = 11 AND CNP_Sub = 11 