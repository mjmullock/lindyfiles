DROP TABLE IF EXISTS cities;
CREATE TABLE cities (
	locId	INTEGER,
	country CHAR(2),
	region VARCHAR(50),
	city VARCHAR(200),
	postalCode CHAR(5),
	latitude REAL,
	longitude REAL,
	metroCode INTEGER,
	areaCode INTEGER
);

.separator ,
.import cities.csv cities

