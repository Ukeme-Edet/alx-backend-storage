-- A SQL script that creates a stored procedure `AverageScoreForUser` that computes the average score for a user
-- Requirements:
-- - Procedure `AverageScoreForUser` takes 1 input:
-- - - `user_id`, a users.id (`user_id` is linked to an existing `users`)
DELIMITER //
CREATE PROCEDURE AverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE avg_score DECIMAL(5, 2);
	
	-- Compute the average score
	SELECT AVG(score) INTO avg_score
	FROM corrections
	WHERE user_id = user_id;
	
	-- If the user has no score, set the average to 0
	IF avg_score IS NULL THEN
		SET avg_score = 0;
	END IF;

	-- Set the average score for the user
	UPDATE users
	SET average_score = avg_score
	WHERE id = user_id;
END//
DELIMITER ;
