-- phantoms
USE dbms_s6

--DELETE FROM Users WHERE name LIKE 'phantom:)'

BEGIN TRAN
WAITFOR DELAY '00:00:06'
INSERT INTO Users(name, city, dob) VALUES ('phantom:)', 'cc', '10-10-2002')
COMMIT TRAN