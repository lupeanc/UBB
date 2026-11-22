USE Lab3_DBMS
GO

CREATE OR ALTER PROCEDURE uspAddLibraryRecover(@id integer, @address VARCHAR(30), @nr_Of_Books integer)
AS
	SET NOCOUNT ON
	BEGIN TRAN
	BEGIN TRY
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
		COMMIT TRAN
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
	END CATCH
GO

CREATE OR ALTER PROCEDURE uspAddSubscriberRecover(@cnp integer, @name VARCHAR(30), @age integer, @nr_Of_Rented_Books integer)
AS
	SET NOCOUNT ON
	BEGIN TRAN
	BEGIN TRY
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
		COMMIT TRAN
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
	END CATCH
GO

		
CREATE OR ALTER PROCEDURE uspAddSubscriptionRecover(@library_id integer, @sub_cnp integer, @price integer)
AS
	SET NOCOUNT ON
	BEGIN TRAN
	BEGIN TRY
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
		COMMIT TRAN
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
	END CATCH
GO

CREATE OR ALTER PROCEDURE uspBadAddScenario
AS
	EXEC uspAddLibraryRecover 10, 'Street4', 2000
	EXEC uspAddSubscriberRecover 10, 'b', 16, 3 -- this will fail, but the item added before will still be in the database
	EXEC uspAddSubscriptionRecover 10, 10, 20 -- this fails as well, because of sql's insert constraints:
											  -- subscriber cnp is a fk for subscription. if subscriber cnp does not exist => sql will NOT insert
GO

CREATE OR ALTER PROCEDURE uspGoodAddScenario
AS
	EXEC uspAddLibraryRecover 12, 'Street3', 1000
	EXEC uspAddSubscriberRecover 12, 'Good', 21, 4
	EXEC uspAddSubscriptionRecover 12, 12, 20
GO

EXEC uspBadAddScenario
SELECT * FROM LogTable

EXEC uspGoodAddScenario
SELECT * FROM LogTable


SELECT * FROM Library
SELECT * FROM Subscriber
SELECT * FROM Subscription




DELETE FROM Library WHERE ID = 12
DELETE FROM Subscriber WHERE CNP = 12
DELETE FROM Subscription WHERE Library_ID = 12 AND CNP_Sub = 12