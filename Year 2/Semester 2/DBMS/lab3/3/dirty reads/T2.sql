USE Lab3_DBMS;
GO

-- part 2; we can read uncommited data (dirty read)
SET TRAN ISOLATION LEVEL READ UNCOMMITTED
BEGIN TRAN
-- see update -> dirty read
SELECT * FROM Library
WAITFOR DELAY '00:00:10'
-- update was rolled back
SELECT * FROM Library
COMMIT TRAN

-- UPDATE Library SET Address = 'AddressDirtyRead' WHERE ID = 1