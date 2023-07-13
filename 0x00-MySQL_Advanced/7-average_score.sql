-- Task: Compute and store the average score for a student

-- Procedure: ComputeAverageScoreForUser
-- Input: user_id, a users.id value
-- Computes and updates the average score for the user with the given user_id
-- If there are no corrections for the user, the average score is set to 0

DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
	UPDATE users
	SET
	average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id)
	WHERE id = user_id;

END $$

DELIMITER ;