-- This function safely divides two numbers, returning 0 if the second number (b) is 0.
-- We use DETERMINISTIC because, given the same inputs (a and b), the result will always be the same.
-- MySQL can optimize this function knowing that the output does not change for the same input.

DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
DETERMINISTIC -- The result is predictable and will always return the same output for the same inputs
BEGIN
    -- If the second number is 0, return 0 to avoid division by zero error
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END //

DELIMITER ;

-- The SafeDiv function ensures no division by zero issues,
-- acting like a safeguard for when the divisor vanishes,
-- much like protecting our resources as they dwindle to zero.
