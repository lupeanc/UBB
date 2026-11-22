USE practicdbms
GO

-- FIX:
-- REPEATABLE READ forces transactions to keep their SLocks until the end => this will print the initial value
--SET TRAN ISOLATION LEVEL REPEATABLE READ
SET TRAN ISOLATION LEVEL READ COMMITTED
BEGIN TRAN
-- before update
SELECT * FROM SmartDevices
WAITFOR DELAY '00:00:06'
-- after update: different value
SELECT * FROM SmartDevices
COMMIT TRAN

-- WHY DOES THIS HAPPEN?
-- T2's isolation level is READ COMMITTED.
-- Under this iso level, SELECT aquires a SLock, and then it IMMEDIATELY lets it go (not at the end of the transaction)
-- this means that other transaction can now aquire an SLock and XLock on the obj previously SLocked by T2
-- therefore, another T can modify the value alread read by T2
-- => NON-REPEATABLE READS (obj does not have the same value)
