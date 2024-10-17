-- Weighted Average score 
-- creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN id INT)
BEGIN
	-- Get project id by project name
	DECLARE student_sum INT;
	DECLARE student_weight_sum INT;
	DECLARE student_average FLOAT DEFAULT 0;
	-- Calculate weighted sum of scores and total weights
    	SELECT SUM(corrections.score * projects.weight), SUM(projects.weight)
    	INTO student_sum, student_weight_sum
    	FROM corrections
    	JOIN projects ON corrections.project_id = projects.id
    	WHERE corrections.user_id = user_id;

	IF student_count <> 0 THEN
		SET student_average = student_sum / student_weight_sum;
	END IF;
	UPDATE users
	SET average_score = student_average WHERE users.id = id;
END$$
DELIMITER ;
