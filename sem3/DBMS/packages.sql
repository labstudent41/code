CREATE OR REPLACE PACKAGE hr AS
	PROCEDURE hire (id IN NUMBER, name IN VARCHAR2, age NUMBER,
				address VARCHAR2, salary NUMBER);
	PROCEDURE fire (id IN NUMBER);
END hr;
/

CREATE OR REPLACE PACKAGE BODY hr AS
    
	PROCEDURE hire (id IN NUMBER, name IN VARCHAR2, age NUMBER,
				address VARCHAR2, salary NUMBER) IS
	BEGIN
		INSERT INTO customer VALUES (id, name, age, address, salary);
		COMMIT;
	END hire;
	
	PROCEDURE fire (id IN NUMBER) IS
	BEGIN
		DELETE FROM customer WHERE id=id;
		COMMIT;
	END fire;
	
END;

/
