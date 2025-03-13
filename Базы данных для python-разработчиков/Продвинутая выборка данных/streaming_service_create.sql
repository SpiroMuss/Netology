CREATE SCHEMA IF NOT EXISTS streaming_service;

CREATE TABLE IF NOT EXISTS streaming_service.genre(
	"id" SERIAL PRIMARY KEY,
	"name" VARCHAR(60) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS streaming_service.musician(
	"id" SERIAL PRIMARY KEY,
	"name" VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS streaming_service.album(
	"id" SERIAL PRIMARY KEY,
	"name" VARCHAR(60) NOT NULL,
	"date" DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS streaming_service.compilation(
	"id" SERIAL PRIMARY KEY,
	"name" VARCHAR(60) NOT NULL,
	"date" DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS streaming_service.song(
	"id" SERIAL PRIMARY KEY,
	"name" VARCHAR(60) NOT NULL,
	"seconds" INT NOT NULL,
	"album_id" BIGINT NOT NULL REFERENCES streaming_service.album("id")
);

CREATE TABLE IF NOT EXISTS streaming_service.song_compilation(
	"id" SERIAL PRIMARY KEY,
	"song_id" BIGINT NOT NULL REFERENCES streaming_service.song("id"),
	"compilation_id" BIGINT NOT NULL REFERENCES streaming_service.compilation("id")
);

CREATE TABLE IF NOT EXISTS streaming_service.album_musician(
	"id" SERIAL PRIMARY KEY,
	"album_id" BIGINT NOT NULL REFERENCES streaming_service.album("id"),
	"musician_id" BIGINT NOT NULL REFERENCES streaming_service.musician("id")
);

CREATE TABLE IF NOT EXISTS streaming_service.genre_musician(
	"id" SERIAL PRIMARY KEY,
	"genre_id" INT NOT NULL REFERENCES streaming_service.genre("id"),
	"musician_id" BIGINT NOT NULL REFERENCES streaming_service.musician("id")
);