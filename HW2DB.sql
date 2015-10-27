use hw2db;


drop table if exists players;

create table players(
	name varchar(30),
	password varchar(20),
	character varchar(30),
	posX DECIMAL(4,4),
	posY DECIMAL(4,4),
	posZ DECIMAL(4,4),
	posH DECIMAL(4,4), 
	isMoving boolean,


	PRIMARY KEY (name)


);

insert into players VALUES ('Vicken','1234','ralph',0,0,0,0,0,0);
insert into players VALUES ('Genus','1234','panda',3,3,0,0,0,0);
insert into players VALUES ('Maxime','1234','car',5,5,0,0,0,0);
insert into players VALUES ('Charles','1234','car',7,7,0,0,0,0);
