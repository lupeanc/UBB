USE Lab3_DBMS
GO

-- solution: set transaction isolation level to serializable
SET TRAN ISOLATION LEVEL SERIALIZABLE
BEGIN TRAN
SELECT * FROM Library
WAITFOR DELAY '00:00:06'
SELECT * FROM Library
COMMIT TRAN