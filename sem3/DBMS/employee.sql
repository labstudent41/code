CREATE TABLE employee (fname VARCHAR(20), lname VARCHAR(20),
						e_info VARCHAR(20));
						
INSERT INTO employee VALUES ('Utkarsh', 'Sharma', 'Accountant');
INSERT INTO employee VALUES ('Azan', 'Shaikh', 'Sweeper');
INSERT INTO employee VALUES ('Russel', 'Martins', 'Manager');
INSERT INTO employee VALUES ('Laxman', 'Naik', 'Guard');
INSERT INTO employee VALUES ('Sahil', 'Pawar', 'Guard');
						
CREATE OR REPLACE PROCEDURE add_emp (
    fname VARCHAR, lname VARCHAR, e_info VARCHAR
    ) IS
BEGIN
	INSERT INTO employee VALUES (fname, lname, e_info);
END fstring;
/

CREATE OR REPLACE FUNCTION fstring () RETURN VARCHAR IS
BEGIN
	RETURN 'HELLO WORLD';
END fstring;
/