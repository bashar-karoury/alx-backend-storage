-- Average weighted score for all 
-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average score for all students
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	-- Get project id by project name
	DECLARE student_sum INT;
	DECLARE student_weight_sum INT;
	DECLARE student_average FLOAT DEFAULT 0;
	DECLARE student_id INT DEFAULT 0;

	-- create cursor to loop thru users

	-- Declare a cursor to fetch all student ids
    	DECLARE student_cursor CURSOR FOR SELECT id FROM users;
    
    	-- Declare a handler to detect when the cursor is finished
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;
	-- open cursor
	OPEN student_cursor;

	-- loop
	student_loop: LOOP
		-- fetch next student
		FETCH student_cursor INTO student_id;
		-- exit condition
		IF finished = 1 THEN
			LEAVE student_loop;
		END IF;
		-- Calculate weighted sum of scores and total weights
    		SELECT SUM(corrections.score * projects.weight), SUM(projects.weight)
	    	INTO student_sum, student_weight_sum
    		FROM corrections
	    	JOIN projects ON corrections.project_id = projects.id
    		WHERE corrections.user_id = student_id;

		IF student_weight_sum <> 0 THEN
			SET student_average = student_sum / student_weight_sum;
		END IF;
		UPDATE users
		SET average_score = student_average
		WHERE users.id = student_id;
	END LOOP student_loop;
	CLOSE student_cursor;
END$$
DELIMITER ;
