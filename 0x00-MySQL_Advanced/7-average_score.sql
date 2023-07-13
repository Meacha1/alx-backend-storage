-- Task: Compute and store the average score for a student

-- Procedure: ComputeAverageScoreForUser
-- Input: user_id, a users.id value
-- Computes and updates the average score for the user with the given user_id
-- If there are no corrections for the user, the average score is set to 0

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score DECIMAL(10,2);
    DECLARE total_projects INT;
    DECLARE avg_score DECIMAL(10,2);

    -- Calculate the sum of scores and the count of distinct project IDs for the user
    SELECT SUM(score), COUNT(DISTINCT project_id)
    INTO total_score, total_projects
    FROM corrections
    WHERE user_id = user_id;

    -- Compute the average score
    IF total_projects > 0 THEN
        SET avg_score = total_score / total_projects;
    ELSE
        SET avg_score = 0;
    END IF;

    -- Update the average_score field of the user
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END $$

DELIMITER ;
