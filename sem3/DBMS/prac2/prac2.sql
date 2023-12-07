DECLARE

marks number;

BEGIN

marks := &marks;

IF marks >= 90 THEN
	dbms_output.put_line('O grade');
ELSIF marks >= 80 THEN
	dbms_output.put_line('A grade');
ELSIF marks >= 70 THEN
	dbms_output.put_line('B grade');
ELSIF marks >= 60 THEN
	dbms_output.put_line('C grade');
ELSIF marks >= 50 THEN
	dbms_output.put_line('D grade');
ELSIF marks >= 40 THEN
	dbms_output.put_line('E grade');
ELSE
	dbms_output.put_line('Fail');
END IF;

END;
/