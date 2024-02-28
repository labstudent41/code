set serveroutput on

CREATE TABLE employ (e_id NUMBER(3), e_salary NUMBER(10));

INSERT INTO employ VALUES(1, 5000);
INSERT INTO employ VALUES(2, 10000);
INSERT INTO employ VALUES(3, 15000);
INSERT INTO employ VALUES(4, 20000);
INSERT INTO employ VALUES(5, 25000);

SELECT * FROM employ;

CREATE OR REPLACE TRIGGER trigemp
	AFTER UPDATE
	ON employ
	FOR EACH ROW
DECLARE
	sal_diff NUMBER;
BEGIN
	sal_diff := :NEW.e_salary - :OLD.e_salary;
	DBMS_OUTPUT.PUT_LINE('Old salary : ' || :OLD.e_salary);
	DBMS_OUTPUT.PUT_LINE('New salary : ' || :NEW.e_salary);
	DBMS_OUTPUT.PUT_LINE('Salary difference : ' || sal_diff);
END;
/

CREATE OR REPLACE TRIGGER trigemp
	AFTER UPDATE
	ON employ
	FOR EACH ROW
DECLARE
	c NUMBER;
BEGIN
	c := :NEW.e_salary * 0.10;
	UPDATE employ set e_commission=c;
END;
/