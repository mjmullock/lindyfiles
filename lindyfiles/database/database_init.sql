BEGIN TRANSACTION;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    username    VARCHAR(100),
    password    VARCHAR(100),
    fname       VARCHAR(100),
    email       VARCHAR(200),
    picture     VARCHAR(100),
    leader      BOOLEAN,
    follower    BOOLEAN,
    sessid      VARCHAR(100),
    PRIMARY KEY (email)
);

DROP TABLE IF EXISTS pros;
CREATE TABLE pros (
    fname       VARCHAR(100),
    lname       VARCHAR(100),
    picture     VARCHAR(100),
    leader      BOOLEAN,
    follower    BOOLEAN,
    teacher     BOOLEAN,
    website     VARCHAR(100),
    organization VARCHAR(100),
    organization_website     VARCHAR(100),
    PRIMARY KEY (fname, lname)
);

.separator ,
.import ./Pro_Dancers.csv pros

DROP TABLE IF EXISTS events;
CREATE TABLE events (
    id			INTEGER PRIMARY KEY,
    name    	        VARCHAR(100) NOT NULL,
    start_date		DATE,
    end_date		DATE,
    social_dance	BOOLEAN,
    workshop		BOOLEAN,
    competition		BOOLEAN,
    starting_price	SMALLMONEY,
    city		VARCHAR(100),
    state		VARCHAR(100),
    host		VARCHAR(100),
    website		VARCHAR(100),
    UNIQUE (name, start_date) 
);     

DROP TABLE IF EXISTS tmpevents;
CREATE TABLE tmpevents (
    name    	        VARCHAR(100) NOT NULL,
    start_date		DATE,
    end_date		DATE,
    social_dance	BOOLEAN,
    workshop		BOOLEAN,
    competition		BOOLEAN,
    starting_price	SMALLMONEY,
    city		VARCHAR(100),
    state		VARCHAR(100),
    host		VARCHAR(100),
    website		VARCHAR(100),
    PRIMARY KEY (name, start_date) 
);     

.separator ,
.import ./Swing_Dance_Events.csv tmpevents

INSERT INTO events(name, start_date, end_date, social_dance, workshop, competition, starting_price, city, state, host, website)
SELECT * FROM tmpevents; 

DROP TABLE IF EXISTS tmpevents;
END TRANSACTION;
