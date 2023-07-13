-- a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students.
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  DECLARE user_id INT;

  DECLARE users_cursor CURSOR FOR 
  SELECT id FROM users;

  OPEN users_cursor;

  users_loop: LOOP
    FETCH users_cursor INTO user_id;

    CALL ComputeAverageWeightedScoreForUser(user_id);

  END LOOP users_loop;

  CLOSE users_cursor;

END$$
DELIMITER ;