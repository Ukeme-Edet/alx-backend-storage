-- A SQL script that creates a function `SafeDiv` that divides (and returns) the firt by the seconf number or returns 0 if the second number is equal to 0
-- Requirements:
-- - A function must be created
-- - The function `SafeDiv` must take 2 arguments:
-- - - `a`, INT
-- - - `b`, INT
-- And returns `a / b` or 0 if `b == 0`
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
	IF b = 0 THEN
		RETURN 0;
	END IF;
	RETURN a / b;
END//
DELIMITER ;
