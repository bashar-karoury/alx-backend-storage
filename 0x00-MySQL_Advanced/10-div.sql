-- Safe divide  
--  creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.
DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
BEGIN
    -- Code to compute the return value
	IF b = 0 THEN
		RETURN 0;
	END IF;
    RETURN a/b; -- Return statement
END$$
DELIMITER ;
