use hw2db;



drop table if exists connectedPlayers;

drop table if exists players;



create table players(
	
	username varchar(30),
	
	password text,
	
	pos text,
	
	isMoving boolean,

	
	PRIMARY KEY (username)

);




create table connectedPlayers(
	
	id integer PRIMARY KEY,
	
	username varchar(30),
    
	model text,
    
    
	FOREIGN KEY (username) REFERENCES players(username)
);




insert into players VALUES ('Vicken','1234','0,0,0,0',False);

insert into players VALUES ('Genus','1234','3.0,3.0,0,0',False);

insert into players VALUES ('Maxime','1234','5.0,5.0,0,0',False);

insert into players VALUES ('Charles','1234','7.0,7.0,0,0',False);




insert into connectedPlayers VALUES ('1','Genus','Ralph');

DROP USER if exists'cs454user'@'localhost';
CREATE USER 'cs454user'@'localhost' IDENTIFIED BY 'cs454pwd';
GRANT ALL PRIVILEGES ON hw2db.* TO 'cs454user'@'localhost';
FLUSH PRIVILEGES;
