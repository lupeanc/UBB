USE Lab3_DBMS
GO

-- SELECT * FROM Library
-- SELECT * FROM Subscriber

-- part 1
SET DEADLOCK_PRIORITY NORMAL
BEGIN TRAN
-- exclusive lock on Subscriber
UPDATE Subscriber SET Name = 'Transaction 2' WHERE CNP = 20
WAITFOR DELAY '00:00:10'

-- this transaction will be blocked, because T1 already has an exclusive lock on Library
UPDATE Library SET Address = 'Transaction 2' WHERE ID = 20
COMMIT TRAN

-- this transaction will be chosen as the deadlock victim
-- and it will terminate with an error
-- the tables will contain the values from T1