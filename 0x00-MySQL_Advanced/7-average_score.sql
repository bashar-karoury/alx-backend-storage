-- Average score 
-- creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN id INT)
BEGIN
	-- Get project id by project name
	DECLARE student_sum INT;
	DECLARE student_count INT;
	DECLARE student_average FLOAT DEFAULT 0;
	SELECT SUM(score), COUNT(score) INTO student_sum, student_count FROM corrections
	WHERE user_id = id; 
	IF student_count <> 0 THEN
		SET student_average = student_sum / student_count;
	END IF;
	UPDATE users
	SET average_score = student_average WHERE users.id = id;
END$$
DELIMITER ;
