DROP TABLE VersionTable
CREATE TABLE VersionTable(
	vers INT
)

DELETE FROM versionTable
INSERT INTO versionTable
VALUES (8)

DROP TABLE AuxTable
CREATE TABLE AuxTable(
	initial_version INT,
	final_version INT,
	procedure_name varchar(100),
	PRIMARY KEY(initial_version, final_version)

)

INSERT INTO AuxTable
VALUES
	(1,2,'changeMRSizeTinyInt'),
	(2,1,'changeMRSizeInt'),
	(2,3,'addCharactersColumnIsPopular'),
	(3,2,'removeCharactersColumnIsPopular'),
	(3,4,'addCharactersDefaultConstraintUnknown'),
	(4,3,'removeCharactersDefaultConstraintUnknown'),
	(4,5,'createTablePacks'),
	(5,4,'dropTablePacks'),
	(5,6,'addPrimaryKeyPacks'),
	(6,5,'removePrimaryKeyPacks'),
	(6,7,'addCandidateKeyPacks'),
	(7,6,'removeCandidateKeyPacks'),
	(7,8,'addForeignKeyPacks'),
	(8,7,'removeForeignKeyPacks')
GO

CREATE OR ALTER PROCEDURE goToVersion(@newVersion INT)
AS
BEGIN
	DECLARE @currentVersion INT
	DECLARE @procedure varchar(100)
	SELECT @currentVersion = vers FROM VersionTable

	IF (@newVersion > (SELECT MAX(final_version) FROM AuxTable) OR @newVersion<1)
		RAISERROR('Invalid Version',10,1)
		RETURN
	IF @newVersion = @currentVersion
		PRINT('Already in this version!')
	ELSE
	BEGIN
		WHILE @currentVersion>@newVersion
		BEGIN
			SELECT @procedure = procedure_name FROM AuxTable
								WHERE initial_version=@currentVersion
								AND final_version=@currentVersion-1
			EXEC @procedure
			SET @currentVersion=@currentVersion-1

		END

		WHILE @currentVersion<@newVersion
		BEGIN
			SELECT @procedure = procedure_name FROM AuxTable
								WHERE initial_version = @currentVersion
								AND final_version = @currentVersion+1
			EXEC @procedure
			SET @currentVersion=@currentVersion+1

		END

		UPDATE VersionTable SET vers = @newVersion

	END
END
GO

EXEC goToVersion 10

SELECT * FROM VersionTable
SELECT * FROM AuxTable