#DROP DATABASE gans_local;
CREATE DATABASE gans_aws_JH;

USE gans_aws_JH;

DROP TABLE cities;
CREATE TABLE IF NOT EXISTS cities (
	city_id INT AUTO_INCREMENT,
    city_name VARCHAR(50),
    latitude FLOAT,
    longitude FLOAT,
    population INT,
    country VARCHAR(50),
    PRIMARY KEY (city_id)
);

DROP TABLE airports;

CREATE TABLE IF NOT EXISTS airports(
	city_id INT NOT NULL,
    icao_id VARCHAR(50),
    airport_name VARCHAR(50),
    airport_short_name VARCHAR(50),
    PRIMARY KEY (icao_id),
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);

DROP TABLE flights;
CREATE TABLE IF NOT EXISTS flights(
   flight_id INT AUTO_INCREMENT,
   icao_id VARCHAR(50) NOT NULL,
   arrival_terminal INT,
   arrival_local_time DATETIME,
   arrival_from_where VARCHAR(50),
   flight_number VARCHAR(50),
   flight_status VARCHAR(50),
   airplane_model VARCHAR(50),
   airline_name VARCHAR(50),
   depart_icao VARCHAR(50),
   city_id INT,
    PRIMARY KEY (flight_id),
    FOREIGN KEY (icao_id) REFERENCES airports(icao_id)
);
SELECT * FROM flights;

DROP TABLE weather;

CREATE TABLE IF NOT EXISTS weather(
	weather_id INT AUTO_INCREMENT,
    city_id INT NOT NULL,
    `time` DATETIME,
    current_temp FLOAT,
    forecast_temp VARCHAR(40),
    feels_like FLOAT,
    humidity_level INT,
    PRIMARY KEY (weather_id),
    FOREIGN KEY (city_id) REFERENCES cities(city_id),
    FOREIGN KEY (city_id) REFERENCES airports(city_id)
);
ALTER TABLE weather
ADD CONSTRAINT fk_city_id
FOREIGN KEY (city_id) REFERENCES cities(city_id);

SELECT * FROM weather;
SELECT * FROM airports;
SELECT * FROM cities;
SELECT * FROM flights;


