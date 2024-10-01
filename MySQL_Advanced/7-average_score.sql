-- This stored procedure calculates the average score for a given user_id.
-- It updates the average_score field in the users table based on the user's scores in the corrections table.


DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;

    -- Calculate the average score for the user
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = user_id;

    -- Update the user's average_score field in the users table
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END //

DELIMITER ;

-- This procedure is like tracking global temperatures.
-- As scores (like carbon emissions) accumulate, it recalculates the average (the rising temperature),
-- keeping a pulse on the critical balance. Without regular updates, things could spiral out of control.
