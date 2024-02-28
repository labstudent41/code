CREATE OR REPLACE PROCEDURE findmin(
	x IN NUMBER,
	y IN NUMBER,
	z OUT NUMBER) IS
BEGIN
	IF x < y THEN
		z := x;
	ELSE
		z := y;
	END IF;
END;

DECLARE
a NUMBER;
b NUMBER;
c NUMBER;

BEGIN
	a := 23;
	b := 25;
	findmin(a, b, c);
	DBMS_OUTPUT.PUT_LINE('Min value : ' || c);
END;
/