USE Lab3_DBMS
GO

--part 2: the row is changed while T2 is in progress, so we will se both values for address
SET TRAN ISOLATION LEVEL READ COMMITTED
BEGIN TRAN
-- see first insert
SELECT * FROM Library
WAITFOR DELAY '00:00:06'
SELECT * FROM Library
COMMIT TRAN

-- DELETE FROM Library WHERE ID = 2