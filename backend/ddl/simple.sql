create table forum_user(
    uid serial not null primary key,
    uname varchar(50),
    email varchar(30),
    gender char(1),
    password varchar(50) not null,
    signature varchar(100)
);

create table tag (
    tname char(20) primary key,
    hot_value int
);