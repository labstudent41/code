DECLARE

a NUMBER(3) := 100;
b NUMBER(3) := 200;

BEGIN


IF (a = 100) THEN
	IF (b = 200) THEN
		dbms_output.put_line('Value of a is 100 and b is 200');
	END IF;
END IF;

dbms_output.put_line('Exact value of a is : ' || a);
dbms_output.put_line('Exact value of b is : ' || b);

END;
/
