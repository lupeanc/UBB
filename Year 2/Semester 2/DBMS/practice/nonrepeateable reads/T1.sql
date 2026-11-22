-- non rep read
USE dbms_s6

--UPDATE Users SET name='before non-rep' WHERE id=1

BEGIN TRAN

WAITFOR DELAY '00:00:06'
UPDATE Users
SET name='non-rep'
WHERE id=1

COMMIT TRAN
