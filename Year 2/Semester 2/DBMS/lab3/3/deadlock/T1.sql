USE Lab3_DBMS
GO

--SELECT * FROM Library
--SELECT * FROM Subscriber
--INSERT INTO Library(ID, Address, Nr_Of_Books) VALUES(20, 'Street nr 12', 120)
--INSERT INTO Subscriber(CNP, Name, Age, Nr_Of_Rented_Books) VALUES(20, 'SubscriberDeadlock', 20, 5)

-- UPDATE Subscriber SET Name = 'Ana' WHERE CNP = 20
-- UPDATE Library SET Address = 'Zalau, nr 123' WHERE ID = 20

-- part 1
BEGIN TRAN
-- exclusive look on table Library
UPDATE Library SET Address = 'Transaction 1' WHERE ID = 20
WAITFOR DELAY '00:00:10'

-- this transaction will be blocked, because T2 already has an exclusive lock on Subscriber
UPDATE Subscriber SET Name = 'Transaction 1' WHERE CNP = 20
COMMIT TRAN