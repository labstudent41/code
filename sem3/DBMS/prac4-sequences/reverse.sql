CREATE OR REPLACE FUNCTION reverse(num NUMBER)
	RETURN NUMBER IS rev NUMBER := 0 ; n NUMBER := 0;
BEGIN
	DBMS_OUTPUT.PUT_LINE(num);
	-- WHILE num > 0 LOOP
		-- n := mod(num, 10);
		-- num := floor(num / 10);
		-- rev := (rev * 10) + n;
		-- DBMS_OUTPUT.PUT_LINE(num || ' ' || n || ' ' || rev);
	-- END LOOP;
	DBMS_OUTPUT.PUT_LINE(rev);
	RETURN rev;
END;
/

DECLARE
	num NUMBER := 45;
	rev NUMBER := 0;
	n NUMBER := 0;
BEGIN
	n := reverse(num);
	DBMS_OUTPUT.PUT_LINE(n);
END;
/

-- DECLARE
	-- num NUMBER := 45;
	-- rev NUMBER := 0;
	-- n NUMBER := 0;
-- BEGIN
	-- DBMS_OUTPUT.PUT_LINE(num);
	-- WHILE num > 0 LOOP
		-- n := mod(num, 10);
		-- num := floor(num / 10);
		-- rev := (rev * 10) + n;
		-- DBMS_OUTPUT.PUT_LINE(num || ' ' || n || ' ' || rev);
	-- END LOOP;
	-- DBMS_OUTPUT.PUT_LINE(rev);
-- END;
-- /
