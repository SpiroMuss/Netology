INSERT INTO streaming_service.genre VALUES
(DEFAULT, 'Metal'),
(DEFAULT, 'Rock'),
(DEFAULT, 'Pop'),
(DEFAULT, 'Hip-Hop'),
(DEFAULT, 'Rap');

INSERT INTO streaming_service.musician VALUES
(DEFAULT, 'Metallica'),
(DEFAULT, 'Ghost'),
(DEFAULT, 'Post Malone'),
(DEFAULT, 'Swae Lee');

INSERT INTO streaming_service.album VALUES
(DEFAULT, 'Death Magnetic', '01-01-2008'),
(DEFAULT, 'Seven Inches of Satanic Panic', '09-13-2019'),
(DEFAULT, E'Hollywood\'s Bleeding', '09-06-2019'),
(DEFAULT, 'Death Magnetic 2', '01-01-2020');

INSERT INTO streaming_service.compilation VALUES
(DEFAULT, 'Compilation-1', '10-01-2019'),
(DEFAULT, 'Compilation-2', '11-05-2020'),
(DEFAULT, 'Compilation-3', '03-12-2023'),
(DEFAULT, 'Compilation-4', '02-06-2017');

INSERT INTO streaming_service.song VALUES
(DEFAULT, 'My Apocalypse', 301, 1),
(DEFAULT, 'The End Of The Line', 472, 1),
(DEFAULT, 'Mary On A Cross', 245, 2),
(DEFAULT, 'Allergic', 156, 3),
(DEFAULT, 'Sunflower - Spider-Man: Into the Spider-Verse', 157, 3),
(DEFAULT, 'Wow.', 149, 3);

INSERT INTO streaming_service.song_compilation VALUES
(DEFAULT, 3, 1),
(DEFAULT, 4, 1),
(DEFAULT, 5, 1),
(DEFAULT, 1, 2),
(DEFAULT, 2, 2),
(DEFAULT, 3, 2),
(DEFAULT, 2, 3),
(DEFAULT, 3, 3),
(DEFAULT, 4, 3),
(DEFAULT, 1, 4),
(DEFAULT, 2, 4);

INSERT INTO streaming_service.album_musician VALUES
(DEFAULT, 1, 1),
(DEFAULT, 2, 2),
(DEFAULT, 3, 3),
(DEFAULT, 3, 4),
(DEFAULT, 4, 1);

INSERT INTO streaming_service.genre_musician VALUES
(DEFAULT, 1, 1),
(DEFAULT, 2, 1),
(DEFAULT, 2, 2),
(DEFAULT, 3, 3),
(DEFAULT, 4, 3),
(DEFAULT, 5, 3),
(DEFAULT, 5, 4);