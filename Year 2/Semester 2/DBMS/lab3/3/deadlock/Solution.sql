USE Lab3_DBMS
GO

-- solution: set deadlock priority to high for the second transaction
-- now, T1 will be chosen as the deadlock victim, as it has a lower priority
-- default priority is normal (0)

SET DEADLOCK_PRIORITY HIGH
BEGIN TRAN
-- exclusive lock on table Subscriber
UPDATE Subscriber SET Name = 'Transaction 2' WHERE CNP = 20
WAITFOR DELAY '00:00:10'

UPDATE Library SET Address = 'Transaction 2' WHERE ID = 20
COMMIT TRAN

 --alternatively, the transactions could be changed to access the same tables in the same order
 BEGIN TRAN
UPDATE Library SET Address = 'Transaction 2' WHERE ID = 20
WAITFOR DELAY '00:00:10'

UPDATE Subscriber SET Name = 'Transaction 2' WHERE CNP = 20
COMMIT TRAN
