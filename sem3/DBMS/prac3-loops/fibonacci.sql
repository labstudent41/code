DECLARE
	fterm NUMBER := 0;
	sterm NUMBER := 1;
	nterm NUMBER := 1;
	n NUMBER;
BEGIN
	dbms_output.put_line(fterm || chr(10) || sterm);
	n := &n;
	WHILE nterm <= n LOOP
		nterm := fterm + sterm;
		dbms_output.put_line(nterm);
		fterm := sterm;
		sterm := nterm;
	END LOOP;
END;
/