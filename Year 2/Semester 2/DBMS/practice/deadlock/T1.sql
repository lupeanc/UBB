-- deadlock
USE dbms_s6

BEGIN TRAN

UPDATE Users SET name='dead' WHERE id=1

WAITFOR DELAY '00:00:06'

UPDATE Posts
SET shares=0
WHERE id=1
COMMIT TRAN

