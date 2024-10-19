-- A SQL script that creates a stored procedure `ComputeAverageWeightedScoreForUser` that computes and stores the average weighted score for a student
-- Requirements:
-- - Procedure `ComputeAverageWeightedScoreForUser` takes 1 input:
-- - - `user_id`, a users.id (`user_id` is linked to an existing `users`)
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
DELIMITER ;
