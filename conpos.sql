create database conpos;
use conpos;

create table product(
	pno int not null primary key,
    pname varchar(20) not null,
    pprice int not null
);

create table inventory(
	ino int not null primary key,
    pno int not null,
    foreign key(pno) references product(pno),
    Pcount int not null,
    enter_date datetime not null default now()
);

create table sale(
	sno int not null primary key,
    eno int not null,
    sdate datetime not null default now(),
    total_price int not null
);

create table sale_detail(
	sno int not null,
    pno int not null,
    scount int not null,
    sum_price int not null,
    primary key(sno,pno),
    foreign key(sno) references sale(sno) on delete cascade on update cascade,
    foreign key(pno) references product(pno)
);

create table employee(
	eno int not null primary key,
    ename varchar(20) not null,
    etel varchar(14) not null,
    econdition boolean not null
);

create table commute(
	cno int not null primary key,
    eno int not null,
    foreign key(eno) references employee(eno) on delete cascade on update cascade,
    atten_time datetime not null,
    leave_time datetime not null
);

select * from product;
select * from inventory;
select * from sale;
select * from sale_detail;
select * from commute;
select * from employee;

create user 'conceo'@'%' identified by 'conceo15';

grant all privileges on conpos.* to 'conceo'@'%';