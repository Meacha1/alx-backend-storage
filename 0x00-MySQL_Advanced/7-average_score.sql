-- SQL script that creates a stored procedure ComputeAverageScoreForUser
--that computes and store the average score for a student
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score DECIMAL(10,2);
    DECLARE total_projects INT;
    DECLARE avg_score DECIMAL(10,2);

    SELECT SUM(score), COUNT(DISTINCT project_id)
    INTO total_score, total_projects
    FROM corrections
    WHERE user_id = user_id;

    IF total_projects > 0 THEN
        SET avg_score = total_score / total_projects;
    ELSE
        SET avg_score = 0;
    END IF;

    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END //

DELIMITER ;
