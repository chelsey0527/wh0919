----- HW2 -----
CREATE TABLE member(
	id bigint AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL ,
  	username VARCHAR(255) NOT NULL,
	password VARCHAR(255) NOT NULL,
	follower_count int unsigned NOT NULL DEFAULT 0,
	time datetime NOT NULL DEFAULT current_timestamp(),
	PRIMARY KEY (id) 
)
;
