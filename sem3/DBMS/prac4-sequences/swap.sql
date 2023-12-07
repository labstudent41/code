
CREATE OR REPLACE PROCEDURE swap(
	a IN OUT NUMBER,
	b IN OUT NUMBER) IS	c NUMBER;
BEGIN
	c := a;
	a := b;
	b := c;
END;

DECLARE
	a NUMBER := 5;
	b NUMBER := 10;
	c NUMBER;
BEGIN
	DBMS_OUTPUT.PUT_LINE('Values before swap');
	DBMS_OUTPUT.PUT_LINE(a || ' ' || b);
	swap(a, b);
	
	DBMS_OUTPUT.PUT_LINE('Values after swap');
	DBMS_OUTPUT.PUT_LINE(a || ' ' || b);
END;
/