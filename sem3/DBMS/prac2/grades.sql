DECLARE
c_grade char(1);
c_rank varchar2(20);

BEGIN
c_grade := '&c_grade';

CASE c_grade
	WHEN 'A' THEN
		c_rank := 'Excellent';
	WHEN 'B' THEN
		c_rank := 'Very Good';
	WHEN 'C' THEN
		c_rank := 'Good';
	WHEN 'D' THEN
		c_rank := 'Fair';
	WHEN 'F' THEN
		c_rank := 'Gareeb';
	ELSE
		c_rank := 'No such grade';
END CASE;

DBMS_OUTPUT.PUT_LINE(c_rank);

END;
/