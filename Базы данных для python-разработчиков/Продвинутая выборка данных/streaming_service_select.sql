--2.1
SELECT "name", "seconds"
FROM streaming_service.song
ORDER BY seconds DESC LIMIT 1;

--2.2
SELECT "name"
FROM streaming_service.song
WHERE "seconds" > 209;

--2.3
SELECT "name"
FROM streaming_service.compilation
WHERE "date" >= '01-01-2018' AND "date" < '01-01-2021';

--2.4
SELECT "name"
FROM streaming_service.musician
WHERE "name" NOT LIKE '% %';

--2.5
SELECT "name"
FROM streaming_service.song
WHERE UPPER("name") LIKE '%MY%' 
	OR UPPER("name") LIKE '%МОЙ%';

--3.1
SELECT g.name AS genre, COUNT(gm.musician_id) AS musician_count
FROM streaming_service.genre_musician gm
JOIN streaming_service.genre g ON gm.genre_id = g.id
GROUP BY g.name ORDER BY g.name;

--3.2
SELECT COUNT(DISTINCT song_id)
FROM streaming_service.song_compilation sc
JOIN streaming_service.compilation c ON sc.compilation_id = c.id
WHERE c.date < '01-01-2021' AND c.date >= '01-01-2019';

--3.3
SELECT a.name, AVG(s.seconds)
FROM streaming_service.song s
JOIN streaming_service.album a ON s.album_id = a.id
GROUP BY a.name;

--3.4
SELECT m.name
FROM streaming_service.musician m
WHERE NOT EXISTS (
	SELECT 1
	FROM streaming_service.album ss_album
	JOIN streaming_service.album_musician am ON ss_album.id = am.album_id
	WHERE m.id = am.musician_id
		AND ss_album.date BETWEEN '2020-01-01' AND '2020-12-31'
);

--3.5
SELECT DISTINCT c.name
FROM streaming_service.compilation c
JOIN streaming_service.song_compilation sc ON c.id = sc.compilation_id
JOIN streaming_service.song s ON s.id = sc.song_id
JOIN streaming_service.album a ON s.album_id = a.id
JOIN streaming_service.album_musician am ON a.id = am.album_id
JOIN streaming_service.musician m ON am.musician_id = m.id
WHERE m.id = 1;

--4.1
SELECT a.name
FROM streaming_service.album a
JOIN streaming_service.album_musician am ON a.id = am.album_id
GROUP BY a.name
HAVING COUNT(am.musician_id) > 1;

--4.2
SELECT s.name
FROM streaming_service.song s
LEFT JOIN streaming_service.song_compilation sc ON s.id = sc.song_id
WHERE sc.song_id IS NULL;

--4.3
WITH MinDuration AS (
    SELECT MIN(s.seconds) AS min_seconds
    FROM streaming_service.song s
)
SELECT DISTINCT m.name
FROM streaming_service.song s
JOIN streaming_service.album_musician am ON s.album_id = am.album_id
JOIN streaming_service.musician m ON am.musician_id = m.id
JOIN MinDuration md ON s.seconds = md.min_seconds;

--4.4
WITH sc AS (
    SELECT a.id, COUNT(s.id) AS song_count
    FROM streaming_service.album a
    JOIN streaming_service.song s ON a.id = s.album_id
    GROUP BY a.id
),
msc AS (
    SELECT MIN(song_count) AS min_song_count
    FROM sc
)
SELECT DISTINCT a.name
FROM streaming_service.album a
JOIN sc ON a.id = sc.id
JOIN msc ON sc.song_count = msc.min_song_count;