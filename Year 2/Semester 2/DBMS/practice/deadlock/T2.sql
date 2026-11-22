-- deadlock
USE dbms_s6

-- best fix: do everything in the same order. if not, choose this one as the winner
--SET DEADLOCK_PRIORITY HIGH
SET DEADLOCK_PRIORITY NORMAL
BEGIN TRAN
UPDATE Posts
SET shares=0
WHERE id=1

WAITFOR DELAY '00:00:06'

UPDATE Users
SET name='dead'
WHERE id=1
COMMIT TRAN
