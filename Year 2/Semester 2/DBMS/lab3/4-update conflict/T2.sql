USE Lab3_DBMS
GO

-- update conflict
SET TRAN ISOLATION LEVEL SNAPSHOT
-- basically works with a snapshot of the db, not the db itself
-- as to not have readers blocking writers/vice versa
BEGIN TRAN

WAITFOR DELAY '00:00:05'

-- T1 has now updated and obtained a lock on this table
-- trying to update the same row will result in a error (process is blocked)
UPDATE Library SET Address = 'New name 2' WHERE ID = 200
COMMIT TRAN