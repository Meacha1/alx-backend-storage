--  a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (
    IN user_id INT
)
BEGIN
  DECLARE total_score FLOAT;
  DECLARE total_weight FLOAT;

  SELECT SUM(c.score * p.weight) INTO total_score 
  FROM users AS u
  JOIN corrections AS c ON u.id = c.user_id 
  JOIN projects AS p ON c.project_id = p.id
  WHERE u.id = user_id;

  SELECT SUM(p.weight) INTO total_weight
  FROM projects AS p
  JOIN corrections AS c ON p.id = c.project_id
  WHERE c.user_id = user_id;

  UPDATE users SET average_score = total_score / total_weight WHERE id = user_id;

END$$
DELIMITER ;