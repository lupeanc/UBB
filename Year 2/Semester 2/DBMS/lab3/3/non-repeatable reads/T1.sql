USE Lab3_DBMS
GO

--part 1
--INSERT INTO Library(ID, Address, Nr_Of_Books) VALUES(2, 'Baia Mare, nr 100', 400)
BEGIN TRAN
WAITFOR DELAY '00:00:04'
UPDATE Library SET Address = 'Timisoara, nr 30' WHERE ID = 2
COMMIT TRAN