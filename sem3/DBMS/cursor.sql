CREATE TABLE customer (id INTEGER, name VARCHAR(20), age INTEGER,
					address VARCHAR(20), salary INTEGER);
INSERT INTO customer VALUES (1, 'Utkarsh', 20, 'Vasai East', 25000);
INSERT INTO customer VALUES (2, 'Azan', 25, 'Vasai East', 30000);
INSERT INTO customer VALUES (3, 'Russel', 28, 'Vasai West', 50000);
INSERT INTO customer VALUES (4, 'Laxman', 24, 'Nalasopara', 35000);
INSERT INTO customer VALUES (5, 'Sahil', 27, 'Nalasopara', 30000);

DECLARE
	total_row NUMBER(2);
BEGIN
	UPDATE customer SET salary=salary+5000;
	IF SQL%NOTFOUND THEN
		DBMS_OUTPUT.PUT_LINE('No customers selected');
	ELSIF SQL%FOUND THEN
		total_row := SQL%ROWCOUNT;
		DBMS_OUTPUT.PUT_LINE(total_row || 'customer selected');
	END IF;
	SELECT * FROM customer;
END;

DECLARE
	c_id customer.id%TYPE;
	c_name customer.name%TYPE;
	c_addr customer.address%TYPE;
	CURSOR c_cust is SELECT id, name, address from customer;
BEGIN
	OPEN c_cust;
	LOOP
		FETCH c_cust into c_id, c_name, c_addr;
		EXIT WHEN c_cust%NOTFOUND;
		DBMS_OUTPUT.PUT_LINE(c_id || ' ' || c_name || ' ' || c_addr);
	END LOOP;
	CLOSE c_cust;
END;

/