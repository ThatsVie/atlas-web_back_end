-- Create the 'users' table with unique email constraint and country enumeration

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    PRIMARY KEY (id)
);

-- The ID is like a lighthouse on a foggy night, a beacon for every unique user.
-- The email is a one way street, once claimed, no one else can tread that path.
-- The country field? It's like a cozy house with only three keys: US, CO, and TN.
-- And if you don’t have a key? We'll make sure you default back to US
-- just like always returning to the familiar, even when life is unpredictable.
