# MySQL
Fundamental knowledge about MySQL.


# ✨ Getting Started

## Connect to your MySQL
1. Go to your MySQL folder
```
cd /usr/local/mysql/bin
```
2. After typing this, it will ask you to input your password
```
./mysql -u root -p
```

## Build database with command line
1. See what is in your database
  ``` SQL
  show databases;
  ```
2. Create your database
```
create database <databasename>;
```
3. Use your database
```
use <databasename>;
```


# 📖 Homeworks

## task 2 : create member table
Use create table <tablename> to create your table
```
CREATE TABLE member(
	id bigint AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL ,
  	username VARCHAR(255) NOT NULL,
	password VARCHAR(255) NOT NULL,
	follower_count int unsigned NOT NULL DEFAULT 0,
	time datetime NOT NULL DEFAULT current_timestamp(),
	PRIMARY KEY (id) 
);
```
You may check values in your table with
```
desc <tablename>
```
![task2](https://github.com/chelsey0527/wh0919/blob/develop/week-5/images/task2.png)
 
## task 3 : SQL CRUD
  
### 1. Insert datas into table
```
INSERT INTO member (name, username, password, follower_count, time)
VALUES ('mem1', 'test', 'test', 1, current_timestamp());
```
![task3-1](https://github.com/chelsey0527/wh0919/blob/develop/week-5/images/task3-1.png)

### 2. Get all values in table
```
SELECT * FROM member;
```
![task3-2](https://github.com/chelsey0527/wh0919/blob/develop/week-5/images/task3-2.png)

### 3. Get all values order by time descending
```
SELECT * FROM member ORDER BY time DESC;
```
![task3-3](https://github.com/chelsey0527/wh0919/blob/develop/week-5/images/task3-3.png)
  
### 4. Get values in intervals
```
SELECT * FROM member WHERE id>1 AND id<5 ORDER BY time DESC;
```
![task3-4](https://github.com/chelsey0527/wh0919/blob/develop/week-5/images/task3-4.png)

### 5. Get values with username
```
SELECT * FROM member WHERE username = "test";
```
![task3-5](https://github.com/chelsey0527/wh0919/blob/develop/week-5/images/task3-5.png)
                                         
### 6. Get values with username and password
```
SELECT * FROM member WHERE username = "test" AND password = "test";
```
![task3-6](https://github.com/chelsey0527/wh0919/blob/develop/week-5/images/task3-6.png)

### 7. Update name
```                                         
UPDATE member
SET name = "test2"
WHERE username = "test";
```
![task3-7](https://github.com/chelsey0527/wh0919/blob/develop/week-5/images/task3-7.png)

                                         
## task 4 : SQL Aggregate Functions
                                         
### 1. Count total members
```
SELECT COUNT(id) FROM member;
```
![task4-1](https://github.com/chelsey0527/wh0919/blob/develop/week-5/images/task4-1.png)
                                         
### 2. Total follower_count number
```
SELECT SUM(follower_count) FROM member;
``` 
![task4-2](https://github.com/chelsey0527/wh0919/blob/develop/week-5/images/task4-2.png) 
### 3. Average follower_count
```
SELECT AVG(follower_count) FROM member;
```
![task4-3](https://github.com/chelsey0527/wh0919/blob/develop/week-5/images/task4-3.png)

## task 5 : SQL JOIN
Create message table
```
CREATE TABLE message(
	id bigint AUTO_INCREMENT,
	member_id bigint NOT NULL,
	content varchar(255) NOT NULL,
	like_count int unsigned NOT NULL DEFAULT 0,
	time datetime NOT NULL DEFAULT current_timestamp(),
	PRIMARY KEY (id),
	FOREIGN KEY (member_id) REFERENCES member(id)
);
```    
                                         
### 1. Get all messages with member name
```
SELECT message.content, member.name
FROM message
INNER JOIN member ON member.id = message.member_id;
```
![task5-1](https://github.com/chelsey0527/wh0919/blob/develop/week-5/images/task5-1.png)
                                         
### 2. Get all messages posted by username="test"
```
SELECT member.username, message.content
FROM member
INNER JOIN message ON member.id = message.member_id WHERE member.username="test";
```
![task5-2](https://github.com/chelsey0527/wh0919/blob/develop/week-5/images/task5-2.png)

                                         
### 3. Get username="test"'s average like_count 
```
SELECT AVG(message.like_count)
FROM member
INNER JOIN message ON member.id = message.member_id WHERE member.username="test";
```
![task5-1](https://github.com/chelsey0527/wh0919/blob/develop/week-5/images/task5-3.png)

# Backup your database
Using mysqldump
```
/usr/local/mysql/bin/mysqldump -u [user name (or root)] -p[password] [DB name] > [filename].sql
```
