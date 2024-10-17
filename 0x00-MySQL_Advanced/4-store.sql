-- Triggers After insert
-- mulitple tables
DELIMITER $$
CREATE 
TRIGGER `DecreaseQunatities`
AFTER INSERT ON `orders`
FOR EACH ROW
	-- Edit trigger body code below this line. Do not edit lines above this one
BEGIN 
	UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
END$$
DELIMITER ;
