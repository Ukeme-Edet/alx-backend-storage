-- A SQL script that creates a stored procedure `ComputeAverageWeightedScoreForUsers` that computes and stores the average weighted score for all students
-- Requirements:
-- - Procedure `ComputeAverageWeightedScoreForUsers` takes no input
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE avg_weighted_score FLOAT DEFAULT 0;
	DECLARE total_score FLOAT DEFAULT 0;
	DECLARE total_weight FLOAT DEFAULT 0;

	-- Compute the total score and total weight
	SELECT SUM(score * weight), SUM(weight) INTO total_score, total_weight
	FROM corrections
	JOIN projects ON corrections.project_id = projects.id
	WHERE corrections.user_id = user_id;

	-- Compute the average weighted score
	IF total_weight > 0 THEN
		SET avg_weighted_score = total_score / total_weight;
	ELSE
		SET avg_weighted_score = 0;
	END IF;

	-- Update the user's average weighted score
	UPDATE users
	SET average_score = avg_weighted_score
	WHERE id = user_id;
END//
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE user_id INT;
	
	-- Get all user IDs
	CREATE TEMPORARY TABLE IF NOT EXISTS user_ids AS
		SELECT id
		FROM users;
	
	-- Loop through each user ID
	WHILE (SELECT COUNT(*) FROM user_ids) > 0 DO
		SELECT id INTO user_id
		FROM user_ids
		LIMIT 1;
		
		-- Compute the average weighted score for the user
		CALL ComputeAverageWeightedScoreForUser(user_id);
		
		-- Remove the user ID from the temporary table
		DELETE FROM user_ids
		WHERE id = user_id;
	END WHILE;
	
	DROP TEMPORARY TABLE IF EXISTS user_ids;
END//
DELIMITER ;
