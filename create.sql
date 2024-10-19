DROP SCHEMA IF EXISTS ccca CASCADE;

CREATE SCHEMA ccca;

CREATE TABLE ccca.account (
	account_id UUID PRIMARY KEY,
	name TEXT NOT NULL,
	email TEXT NOT NULL,
	cpf TEXT NOT NULL,
	car_plate TEXT NULL,
	is_passenger BOOLEAN NOT NULL DEFAULT false,
	is_driver BOOLEAN NOT NULL DEFAULT false,
	password TEXT NOT NULL
);


CREATE TABLE ccca.ride (
	ride_id UUID,
	passenger_id UUID,
	driver_id UUID,
	status TEXT,
	distance NUMERIC,
	from_lat NUMERIC,
	from_long NUMERIC,
	to_lat NUMERIC,
	to_long NUMERIC,
	date TIMESTAMP,
	fare NUMERIC
);


CREATE TABLE ccca.position (
	position_id UUID,
	ride_id UUID,
	lat NUMERIC,
	long NUMERIC,
	date TIMESTAMP
);