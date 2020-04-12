--1.创建kaikeba库
create database if not exists kaikeba;

--2.使用kaikeba库
use kaikeba;

--3.创建user_info表
create table if not exists user_info (
user_id  string,
user_name  string, 
sex  string,
age  int,
city  string,
firstactivetime  string,
level  int,
extra1  string,
extra2  map<string,string>)
row format delimited fields terminated by '\t'
collection items terminated by ','
map keys terminated by ':'
lines terminated by '\n'
stored as textfile;

--4.创建user_trade表
create table if not exists user_trade (
user_name  string,
piece  int,
price  double,
pay_amount  double,
goods_category  string,
pay_time  bigint)  
partitioned by (
dt string)
row format delimited fields terminated by '\t';

--5.创建trade_2017表
create table if not exists trade_2017 (
user_name string, 
amount double, 
trade_time string)
row format delimited fields terminated by '\t';

--6.创建trade_2018表
create table if not exists trade_2018 (
user_name string, 
amount double, 
trade_time string)
row format delimited fields terminated by '\t';

--7.创建trade_2019表
create table if not exists trade_2019 (
user_name string, 
amount double, 
trade_time string)
row format delimited fields terminated by '\t';

--8.创建user_list_1表
create table if not exists user_list_1(
user_id string, 
user_name string)
row format delimited fields terminated by '\t'
collection items terminated by ','
map keys terminated by ':';

--9.创建user_list_2表
create table if not exists user_list_2(
user_id string, 
user_name string)
row format delimited fields terminated by '\t'
collection items terminated by ','
map keys terminated by ':';

--10.创建user_list_3表
create table if not exists user_list_2(
user_id string, 
user_name string)
row format delimited fields terminated by '\t'
collection items terminated by ','
map keys terminated by ':';

--11.创建user_fefund表
create table if not exists user_refund(
user_name string, 
refund_piece int, 
refund_amount double, 
refund_time string)
partitioned by ( 
dt string)
row format delimited fields terminated by '\t';

--12.创建user_trade_bak表
create table user_trade_bak(
user_name string, 
piece int, 
price double, 
pay_amount double, 
goods_category string, 
pay_time timestamp)
partitioned by( 
dt string)
row format delimited fields terminated by '\t';

--13.创建user_goods_category表
create table user_goods_category(
user_name string, 
category_detail string)
row format delimited fields terminated by '\t';