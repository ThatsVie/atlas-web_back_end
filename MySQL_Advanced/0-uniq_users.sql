-- Task 0: We are all unique!
-- Create the 'users' table with unique email constraint

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY (id)
);

-- The id is like a sunflower growing tall, reaching for the light, 
-- even in the midst of storms. It stands firm, unique, and beautiful.

-- The email is like the first flower blooming after winter
-- each one is different, delicate, and special, holding its place in the world.

-- When you try to insert a duplicate email, it’s like trying to plant two trees in the same spot. 
-- One will always be rooted first, claiming its place, and the other must find its own path.

-- Uniqueness in our data, like in life, allows each piece to shine on its own. 
-- Together, these unique elements form a garden of beauty, even if chaos surrounds us.
