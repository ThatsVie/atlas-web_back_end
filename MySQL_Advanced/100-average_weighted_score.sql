-- This procedure computes the average weighted score for a given user (input_user_id).
-- The average weighted score is calculated by multiplying each project's score with its weight, 
-- summing the results, and dividing by the total weight of the projects.
-- It updates the average_score field in the users table with the weighted average for the user.
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN input_user_id INT)
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight INT;

    -- Calculate the total weighted score for the given user
    SELECT SUM(c.score * p.weight) INTO total_weighted_score
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = input_user_id;

    -- Calculate the total weight for the user's projects
    SELECT SUM(p.weight) INTO total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = input_user_id;

    -- Update the user's average_score based on the weighted average
    IF total_weight > 0 THEN
        UPDATE users
        SET average_score = total_weighted_score / total_weight
        WHERE id = input_user_id;
    END IF;
END //

DELIMITER ;
