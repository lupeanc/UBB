--a. UNION[ALL] AND OR
--Select all new games + the sequels of older ones
SELECT g.gname
FROM Games g
WHERE gname LIKE '%2' OR gyear>=2020

select * from Games
SELECT g1.gname
FROM Games g1
WHERE g1.gname LIKE '%2'
UNION
SELECT g2.gname
FROM Games g2
WHERE g2.gyear>=2020

--Select all character's whose name starts with J + the main characters
SELECT c.charname, c.charrole
FROM Characters c
WHERE c.charname LIKE 'J%' OR c.charrole LIKE 'Main%'

select * from Characters
SELECT c1.charname, c1.charrole
FROM Characters c1
WHERE c1.charname LIKE 'J%'
UNION ALL
SELECT c2.charname, c2.charrole
FROM Characters c2
WHERE c2.charrole LIKE 'Main%'

--b. INTERSECT AND IN + OR
select * from Graphics
SELECT *
FROM Graphics
WHERE grtype LIKE '3D'
INTERSECT
SELECT *
FROM Graphics
WHERE grpov LIKE 'First%' OR grpov LIKE 'Customizable%'

--IN + ORDER BY
select * from Awards
SELECT *
FROM Awards
WHERE aname LIKE 'Steam%'
INTERSECT
SELECT *
FROM Awards
WHERE ayear IN (2020, 2022, 2025)
ORDER BY ayear

--c. EXCEPT AND NOT IN
select * from Publishers
SELECT p1.pubname
FROM Publishers p1
WHERE pubname LIKE '%_ _%'
EXCEPT
SELECT p2.pubname
FROM Publishers p2
WHERE p2.pubname LIKE '%Fox'

--All characters under 30 + whose charrole=main...
 -- + ORDER BY
select * from Characters
SELECT *
FROM Characters
WHERE charage <=30
EXCEPT
SELECT *
FROM Characters
WHERE charrole NOT IN ('Main Character', 'Main Helper')
ORDER BY charage

--d. INNER - 3 TABLES + TOP
SELECT TOP 5 g.gname, c.charname, c.charage+20 as EstimatedAgeDuringSequels
FROM Games g INNER JOIN GameCharacters gc ON g.gid = gc.gid
INNER JOIN Characters c ON gc.charid = c.charid

--LEFT OUTER - 2 many to many
SELECT g.gname,Awards.aname, Awards.ayear, AwardCategories.acname
FROM Games g LEFT OUTER JOIN GameAwards ga ON g.gid=ga.gid
LEFT OUTER JOIN Awards ON ga.aid=Awards.aid
LEFT OUTER JOIN AwardCategories ON AwardCategories.acid=ga.acid
ORDER BY Awards.ayear

--RIGHT OUTER - 3 TABLES + TOP
select * from Games
SELECT TOP 5 Games.gname, Publishers.pubname
FROM Games RIGHT OUTER JOIN Publishers ON Games.pubid = Publishers.pubid

--FULL JOIN - 2 many to many
SELECT Games.gname, Platforms.pname, SupportedInputs.siname
FROM Games FULL OUTER JOIN  GamePlatforms ON Games.gid=GamePlatforms.gid
FULL OUTER JOIN Platforms ON GamePlatforms.pid=Platforms.pid
FULL OUTER JOIN GameSupportedInputs ON Games.gid=GameSupportedInputs.gid
FULL OUTER JOIN SupportedInputs ON GameSupportedInputs.siid=SupportedInputs.siid

--e. IN + SUBQUERY + AND
SELECT g.gname, MinRequirements.mrtype
FROM Games g, MinRequirements
WHERE g.mrid = MinRequirements.mrid AND g.gname IN (
	SELECT g2.gname
	FROM Games g2
	WHERE g2.gname LIKE '%_ _%' AND g2.gyear>2012
)

--All PC games - with awards newer than 2010 - with the sum of their votes >= 4000
SELECT g.gname
FROM Platforms p, Games g
WHERE p.pdevice LIKE '%PC%' AND g.gname IN (
	SELECT g2.gname
	FROM Games g2 INNER JOIN GameAwards ga ON g2.gid=ga.gid
	INNER JOIN Awards a ON a.aid=ga.aid 
	WHERE a.ayear>2010 AND (
		SELECT SUM(ac.acvotes)
		FROM GameAwards ga2 INNER JOIN AwardCategories ac ON ga2.acid=ac.acid
		WHERE a.aid=ga2.aid 
	) >=4000
)

--f. EXISTS
--Select all main characters that appear in games
SELECT c.charname, c.charage-10 as AgeDuringPrequel
FROM Characters c
WHERE c.charrole LIKE 'Main%' AND EXISTS (
	SELECT *
	FROM GameCharacters gc
	WHERE c.charid=gc.charid
)

--Select all genres that are found in the games from the db
SELECT DISTINCT gen.genname
FROM Genres gen
WHERE EXISTS (
	SELECT *
	FROM GameGenres gg
	WHERE gg.genid=gen.genid
)

--g. FROM wth SUBQ
SELECT A.charid
FROM (
	SELECT DISTINCT g.gid, gc.charid
	FROM Games g INNER JOIN MinRequirements mr ON g.mrid = mr.mrid
	INNER JOIN GameCharacters gc ON g.gid=gc.gid
	WHERE mr.mrtype LIKE 'High'
) A

