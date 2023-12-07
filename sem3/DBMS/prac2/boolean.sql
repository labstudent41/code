DECLARE

a BOOLEAN := true;
b BOOLEAN := false;

BEGIN

IF a AND b THEN
	dbms_output.put_line('True');
ELSE
	dbms_output.put_line('False');
END IF;

IF a OR b THEN
	dbms_output.put_line('True');
ELSE
	dbms_output.put_line('False');
END IF;

IF NOT a THEN
	dbms_output.put_line('True');
ELSE
	dbms_output.put_line('False');
END IF;

END;
/