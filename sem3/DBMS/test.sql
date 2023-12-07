DECLARE
a number := 20;
b number := 10;
add number := a + b;
sub number := a - b;
mul number := a * b;
div number := a / b;

BEGIN
dbms_output.put_line('Sum : ' || add);
dbms_output.put_line('Not Eligible');
dbms_output.put_line('Not Eligible');
dbms_output.put_line('Not Eligible');

END;
/
