-- create table unique_id

CREATE TABLE if not EXISTS(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
