-- A SQL script that creates a stored procedure `ComputeAverageScoreForUser` that computes and stores the average score for a student
-- Requirements:
-- - Procedure `ComputeAverageScoreForUser` takes 1 input:
-- - - `user_id`, a users.id (`user_id` is linked to an existing `users`)
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE avg_score FLOAT;
	
	-- Compute the average score
	SELECT AVG(score) INTO avg_score
	FROM corrections
	WHERE corrections.user_id = user_id;
	
	-- Update the user's average score
	UPDATE users
	SET average_score = avg_score
	WHERE id = user_id;
END//
DELIMITER ;