SELECT B.grid
FROM (
	SELECT DISTINCT g.gid, gr.grid
	FROM Graphics gr INNER JOIN Games g ON g.grid=gr.grid INNER JOIN GameGenres gg ON g.gid=gg.gid
	INNER JOIN Genres gen ON gen.genid=gg.genid
	WHERE gen.gen_default_difficulty NOT IN ('%Easy%')
) B

--h. GROUP BY
SELECT g.gname, COUNT(*) as NumberOfCharacters
FROM Games g INNER JOIN GameCharacters gc ON g.gid=gc.gid
INNER JOIN Characters c ON gc.charid=c.charid
GROUP BY g.gname

SELECT g.gname, SUM(ac.acvotes) as Sum, AVG(ac.acvotes) as Average, COUNT(ac.acvotes) as Counter
FROM Games g INNER JOIN GameAwards ga ON g.gid=ga.gid
INNER JOIN AwardCategories ac ON ga.acid=ac.acid
GROUP BY g.gname
HAVING AVG(ac.acvotes)>1500

--Games which came out later than the avergae of all games
SELECT g.gname, g.gyear
FROM Games g
GROUP BY g.gname, g.gyear
HAVING MAX(g.gyear)>(
	SELECT AVG(g2.gyear) as avrg
	FROM Games g2
)

--award categoris having the max number of votes equal to the average of all votes
SELECT ac.acname
FROM Awards a INNER JOIN GameAwards ga ON a.aid=ga.aid
INNER JOIN AwardCategories ac ON ac.acid=ga.acid
GROUP BY ac.acname
HAVING MAX(ac.acvotes)=(
	SELECT AVG(ac2.acvotes)
	FROM AwardCategories ac2
)

--awards having the min of votes in their award categories smaller than the average
SELECT a.aname
FROM Awards a INNER JOIN GameAwards ga ON a.aid=ga.aid
INNER JOIN AwardCategories ac ON ac.acid=ga.acid
GROUP BY a.aname
HAVING MIN(ac.acvotes)<(
	SELECT AVG(ac2.acvotes)
	FROM AwardCategories ac2
)

--i.
--platforms names + devices which also have older games (<=2022)
SELECT p.pname, p.pdevice
FROM Platforms p
WHERE p.pid<>ALL(
	SELECT p2.pid
	FROM Games g INNER JOIN GamePlatforms gp ON g.gid=gp.gid
	INNER JOIN Platforms p2 ON p2.pid=gp.pid
	WHERE g.gyear>=2023
)

SELECT p.pname, p.pdevice
FROM Platforms p
WHERE p.pid NOT IN(
	SELECT p2.pid
	FROM Games g INNER JOIN GamePlatforms gp ON g.gid=gp.gid
	INNER JOIN Platforms p2 ON p2.pid=gp.pid
	WHERE g.gyear>=2023
)

--select characters and their updated age if they are in the franchise 'Call of Duty'
SELECT c.charname, c.charage+2 as AgeUpdatedAfterInterviews
FROM Characters c
WHERE c.charname=ANY(
	SELECT c2.charname
	FROM Games g INNER JOIN GameCharacters gc ON g.gid=gc.gid
	INNER JOIN Characters c2 ON c2.charid=gc.charid
	WHERE g.gname LIKE 'Call of Duty%'
)

SELECT c.charname, c.charage+2 as AgeUpdatedAfterInterviews
FROM Characters c
WHERE c.charname IN (
	SELECT c2.charname
	FROM Games g INNER JOIN GameCharacters gc ON g.gid=gc.gid
	INNER JOIN Characters c2 ON c2.charid=gc.charid
	WHERE g.gname LIKE 'Call of Duty%'
)

--select awards and award categories where the votes are >=
--than the max of the awards with the id < 3
SELECT a.aname, a.ayear, ac.acid, ac.acname, ac.acvotes
FROM Awards a INNER JOIN GameAwards ga ON a.aid=ga.aid
INNER JOIN AwardCategories ac ON ac.acid=ga.acid
WHERE ac.acvotes>=ALL(
	SELECT ac2.acvotes
	FROM AwardCategories ac2
	WHERE ac2.acid<3
)

SELECT a.aname, a.ayear, ac.acid, ac.acname, ac.acvotes
FROM Awards a INNER JOIN GameAwards ga ON a.aid=ga.aid
INNER JOIN AwardCategories ac ON ac.acid=ga.acid
WHERE ac.acvotes>=(
	SELECT MAX(ac2.acvotes)
	FROM AwardCategories ac2
	WHERE ac2.acid<3
)

--select games where the year is smaller than the
--min of the games who have over 2500 votes in any category
SELECT g.gname, g.gyear
FROM Games g
WHERE g.gyear<ALL(
	SELECT g2.gyear
	FROM Games g2 INNER JOIN GameAwards ga ON g2.gid=ga.gid
	INNER JOIN AwardCategories ac ON ac.acid=ga.acid
	WHERE ac.acvotes>2500
)

SELECT g.gname, g.gyear
FROM Games g
WHERE g.gyear<(
	SELECT MIN(g2.gyear)
	FROM Games g2 INNER JOIN GameAwards ga ON g2.gid=ga.gid
	INNER JOIN AwardCategories ac ON ac.acid=ga.acid
	WHERE ac.acvotes>2500
)