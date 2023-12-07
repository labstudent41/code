CREATE TABLE accounts (acc_number NUMBER, balance NUMBER);

CREATE OR REPLACE PACKAGE account AS
	PROCEDURE acc_open (acc_number NUMBER, balance NUMBER);
	PROCEDURE acc_update (accn NUMBER, amount NUMBER);
	PROCEDURE withdraw (accn NUMBER, amount NUMBER);
END account;

/

CREATE OR REPLACE PACKAGE BODY account AS
	PROCEDURE acc_open (acc_number NUMBER, balance NUMBER) IS
    BEGIN
		INSERT INTO accounts VALUES (acc_number, balance);
		COMMIT;
	END acc_open;
	PROCEDURE acc_update (accn NUMBER, amount NUMBER) IS
    BEGIN
		UPDATE accounts SET balance=amount
			WHERE accounts.acc_number=accn;
		COMMIT;
	END acc_update;
	PROCEDURE withdraw (accn NUMBER, amount NUMBER) IS
    BEGIN
		UPDATE accounts SET balance=balance-amount
			WHERE accounts.acc_number=accn;
		COMMIT;
	END withdraw;
END account;

/

execute account.acc_open(1, 200);
execute account.acc_open(2, 500);
execute account.acc_open(3, 900);
execute account.acc_open(4, 100);
execute account.acc_open(5, 600);

execute account.acc_update(2, 800);
execute account.withdraw(5, 100);

SELECT * FROM accounts;
