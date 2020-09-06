

CREATE TABLE People_I_Know ( PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
		);


CREATE TABLE department(
     ID varchar(4),
     Dept varchar(4),
     RoomNum varchar(3)
 );


 INSERT INTO department VALUES ("OBC","CP","104" );
 INSERT INTO department VALUES ("JJ","CSI","102" );


select * from department;
