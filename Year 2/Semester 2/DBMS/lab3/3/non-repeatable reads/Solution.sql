USE Lab3_DBMS
GO

--solution: set transaction isolation level to repeatable read
-- this basically keeps the rows locked until t1 is commited fully. not just while the rows are being updated
SET TRAN ISOLATION LEVEL REPEATABLE READ
BEGIN TRAN
SELECT * FROM Library
WAITFOR DELAY '00:00:06'
-- now we see the value before the update
SELECT * FROM Library
COMMIT TRAN

-- DELETE FROM Library WHERE ID = 2