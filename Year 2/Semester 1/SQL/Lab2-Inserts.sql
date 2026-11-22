-- INSERT FOR GENRES - no violations
insert into Genres (genname, gen_default_difficulty)
values ('Shooter', 'Average'),
('Open World', 'Easy'),
('RPG', 'Average'),
('Horror', 'Hard'),
('Relaxing', 'Easy');

select * from Genres;

-- INSERT INTO PUBLISHERS
insert into Publishers (pubname)
values ('EA'),
('GhostShip Games'),
('Toby Fox'),
('Respawn'),
('Semiwork Studios'),
('Activision'),
('Microsoft'),
('Test Publisher');

select * from Publishers;

-- INSERT INTO PLATFORMS
insert into Platforms (pname, pdevice)
values ('Steam', 'PC'),
('Micorsoft Store', 'PC/Cosole'),
('PS Store', 'Playstation'),
('Xbox Store', 'Xbox'),
('Google Playstore', 'Android Devices');

-- INSERT INTO MINREQ
insert into MinRequirements (mrtype, mrsize_gb)
values ('Low', 4),
('Medium', 8),
('High', 16);

select * from MinRequirements;

-- INSERT INTO SUPPORTED INPUTS
insert into SupportedInputs (siname)
values ('Keyboard and Mouse'),
('Touchscreen'),
('Controller');

-- INSERT INTO GRAPHICS
insert into Graphics (grname, grtype, grpov)
values ('Realistic', '3D', 'First Person'),
('Cartoony', '3D', 'Customizable'),
('Semi-Realistic', '3D', 'Third Person'),
('PixelArt', '2D', 'Third Person'),
('LowPoly', '3D', 'First Person');

select * from Graphics;

-- INSERT INTO CHARACTERS
insert into Characters (charname, charage, charrole)
values ('Simon "Ghost" Riley', 36, 'Main Character'),
('John "Soap" MacTavish', 27, 'Main Character'),
('Steve', 30, 'Protagonist'),
('Jack Cooper', 28, 'Protagonist'),
('BT7274', 12, 'Main Helper'),
('Marcus Fenix', 34, 'Main Character'),
('Sans', 100, 'Episodic Character'),
('Dominic Santiago', 32, 'Secondary Character'),
('John Doe', 23, 'Test Character'),
('Jamie Doe', 24, 'Test Character'),
('JD',34, null),
('Johnathan Kaval', 67, 'Main Character');
select * from Characters;

-- INSERT INTO AWARDS
insert into Awards (aname, ayear)
values ('Steam Awards', 2022),
('Steam Awards', 2025),
('Steam Awards', 2017),
('Microsoft Awards', 2023),
('Microsoft Awards', 2018),
('Steam Awards', 2004),
('Microsoft Awards', 2009);

-- INSERT INTO AWARD CATEORIES
insert into AwardCategories (acname, acvotes)
values ('Best Storyline', 3000),
('Best Graphics', 2500),
('Most Immersve Gameplay', 5000),
('Most Creative Fanbase', 1500);

-- Insert into Games
select * from Publishers;
select * from MinRequirements;
select * from Graphics;

insert into Games (gname, gyear, pubid, mrid, grid)
values ('Titanfall 2', 2018, 4, 2, 1),
('Call of Duty MWII', 2022, 6, 3, 1),
('Call of Duty MWIII', 2023, 6, 3, 1),
('Minecraft', 2008, 7, 1, 2),
('Gears of War 2', 2013, 7, 2, 3),
('Undertale', 2018, 3, 1, 4),
('Repo', 2024, 5, 1, 1),
('Deep Rock Galactic', 2020, 2, 2, 5),
('testGame', 2000, 1, 1, 1);

-- INSERT INTO GameGenres
select * from Games
select * from Genres

--1 VIOLATION
insert into GameGenres (gid, genid)
values (1, 1),
(1, 3),
(2, 1),
(3, 1),
(4, 2),
(5, 1),
(6, 3),
(7, 4),
(8, 1),
(8, 4),
--gid = 11 does not exist
(11,2);

-- INSERT INTO GamePlatforms
select * from Games
select * from Platforms

insert into GamePlatforms (gid, pid)
values (1, 1),
(2, 1),
(2, 2),
(2, 4),
(3, 1),
(3, 2),
(3, 3),
(4, 4),
(5, 4),
(5, 2),
(6, 1),
(7, 1),
(8, 1);

-- INSERT INTO GameCharacters
select * from Games
select * from Characters

insert into GameCharacters (gid, charid)
values (1, 4),
(1, 5),
(2, 1),
(2, 2),
(3, 1),
(3, 2),
(4, 3),
(5, 6),
(5, 8),
(6, 7);


-- INSERT INTO GameSupportedInputs
select * from Games
select * from SupportedInputs

insert into GameSupportedInputs (gid, siid)
values (1, 1),
(1, 3),
(2, 1),
(2, 3),
(3, 1),
(3, 3),
(4, 1),
(4, 2),
(4, 3),
(5, 3),
(6, 1),
(6, 3),
(7, 1),
(8, 1);

-- INSERT INTO GameAwards
select * from Games
select * from Awards
select * from AwardCategories

insert into GameAwards (gid, aid, acid)
values (1, 5, 1),
(1, 5, 2),
(2, 2, 1),
(6, 5, 3),
(4, 5, 4);

--UPDATE 1 - < AND LIKE
UPDATE Games
SET gyear=2025
WHERE gyear<2020 AND gname LIKE 'test%';

--UPDATE 2 - IS NULL
UPDATE Characters
SET charname='JD'
WHERE charrole IS NULL;

--UPDATE 3 - IN (...)
UPDATE Genres
SET gen_default_difficulty = 'Easy Peasy'
WHERE genname IN ('Relaxing', 'Open World');

--DELETE 1
DELETE FROM Characters
WHERE charname LIKE 'Jamie%';

--DELETE 2 - BETWEEN
DELETE FROM Awards
WHERE ayear BETWEEN 2000 AND 2010;



--select Games.gname, count(*) as NoOfCharacters from 
--Games inner join GameCharacters on Games.gid = GameCharacters.gid
--inner join Characters on GameCharacters.charid = Characters.charid
--group by Games.gname;
