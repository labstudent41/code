DECLARE
a number;
b number;
op varchar2(20);
opo number;
BEGIN

a := &a;
b := &b;
op := '&op';

CASE op
	WHEN 'Sum' THEN
		opo := a+b;
	WHEN 'Diff' THEN
		opo := a-b;
	WHEN 'Product' THEN
		opo := a*b;
	WHEN 'Div' THEN
		opo := a/b;
	ELSE
		opo := 'Invalid Operand';
END CASE;

DBMS_OUTPUT.PUT_LINE(opo);

END;
/