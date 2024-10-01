-- This procedure computes the average weighted score for all users.
-- It calculates the average weighted score for each user by multiplying each project's score with its weight,
-- summing the results, and dividing by the total weight of the projects for each user.
-- The average_score field in the users table is updated for each user.

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight INT;
    DECLARE user_id INT;

    -- Cursor to iterate over all users
    DECLARE done INT DEFAULT 0;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    -- Open the cursor
    OPEN cur;

    -- Loop through each user
    read_loop: LOOP
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Calculate the total weighted score for the current user
        SELECT SUM(c.score * p.weight) INTO total_weighted_score
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        -- Calculate the total weight for the current user
        SELECT SUM(p.weight) INTO total_weight
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        -- Update the user's average_score based on the weighted average
        IF total_weight > 0 THEN
            UPDATE users
            SET average_score = total_weighted_score / total_weight
            WHERE id = user_id;
        END IF;

    END LOOP;

    -- Close the cursor
    CLOSE cur;
END //

DELIMITER ;
