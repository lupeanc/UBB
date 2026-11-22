--non rep read
USE practicdbms
GO
--INSERT INTO SmartDevices(name) VALUES('before');
UPDATE SmartDevices SET name='before' WHERE id=1;
--select * from SmartDevices

BEGIN TRAN
WAITFOR DELAY '00:00:06'
UPDATE SmartDevices SET name='non-repeatable' WHERE id=1
COMMIT TRAN

--select * from SmartDevices

