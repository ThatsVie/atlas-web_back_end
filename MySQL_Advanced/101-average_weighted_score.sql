-- This procedure computes the average weighted score for all users.
-- For each user, the procedure calculates the average weighted score by multiplying each project's score with its weight,
-- summing the results, and dividing by the total weight of the projects.
-- It updates the average_score field in the users table for each user.

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE current_user_id INT;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cur;

    -- Loop through each user to calculate and update their average weighted score
    read_loop: LOOP
        FETCH cur INTO current_user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Calculate the total weighted score and total weight for each user
        CALL ComputeAverageWeightedScoreForUser(current_user_id);
    END LOOP;

    CLOSE cur;
END //

DELIMITER ;
