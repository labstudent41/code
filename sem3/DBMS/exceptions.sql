CREATE TABLE product (pname VARCHAR(20), pprice NUMBER(9));

INSERT INTO product VALUES ('Titan Watch', 10000);
INSERT INTO product VALUES ('Redmi Note 10', 12000);
INSERT INTO product VALUES ('Bike light', 20000);

DECLARE
	name VARCHAR(20);
	price NUMBER;
BEGIN
	SELECT pname, pprice INTO name, price
		FROM product WHERE pprice < 5000;
	DBMS_OUTPUT.PUT_LINE(price);
	EXCEPTION
		WHEN NO_DATA_FOUND THEN
			DBMS_OUTPUT.PUT_LINE('No prduct has unit price less than 5000');
END;
/


CREATE TABLE info (fname VARCHAR(20), lname VARCHAR(20));

INSERT INTO info VALUES ('Vikas', 'Kushwaha');
INSERT INTO info VALUES ('Vedant', 'Bhadkamkar');
INSERT INTO info VALUES ('Sneha', 'Bhadkamkar');
INSERT INTO info VALUES ('Sneha', 'Patil');

DECLARE
	l_name VARCHAR(20);
BEGIN
	SELECT lname INTO l_name FROM info WHERE fname='Sneha';
	DBMS_OUTPUT.PUT_LINE(l_name);
	EXCEPTION WHEN TOO_MANY_ROWS THEN
		DBMS_OUTPUT.PUT_LINE('Multiple rows retrived');
END;
/
