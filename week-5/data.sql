---------- HW2 ----------
CREATE TABLE member(
	id bigint AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL ,
  	username VARCHAR(255) NOT NULL,
	password VARCHAR(255) NOT NULL,
	follower_count int unsigned NOT NULL DEFAULT 0,
	time datetime NOT NULL DEFAULT current_timestamp(),
	PRIMARY KEY (id) 
);


---------- HW3 ----------
--- 1 ---
INSERT INTO member (name, username, password, follower_count, time)
VALUES ('mem1', 'test', 'test', 1, current_timestamp());
--- 2 ---
SELECT * FROM member;
--- 3 ---
SELECT * FROM member ORDER BY time DESC;
--- 4 ---
SELECT * FROM member WHERE id>1 AND id<5 ORDER BY time DESC;
--- 5 ---
SELECT * FROM member WHERE username = "test";
--- 6 ---
SELECT * FROM member WHERE username = "test" AND password = "test";
--- 7 ---
UPDATE member
SET name = "test2"
WHERE username = "test";


---------- HW4 ----------
--- 1 ---
SELECT COUNT(id) FROM member;
--- 2 ---
SELECT SUM(follower_count) FROM member;
--- 3 ---
SELECT AVG(follower_count) FROM member;






