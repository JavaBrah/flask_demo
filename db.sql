-- DROP TABLE students;
-- CREATE TABLE students (
--     id SERIAL PRIMARY KEY,
--     first_name VARCHAR(50) NOT NULL,
--     last_name VARCHAR(50) NOT NULL,
--     age INT CHECK (age > 0) NOT NULL,
--     grade CHAR(1) NOT NULL
-- );

-- CREATE TABLE staff (
--     id SERIAL PRIMARY KEY,
--     first_name VARCHAR(20) NOT NULL,
--     last_name VARCHAR(20) NOT NULL,
--     age INT NOT NULL,
--     year_employed INT NOT NULL
-- -- );

-- INSERT INTO staff (
--     first_name, last_name, age, year_employed) VALUES
--     ('johnny', 'moe', 15, 2020);

DELETE FROM students
WHERE id > 10;

SELECT * FROM students;