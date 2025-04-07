CREATE SCHEMA IF NOT EXISTS users;

CREATE TABLE IF NOT EXISTS users.user(
	"id" serial PRIMARY KEY,
	"name" varchar(60) NOT NULL,
	"surname" varchar(60) NOT NULL,
	"email" varchar(60) NOT NULL,
	CHECK ("email" LIKE '%@%.%')
);

CREATE TABLE IF NOT EXISTS users.phone(
	"id" serial PRIMARY KEY,
	"user_id" bigint NOT NULL REFERENCES users.user("id"),
	"phone_number" smallint,
	CHECK ("phone_number" <= 15)
);