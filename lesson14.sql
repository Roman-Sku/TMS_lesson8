create database if not exists lesson14;
use lesson14;
show tables;
create table seller (
id int unsigned primary key auto_increment,
company varchar(64) not null,
phone varchar(64) not null
);

create table products (
id int unsigned primary key auto_increment,
name varchar(64) not null,
cost int unsigned not null,
count int unsigned default 0 not null,
seller_id int unsigned not null,
foreign key (seller_id) references seller (id)
);

create table users (
id int unsigned primary key auto_increment,
username varchar(64) primary key not null,
password varchar(64) not null,
email varchar(64) not null
);

create table orders (
id int unsigned primary key auto_increment,
count int unsigned default 0 not null,
user_id int unsigned not null,
product_id int unsigned not null,
foreign key (user_id) references users (id),
foreign key (product_id) references products (id)
);
