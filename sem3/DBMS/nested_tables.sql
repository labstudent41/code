CREATE TYPE location AS OBJECT (city VARCHAR(20), pin NUMBER(6));
/

CREATE TYPE nest_table AS TABLE OF location;
/

CREATE TABLE student (no NUMBER(3), name VARCHAR2(10), address nest_table)
	NESTED TABLE address STORE AS student_temp;


INSERT INTO student VALUES (1, 'Avi', nest_table(location('Hyd', 400010)));
INSERT INTO student VALUES (2, 'Vikas', nest_table(location('Mah', 401208)));

SELECT * FROM student;

SELECT no, name, s.city, s.pin FROM student s1, TABLE(s1.address) s;
