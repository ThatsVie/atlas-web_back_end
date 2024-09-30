-- Show users and update (or not) the email
SELECT * FROM users;

-- Update valid_email without changing the email
UPDATE users SET valid_email = 1 WHERE email = "bob@dylan.com";

-- Change the email, which should reset valid_email to 0
UPDATE users SET email = "sylvie+new@dylan.com" WHERE email = "sylvie@dylan.com";

-- Update the name, which should NOT reset valid_email
UPDATE users SET name = "Jannis" WHERE email = "jeanne@dylan.com";

-- Show the results
SELECT "--";
SELECT * FROM users;

-- Attempt to update the email with the same value, which should NOT reset valid_email
UPDATE users SET email = "bob@dylan.com" WHERE email = "bob@dylan.com";

-- Show the final results
SELECT "--";
SELECT * FROM users;
