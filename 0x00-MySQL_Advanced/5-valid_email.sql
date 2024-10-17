-- Email validation to sent 
-- TRIGGER AFTER UPDATE
DELIMITER $$
CREATE 
TRIGGER `resetValidaEmail`
BEFORE UPDATE ON `users`
FOR EACH ROW
	-- Edit trigger body code below this line. Do not edit lines above this one
BEGIN 
	IF OLD.email <> NEW.email THEN
		SET NEW.valid_email = FALSE;
	END IF;
END$$
DELIMITER ;
