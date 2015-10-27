use hw2db;

drop table if exists connectedPlayers;
drop table if exists players;

create table players(
	username varchar(30),
	password text,
	model text,
	pos text,
	isMoving boolean,

	PRIMARY KEY (username)

);

create table connectedPlayers(
	id integer PRIMARY KEY,
	username varchar(30),
    
    FOREIGN KEY (username) REFERENCES players(username)
);

insert into players VALUES ('Vicken','1234','ralph','0,0,0,0',False);
insert into players VALUES ('Genus','1234','panda','3.0,3.0,0,0',False);
insert into players VALUES ('Maxime','1234','car','5.0,5.0,0,0',False);
insert into players VALUES ('Charles','1234','car','7.0,7.0,0,0',False);

DROP USER if exists'cs454user'@'localhost';
CREATE USER 'cs454user'@'localhost' IDENTIFIED BY 'cs454pwd';
GRANT ALL PRIVILEGES ON hw2db.* TO 'cs454user'@'localhost';
FLUSH PRIVILEGES;
