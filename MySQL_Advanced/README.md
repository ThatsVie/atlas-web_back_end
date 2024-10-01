<div align="center">
    <img src="https://github.com/user-attachments/assets/98e2e92e-c592-41ae-9223-be0aa0a6eee3" alt="puginacandystore" />
    <h1>MySQL Advanced</h1>
    <p>In this project, we will dive deeper into MySQL by exploring advanced features such as table constraints, indexing, stored procedures, triggers, and views. We will also focus on optimizing queries and ensuring our database structure is well-organized and efficient.</p>
</div>

## Concepts

For this project, we expect you to look at this concept:

- [Advanced SQL](https://intranet.atlasschool.com/concepts/877)

## Resources

Read or watch the following resources to better understand the topics covered in this project:

- [MySQL cheatsheet](https://devhints.io/mysql)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.liquidweb.com/blog/mysql-optimization-how-to-leverage-mysql-database-indexing/)
- [Stored Procedure](https://www.w3resource.com/mysql/mysql-procedure.php)
- [Triggers](https://www.w3resource.com/mysql/mysql-triggers.php)
- [Views](https://www.w3resource.com/mysql/mysql-views.php)
- [Functions and Operators](https://dev.mysql.com/doc/refman/5.7/en/functions.html)
- [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/5.7/en/create-index.html)
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/5.7/en/create-view.html)

### Learning Objectives

- How to create tables with constraints
- How to optimize queries by adding indexes
- What are stored procedures and functions, and how to implement them in MySQL
- What are views, and how to implement them in MySQL
- What are triggers, and how to implement them in MySQL

## Requirements


- All files will be executed on Ubuntu 20.04 LTS using MySQL 8.0
- All SQL queries must have a comment just before (i.e., syntax explanations above each query)
- All SQL files must start with a comment describing the task
- All SQL keywords should be in uppercase (`SELECT`, `WHERE`, etc.)
- A `README.md` file, at the root of the project folder, is mandatory
- The length of your files will be tested using `wc`

### Comments Example

```
-- Get the 3 first students in the Batch ID=3
-- Because Batch 3 is obviously the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

### How to Import an SQL Dump

```bash
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password:
$ curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password:
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password:
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
```

## Tasks and Usage

### Task 0: We are all unique!

In this task, we create a `users` table in MySQL. The table contains three fields: `id`, `email`, and `name`. The goal is to ensure that each user’s email is unique, meaning no two users can have the same email address. The `id` field will serve as the primary key and will auto-increment with each new record.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a SQL script that creates a table `users` with the following attributes:
  - `id`: integer, auto-increment, primary key, never null.
  - `email`: string (255 characters), unique, never null.
  - `name`: string (255 characters).
- The script should not fail if the table already exists.
- The script should work with any database.
- Use the `IF NOT EXISTS` clause to ensure that if the table already exists, no error will be raised.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

**Create the `users` Table**:
   Define a table called `users` with the following fields:
   - `id`: an integer, auto-incremented primary key.
   - `email`: a string (up to 255 characters), unique and not null.
   - `name`: a string (up to 255 characters).

   ```sql
   CREATE TABLE IF NOT EXISTS users (
       id INT AUTO_INCREMENT,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255),
       PRIMARY KEY (id)
   );
   ```

   - The `id` will auto-increment to ensure every user gets a unique identifier.
   - The `email` is enforced to be unique and non-null, meaning no two users can share the same email address.
   - The `IF NOT EXISTS` clause prevents errors if the table already exists.


</details>

<details>
  <summary><strong>Testing and Usage</strong></summary>

1. **Create the Database**:
   First, ensure the database exists. Create the `holberton` database by running:

   ```bash
   echo "CREATE DATABASE holberton;" | mysql -uroot -p
   ```

2. **Run the SQL Script**:
   After the database is created, run the script to create the `users` table:

   ```bash
   cat 0-uniq_users.sql | mysql -uroot -p holberton
   ```

3. **Insert Users**:
   Insert users with unique emails:

   ```bash
   echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -uroot -p holberton
   echo 'INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");' | mysql -uroot -p holberton
   ```

4. **Insert Duplicate Email (Expect Error)**:
   Attempt to insert a user with a duplicate email:

   ```bash
   echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");' | mysql -uroot -p holberton
   ```

   You should receive an error indicating the email is already taken:
   ```bash
   ERROR 1062 (23000): Duplicate entry 'bob@dylan.com' for key 'email'
   ```

5. **View the Data**:
   Finally, view the contents of the `users` table:

   ```bash
   echo "SELECT * FROM users;" | mysql -uroot -p holberton
   ```

   **Expected Output**:
   ```bash
   id      email               name
   1       bob@dylan.com       Bob
   2       sylvie@dylan.com    Sylvie
   ```
   </details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong> </summary>

- **What**: We created a `users` table with three fields: `id`, `email`, and `name`. Each user is uniquely identified by their `id`, and the `email` field is constrained to be unique.
- **Where**: This is performed in a MySQL database (`holberton`).
- **Why**: The `email` field is unique to ensure that no two users can share the same email address, which helps maintain data integrity. The `id` field is the primary key to uniquely identify each user.
- **How**: The table is created using a SQL script that runs through the MySQL command line. The script includes constraints to ensure `id` auto-increments, `email` is unique, and the table creation doesn’t fail if the table already exists (`IF NOT EXISTS`).
- **Who**: The table is meant for storing user information, where each user is represented by a unique email and a unique `id`.
- **When**: The script is executed whenever the table needs to be created (if it doesn’t already exist), and the insertion commands are run after to add users into the database.

</details>


### Task 1: In and not out

In this task, we extend the `users` table by adding a new field `country`. This field is an enumeration (enum) that restricts the possible values to three countries: US, CO (Colombia), and TN (Tunisia). The default value for `country` is `US` if none is provided.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a SQL script that creates a table `users` with the following attributes:
  - `id`: integer, auto-increment, primary key, never null.
  - `email`: string (255 characters), unique, never null.
  - `name`: string (255 characters).
  - `country`: enum of countries (US, CO, TN), never null, default value is US.
- The script should not fail if the table already exists.
- The script can be executed on any database.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

**Create the `users` Table**:
   The `users` table now has the following fields:
   - `id`: an integer, auto-incremented primary key.
   - `email`: a string (up to 255 characters), unique and not null.
   - `name`: a string (up to 255 characters).
   - `country`: an enum restricted to `US`, `CO`, and `TN` with a default value of `US`.

   ```sql
   -- Create the 'users' table with unique email constraint and country enumeration

   CREATE TABLE IF NOT EXISTS users (
       id INT AUTO_INCREMENT,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255),
       country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
       PRIMARY KEY (id)
   );

   -- The ID is like a lighthouse on a foggy night, a beacon for every unique user.
   -- The email is a one-way street, once claimed, no one else can tread that path.
   -- The country field? It's like a cozy house with only three keys: US, CO, and TN.
   -- And if you don’t have a key? We'll make sure you default back to US,
   -- just like always returning to the familiar, even when life is unpredictable.
   ```

</details>

<details>
  <summary><strong>Testing and Usage</strong></summary>

1. **Create the Database**:
   Ensure the `holberton` database exists. Create it if necessary:

   ```bash
   echo "CREATE DATABASE holberton;" | mysql -uroot -p
   ```

2. **Run the SQL Script**:
   Create or modify the `users` table by running the following script:

   ```bash
   cat 1-country_users.sql | mysql -uroot -p holberton
   ```

3. **Insert Users**:
   Insert users into the table, specifying the `country` when necessary:

   ```bash
   echo 'INSERT INTO users (email, name, country) VALUES ("bob@dylan.com", "Bob", "US");' | mysql -uroot -p holberton
   echo 'INSERT INTO users (email, name, country) VALUES ("sylvie@dylan.com", "Sylvie", "CO");' | mysql -uroot -p holberton
   ```

4. **Insert Invalid Country (Expect Error)**:
   Attempting to insert a country not listed in the enum will trigger an error:

   ```bash
   echo 'INSERT INTO users (email, name, country) VALUES ("jean@dylan.com", "Jean", "FR");' | mysql -uroot -p holberton
   ```

   **Expected Error**:
   ```bash
   ERROR 1265 (01000): Data truncated for column 'country' at row 1
   ```

5. **Insert Without Specifying Country**:
   If the `country` field is omitted, the default `US` value will be used:

   ```bash
   echo 'INSERT INTO users (email, name) VALUES ("john@dylan.com", "John");' | mysql -uroot -p holberton
   ```

6. **View the Data**:
   Finally, view the contents of the `users` table:

   ```bash
   echo "SELECT * FROM users;" | mysql -uroot -p holberton
   ```

   **Expected Output**:
   ```bash
   id      email               name        country
   1       bob@dylan.com       Bob         US
   2       sylvie@dylan.com    Sylvie      CO
   3       john@dylan.com      John        US
   ```

</details>

<details>
  <summary><strong>Troubleshooting </strong></summary>

#### Issue 1: **Unknown Column 'country' in 'field list'**

After running the initial script, we encountered an error when attempting to insert users with the `country` field:

```bash
ERROR 1054 (42S22) at line 1: Unknown column 'country' in 'field list'
```

**Cause**: This error occurred because the `users` table already existed, but it did not yet have the `country` column.

**Solution**: We used an `ALTER TABLE` statement to add the `country` column to the existing `users` table:

```bash
echo "ALTER TABLE users ADD COLUMN country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US';" | mysql -uroot -p holberton
```


#### Issue 2: **Duplicate Entry for Email**

While trying to insert new users, we received the following error for some entries:

```bash
ERROR 1062 (23000) at line 1: Duplicate entry 'bob@dylan.com' for key 'users.email'
```

**Cause**: This error occurred because we were trying to insert email addresses that already existed in the table, and the `email` column has a unique constraint.

**Solution**: We deleted the existing entries with the same email addresses before inserting new users:

```bash
echo 'DELETE FROM users WHERE email="bob@dylan.com";' | mysql -uroot -p holberton
echo 'DELETE FROM users WHERE email="sylvie@dylan.com";' | mysql -uroot -p holberton
```
</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How </strong></summary>

- **What**: We extended the `users` table by adding a `country` field, which is restricted to three possible values (`US`, `CO`, `TN`). The default value is `US` if no country is specified.
- **Where**: This was implemented in the `holberton` MySQL database.
- **Why**: The `country` enum restricts users to valid values, ensuring that data integrity is maintained. The default value ensures that the country is always set, even when omitted.
- **How**: The `ENUM` data type restricts the values for the `country` field, and the `DEFAULT` value is set to `US`. If an invalid value is inserted, MySQL will raise an error.
- **Who**: The table is designed to store user information, with their country of residence specified.
- **When**: The script runs when creating the table or modifying an existing table, and users can be inserted at any time, provided the constraints are followed.

</details>

### Task 2: Best band ever!

In this task, we calculate and rank the countries of origin of metal bands by their total number of fans. The ranking is ordered by the number of fans in descending order.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a SQL script that ranks the origins of bands by their total number of fans (not unique).
- The result should be ordered by the number of fans in descending order.
- Column names must be `origin` and `nb_fans`.
- Your script can be executed on any database.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

**Steps to execute:**

1. **Download and extract the table dump**: 
   Download the `metal_bands.sql.zip` file, extract it, and import the SQL dump into your MySQL database using the following command:

   ```bash
   cat metal_bands.sql | mysql -uroot -p holberton
   ```

2. **Write the SQL query**:
   Create a script (`2-fans.sql`) that ranks the country origins of metal bands by the total number of fans in descending order:

   ```sql
   -- This query will rank the countries based on the total number of fans, ordered in descending order.

   SELECT origin, SUM(fans) AS nb_fans
   FROM metal_bands
   GROUP BY origin
   ORDER BY nb_fans DESC;
   ```

3. **Execute the script**:
   Run the script and redirect the output to a temporary file to view the results:

   ```bash
   cat 2-fans.sql | mysql -uroot -p holberton > tmp_res; head tmp_res
   ```

4. **Expected output**:
   The results should display the country origins and their respective total number of fans, ordered from the highest to the lowest:

   ```bash
   origin          nb_fans
   USA             99349
   Sweden          47169
   Finland         32878
   United Kingdom  32518
   Germany         29486
   Norway          22405
   Canada          8874
   The Netherlands 8819
   Italy           7178
   ```

**Explanation of the Output**

- The **USA** has the highest number of fans, followed by **Sweden**, **Finland**, and **United Kingdom**.
- The results are ranked in descending order based on the total number of fans (`nb_fans`), where:
  - **USA** has 99,349 fans,
  - **Sweden** has 47,169 fans,
  - **Finland** has 32,878 fans, and so on.
- Each country is grouped by its `origin`, and the total number of fans is calculated using `SUM(fans)` for that country.
</details>

<details>
  <summary><strong>Troubleshooting</strong></summary>

#### Issue: **Unknown Column 'nb_fans' in 'field list'**

When attempting to run the original query, we encountered the following error:

```bash
ERROR 1054 (42S22) at line 3: Unknown column 'nb_fans' in 'field list'
```

**Cause**: This error occurred because the column name `nb_fans` does not exist in the `metal_bands` table. The actual column name for the number of fans is `fans`.

**Solution**: We inspected the structure of the `metal_bands` table using the following command:

```bash
echo "DESCRIBE metal_bands;" | mysql -uroot -p holberton
```

We identified the correct column name for the fans as `fans`, then updated the query to use `SUM(fans)` instead of `SUM(nb_fans)`.

Updated query:

```sql
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: We rank countries based on the total number of metal band fans, aggregated by country.
- **Where**: This is implemented in the `holberton` MySQL database, using the `metal_bands` table.
- **Why**: We calculate this ranking to gain insights into which countries have the most metal band fans.
- **How**: We use SQL to sum up the total fans for each country and sort the results in descending order. The column for fans is `fans`, and we group by the `origin` column.
- **Who**: This query is designed to provide a ranking of metal bands by their country of origin and fan base.
- **When**: The query runs after importing the `metal_bands.sql` dump and can be executed at any time to recalculate the ranking.

</details>

### Task 3: Old school band

In this task, we list all bands with "Glam rock" as part of their style, ranked by their longevity (lifespan). We calculate the lifespan using the `formed` and `split` columns.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a SQL script that lists all bands with "Glam rock" as their main style.
- The bands should be ranked by their longevity (lifespan).
- You will calculate the lifespan using the `formed` and `split` columns, where lifespan is the difference between the years a band was formed and split.
- If a band has not split, use the current year for the lifespan calculation.
- Column names must be `band_name` and `lifespan (in years)`.
- Your script can be executed on any database.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

**Steps to execute:**

1. **Download and extract the table dump**: 
   Download the `metal_bands.sql.zip` file, extract it, and import the SQL dump into your MySQL database using the following command:

   ```bash
   cat metal_bands.sql | mysql -uroot -p holberton
   ```

2. **Write the SQL query**:
   Create a script (`3-glam_rock.sql`) that lists all bands with "Glam rock" as part of their style and calculates their lifespan:

   ```sql
   -- List all Glam rock bands ranked by their longevity

   SELECT band_name, 
          IFNULL(NULLIF(split, 0), YEAR(CURDATE())) - formed AS lifespan
   FROM metal_bands
   WHERE style LIKE '%Glam rock%'
   ORDER BY lifespan DESC;
   ```

   **Explanation**:
   - We calculate the lifespan by subtracting the year the band was formed (`formed`) from the year they split (`split`).
   - If a band has not split (i.e., `split` is `NULL` or `0`), we use the current year (`YEAR(CURDATE())`).
   - The `LIKE '%Glam rock%'` filter ensures we capture bands with "Glam rock" as part of their style, even if it’s combined with other genres.

3. **Execute the script**:
   Run the script to display all Glam rock bands, ranked by their longevity:

   ```bash
   cat 3-glam_rock.sql | mysql -uroot -p holberton
   ```

4. **Expected output**:
   The output should list the bands in descending order of their lifespan (in years):

   ```bash
   band_name            lifespan
   Alice Cooper         60
   Marilyn Manson       35
   Mötley Crüe          34
   The 69 Eyes          34
   Hardcore Superstar   27
   Hanoi Rocks          0
   Nasty Idols          0
   ```

</details>

<details>
  <summary><strong>Troubleshooting</strong></summary>

#### Issue 1: **Missing Bands with 'Glam rock'**

Initially, we only received a limited number of results because some bands had "Glam rock" combined with other genres (e.g., "Glam rock,Gothic rock"). 

**Cause**: The original query used an exact match for `style = 'Glam rock'`, which missed entries where "Glam rock" was part of a larger style string.

**Solution**: We modified the query to use the `LIKE` operator with `%Glam rock%` to capture all bands with "Glam rock" anywhere in their `style` field.

Updated query:

```sql
SELECT band_name, 
       IFNULL(NULLIF(split, 0), YEAR(CURDATE())) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
```

#### Issue 2: **Handling `split = 0`**

Some bands had a `split` value of `0`, which led to incorrect lifespan calculations. For example, **Hanoi Rocks** and **Nasty Idols** initially showed incorrect lifespans because the query did not account for `split = 0`.

**Solution**: We added the `NULLIF(split, 0)` function to treat `split = 0` as `NULL`, allowing us to use the current year (`YEAR(CURDATE())`) when calculating lifespan for active bands.

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: We list all bands that include "Glam rock" in their style and rank them by their lifespan (in years).
- **Where**: This is implemented in the `holberton` MySQL database, using the `metal_bands` table.
- **Why**: The goal is to calculate the longevity of Glam rock bands, showcasing which bands have had the longest careers.
- **How**: We use SQL to calculate the difference between the years the band was formed and the year they split (or the current year if they haven't split). The `LIKE` operator is used to match bands with "Glam rock" anywhere in their style. We handle `split = 0` by treating it as if the band hasn't split.
- **Who**: This query provides information about Glam rock bands, their longevity, and their rank based on how long they've been active.
- **When**: The query runs after importing the `metal_bands.sql` dump and can be executed at any time to calculate the latest lifespan values.

</details>

### Task 4: Buy buy buy

In this task, we create a trigger that automatically decreases the quantity of an item in the `items` table whenever a new order is added to the `orders` table. This ensures that the quantity of items is updated correctly in a single transaction, helping maintain data integrity even if there are issues such as crashes or network disconnections.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a SQL script that creates a trigger to decrease the quantity of an item after adding a new order.
- Quantity in the table `items` can be negative.
- Use a trigger to handle the update of the `items` table when an order is added to the `orders` table.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

#### 1. **4-init.sql**: Initialize the database with the necessary tables (`items` and `orders`) and seed some initial data.

```sql
-- Initial setup for items and orders tables
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS orders;

CREATE TABLE IF NOT EXISTS items (
    name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL DEFAULT 10
);

CREATE TABLE IF NOT EXISTS orders (
    item_name VARCHAR(255) NOT NULL,
    number INT NOT NULL
);

-- Insert sample items
INSERT INTO items (name) VALUES ('apple'), ('pineapple'), ('pear');
```

- **Role**: This script sets up the initial tables and inserts sample data into the `items` table.
- **How It Works**: 
  - The `items` table has two fields: `name` and `quantity`. Each item starts with a quantity of 10.
  - The `orders` table will be used to record new orders placed for items.

#### 2. **4-store.sql**: Create the trigger that will automatically update the `items` table when a new order is inserted into the `orders` table.

```sql
DELIMITER //

CREATE TRIGGER update_quantity AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END //

DELIMITER ;
```

- **Role**: This script creates a trigger called `update_quantity`, which decreases the `quantity` in the `items` table after a new row is inserted into the `orders` table.
- **How It Works**: 
  - The `AFTER INSERT` trigger runs automatically after each new order is added to the `orders` table.
  - The `NEW.item_name` and `NEW.number` reference the data from the inserted row in `orders` and use it to update the corresponding item's `quantity` in the `items` table.

#### 3. **4-main.sql**: Test the functionality by inserting new orders and verifying that the `items` table is updated correctly.

```sql
-- Show and add orders
SELECT * FROM items;
SELECT * FROM orders;

-- Insert new orders
INSERT INTO orders (item_name, number) VALUES ('apple', 1);
INSERT INTO orders (item_name, number) VALUES ('apple', 3);
INSERT INTO orders (item_name, number) VALUES ('pear', 2);

-- Display updated results
SELECT "--";
SELECT * FROM items;
SELECT * FROM orders;
```

- **Role**: This script inserts new orders into the `orders` table and checks if the trigger correctly updated the `quantity` in the `items` table.
- **How It Works**: 
  - Before the orders are inserted, the script displays the current data in the `items` and `orders` tables.
  - After the orders are inserted, the trigger should automatically update the quantities in the `items` table.
  - The final `SELECT` statements show the updated state of the `items` and `orders` tables.

</details>

<details>
  <summary><strong>Testing and Usage</strong></summary>

1. **Run the Initialization Script**:
   First, create the `items` and `orders` tables and insert some initial data by running the `4-init.sql` script:

   ```bash
   cat 4-init.sql | mysql -uroot -p holberton
   ```

   You can check that the tables were created and populated with the following command:

   ```bash
   echo "SELECT * FROM items;" | mysql -uroot -p holberton
   ```

   **Expected Output**:
   ```
   name        quantity
   apple       10
   pineapple   10
   pear        10
   ```

2. **Create the Trigger**:
   Run the `4-store.sql` script to create the `update_quantity` trigger:

   ```bash
   cat 4-store.sql | mysql -uroot -p holberton
   ```

3. **Insert Orders and Verify Trigger**:
   Run the `4-main.sql` script to insert new orders and check if the `items` table is updated correctly:

   ```bash
   cat 4-main.sql | mysql -uroot -p holberton
   ```

   **Expected Output**:

   **Before inserting orders**:
   ```
   name        quantity
   apple       10
   pineapple   10
   pear        10
   ```

   **After inserting orders**:
   ```
   name        quantity
   apple       6
   pineapple   10
   pear        8
   item_name   number
   apple       1
   apple       3
   pear        2
   ```

   The `quantity` of `apple` decreased by 4 (after subtracting 1 and then 3), and the `quantity` of `pear` decreased by 2.

4. **Run the Scripts in the Correct Order**:
   Be sure to run the scripts in the following order to ensure the correct execution:
   - `4-init.sql`: Initializes the tables and data.
   - `4-store.sql`: Creates the trigger that updates the `items` table.
   - `4-main.sql`: Tests the trigger by inserting orders and checking if the items are updated.

</details>

<details>
  <summary><strong>Troubleshooting</strong></summary>

#### Issue 1: **Trigger Not Working**

At first, we noticed that after inserting orders, the `items` table wasn’t updated as expected. This was because the trigger hadn’t been created successfully.

**Solution**: We re-ran the `4-store.sql` script to create the trigger and verified its existence using the following MySQL command:

```sql
SHOW TRIGGERS LIKE 'orders';
```

This confirmed that the `update_quantity` trigger was now in place.

#### Issue 2: **No Changes to the Items Table**

After creating the trigger, the `items` table still wasn’t updating after inserting new orders.

**Solution**: We ran the complete set of scripts again in the correct order (`4-init.sql`, `4-store.sql`, and `4-main.sql`), which resolved the issue. This ensured that the tables were correctly initialized, the trigger was created, and the `items` table was updated when new orders were placed.

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: We created a trigger to automatically update the quantity of items in the `items` table when a new order is added to the `orders` table.
- **Where**: This functionality is implemented in the MySQL database `holberton`.
- **Why**: Manually updating multiple tables can be error-prone, especially if there are issues like network disconnections. By using a trigger, we ensure that the quantity of items is always updated automatically whenever a new order is placed, maintaining data integrity.
- **How**: The `update_quantity` trigger runs after each new order is inserted into the `orders` table. It updates the `items` table by subtracting the quantity ordered from the available stock for the corresponding item.
- **Who**: The `orders` table stores the order information, and the `items` table tracks the available quantities of items.
- **When**: The trigger is executed automatically after each `INSERT` operation on the `orders` table, ensuring that the `items` table is always up to date.

</details>

### Task 5: Email validation to sent

In this task, we created a trigger that resets the `valid_email` attribute in the `users` table only when the email has been changed. This is useful for triggering email revalidation workflows whenever a user's email is updated.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a SQL script that creates a trigger to reset the `valid_email` attribute when the email has been updated.
- The `valid_email` attribute should only be reset if the email is changed, not when other attributes (e.g., `name`) are updated.
- The trigger should automatically handle email validation logic within the database itself.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

#### 1. **5-init.sql**: Set up the `users` table and insert initial data

```sql
-- Initial setup for users table

DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    valid_email BOOLEAN NOT NULL DEFAULT 0,
    PRIMARY KEY (id)
);

-- Insert sample users
INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");
INSERT INTO users (email, name, valid_email) VALUES ("sylvie@dylan.com", "Sylvie", 1);
INSERT INTO users (email, name, valid_email) VALUES ("jeanne@dylan.com", "Jeanne", 1);
```

- **Role**: This script sets up the initial `users` table and inserts a few rows for testing.
- **How It Works**:
  - The `users` table has three fields: `email`, `name`, and `valid_email`.
  - The `valid_email` field is a boolean that starts as `0` (invalid) by default but can be set to `1` to indicate a validated email.

#### 2. **5-valid_email.sql**: Create the trigger that resets `valid_email` when the email is updated

```sql
DELIMITER //

CREATE TRIGGER reset_valid_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END //

DELIMITER ;
```

- **Role**: This script creates a trigger that resets `valid_email` to `0` only if the email has been changed.
- **How It Works**:
  - The `BEFORE UPDATE` trigger checks if the new email (`NEW.email`) is different from the old one (`OLD.email`).
  - If the email has changed, the trigger sets `NEW.valid_email` to `0`, which will reset the validation status.

#### 3. **5-main.sql**: Test the trigger by updating users’ emails and other attributes

```sql
-- Show users and update (or not) email
SELECT * FROM users;

-- Update valid_email for Bob without changing the email
UPDATE users SET valid_email = 1 WHERE email = "bob@dylan.com";

-- Update Sylvie’s email, which should reset valid_email
UPDATE users SET email = "sylvie+new@dylan.com" WHERE email = "sylvie@dylan.com";

-- Update Jeanne’s name (but not her email), so valid_email should stay the same
UPDATE users SET name = "Jannis" WHERE email = "jeanne@dylan.com";

-- Display updated results
SELECT "--";
SELECT * FROM users;

-- Another update for Bob’s email without changing the actual email
UPDATE users SET email = "bob@dylan.com" WHERE email = "bob@dylan.com";

-- Final output
SELECT "--";
SELECT * FROM users;
```

- **Role**: This script tests the `reset_valid_email` trigger by making changes to the `users` table.
- **How It Works**:
  - The initial query shows the current data in the `users` table.
  - We update Bob’s `valid_email` field without changing his email, which should not trigger the `valid_email` reset.
  - Sylvie's email is updated, so her `valid_email` should reset to `0`.
  - Jeanne’s name is updated, but since her email stays the same, her `valid_email` should not change.

</details>

<details>
  <summary><strong>Testing and Usage</strong></summary>

1. **Run the Initialization Script**:
   First, create the `users` table and insert initial data by running the `5-init.sql` script:

   ```bash
   cat 5-init.sql | mysql -uroot -p holberton
   ```

   Verify the table contents with:

   ```bash
   echo "SELECT * FROM users;" | mysql -uroot -p holberton
   ```

   **Expected Output**:
   ```
   id      email               name    valid_email
   1       bob@dylan.com       Bob     0
   2       sylvie@dylan.com    Sylvie  1
   3       jeanne@dylan.com    Jeanne  1
   ```

2. **Create the Trigger**:
   Run the `5-valid_email.sql` script to create the `reset_valid_email` trigger:

   ```bash
   cat 5-valid_email.sql | mysql -uroot -p holberton
   ```

3. **Test the Trigger**:
   Run the `5-main.sql` script to verify if the trigger behaves as expected:

   ```bash
   cat 5-main.sql | mysql -uroot -p holberton
   ```

   **Expected Output** (before and after updates):
   ```
   id      email               name    valid_email
   1       bob@dylan.com       Bob     0
   2       sylvie@dylan.com    Sylvie  1
   3       jeanne@dylan.com    Jeanne  1

   --

   id      email               name    valid_email
   1       bob@dylan.com       Bob     1
   2       sylvie+new@dylan.com    Sylvie  0
   3       jeanne@dylan.com    Jannis  1

   --

   id      email               name    valid_email
   1       bob@dylan.com       Bob     1
   2       sylvie+new@dylan.com    Sylvie  0
   3       jeanne@dylan.com    Jannis  1
   ```

   The `valid_email` field was reset for Sylvie when her email changed, and it remained unchanged for Bob and Jeanne as their emails did not change.

</details>


<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: We created a trigger to reset the `valid_email` field whenever the email is updated in the `users` table.
- **Where**: This functionality is implemented in the MySQL `holberton` database.
- **Why**: The `valid_email` field ensures that emails are validated. When an email is changed, we want the system to require revalidation, so resetting `valid_email` ensures that the email has to be validated again.
- **How**: The `BEFORE UPDATE` trigger checks if the email is changed, and if so, it resets the `valid_email` field to `0`.
- **Who**: This script applies to all users in the `users` table, ensuring email validation is handled seamlessly.
- **When**: The trigger executes automatically before any update to the `users` table when an email is changed.

</details>

### Task 6: Add Bonus

In this task, we create a stored procedure called `AddBonus`, which adds a correction score for a student (`user_id`) in a specified project (`project_name`). If the project doesn't already exist, the procedure will create it before adding the score. This procedure ensures that students can receive scores for both existing and new projects seamlessly.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a SQL script that creates a stored procedure `AddBonus` that:
  - Takes 3 inputs: `user_id`, `project_name`, and `score`.
  - Adds the `score` for the corresponding `user_id` and `project_name`.
  - If the project doesn't exist, it creates it before adding the correction.
- The procedure can be executed on any database.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

#### 1. **6-init.sql**: Initialize the database with `users`, `projects`, and `corrections` tables, and seed some initial data.

```sql
-- Initial setup for users, projects, and corrections tables
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    average_score FLOAT DEFAULT 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user_id INT NOT NULL,
    project_id INT NOT NULL,
    score INT DEFAULT 0,
    KEY `user_id` (`user_id`),
    KEY `project_id` (`project_id`),
    CONSTRAINT fk_user_id FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT fk_project_id FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO users (name) VALUES ("Bob"), ("Jeanne");
INSERT INTO projects (name) VALUES ("C is fun"), ("Python is cool");

INSERT INTO corrections (user_id, project_id, score) 
VALUES 
((SELECT id FROM users WHERE name = 'Bob'), (SELECT id FROM projects WHERE name = 'C is fun'), 80),
((SELECT id FROM users WHERE name = 'Bob'), (SELECT id FROM projects WHERE name = 'Python is cool'), 96),
((SELECT id FROM users WHERE name = 'Jeanne'), (SELECT id FROM projects WHERE name = 'C is fun'), 91),
((SELECT id FROM users WHERE name = 'Jeanne'), (SELECT id FROM projects WHERE name = 'Python is cool'), 73);
```

- **Role**: This script initializes the tables and inserts some sample data.
- **How It Works**: 
  - The `users` table stores user information.
  - The `projects` table stores project names.
  - The `corrections` table keeps track of user scores for specific projects.

#### 2. **6-bonus.sql**: Create the `AddBonus` stored procedure.

```sql
-- This stored procedure adds a correction score for a student user_id in a project project_name
-- If the project doesn't exist, it creates the project and then adds the score.
-- Corrections for both existing and new projects can be added

DELIMITER //

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT;

    -- Check if the project exists
    SELECT id INTO project_id FROM projects WHERE name = project_name;

    -- If project doesn't exist, create it
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Add the correction for the user in the project
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END //

DELIMITER ;
```

- **Role**: This script creates the stored procedure `AddBonus`.
- **How It Works**: 
  - The procedure first checks if a project with the specified `project_name` exists. 
  - If the project doesn't exist, it creates a new one.
  - Then, it adds the correction for the user and project.

#### 3. **6-main.sql**: Test the stored procedure.

```sql
-- Show and add bonus correction
SELECT * FROM projects;
SELECT * FROM corrections;

-- Add new corrections using the AddBonus procedure
CALL AddBonus((SELECT id FROM users WHERE name = 'Jeanne'), 'Python is cool', 100);
CALL AddBonus((SELECT id FROM users WHERE name = 'Jeanne'), 'Bonus project', 100);
CALL AddBonus((SELECT id FROM users WHERE name = 'Bob'), 'Bonus project', 10);
CALL AddBonus((SELECT id FROM users WHERE name = 'Jeanne'), 'New bonus', 90);

-- Display updated results
SELECT "--";
SELECT * FROM projects;
SELECT * FROM corrections;
```

- **Role**: This script tests the `AddBonus` procedure by adding corrections to existing and new projects.
- **How It Works**: 
  - The script calls the `AddBonus` procedure for different users and projects.
  - The procedure updates the `projects` and `corrections` tables accordingly.

</details>

<details>
  <summary><strong>Testing and Usage</strong></summary>

1. **Run the Initialization Script**:
   Create the initial tables (`users`, `projects`, `corrections`) and insert some sample data:

   ```bash
   cat 6-init.sql | mysql -uroot -p holberton
   ```

2. **Create the Stored Procedure**:
   Run the `6-bonus.sql` script to create the `AddBonus` procedure:

   ```bash
   cat 6-bonus.sql | mysql -uroot -p holberton
   ```

3. **Test the Stored Procedure**:
   Use the `6-main.sql` script to test adding corrections with the `AddBonus` procedure:

   ```bash
   cat 6-main.sql | mysql -uroot -p holberton
   ```

   **Expected Output** (after running `6-main.sql`):
   ```
   -- Before the procedure is called:
   id  name
   1   C is fun
   2   Python is cool

   user_id project_id  score
   1       1           80
   1       2           96
   2       1           91
   2       2           73

   --

   -- After the procedure is called:
   id  name
   1   C is fun
   2   Python is cool
   3   Bonus project
   4   New bonus

   user_id project_id  score
   1       1           80
   1       2           96
   2       1           91
   2       2           73
   2       2           100
   2       3           100
   1       3           10
   2       4           90
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: The `AddBonus` stored procedure allows you to add a correction score for a user in a specific project, creating the project if it doesn't exist.
- **Where**: The procedure is implemented in the MySQL `holberton` database.
- **Why**: Automating the process of adding corrections and ensuring that projects are created if they don’t already exist simplifies the workflow and ensures data consistency.
- **How**: The procedure first checks if the project exists and creates it if necessary, then adds the correction score for the user in the project.
- **Who**: This is designed for students (users) completing various projects, allowing scores to be added to both existing and new projects.
- **When**: The procedure runs each time a correction is added for a student in a project.

</details>

### Task 7: Average Score

In this task, we create a stored procedure `ComputeAverageScoreForUser` that calculates and stores the average score for a given user. The procedure takes a `user_id` as input and updates the corresponding user's `average_score` in the `users` table.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a SQL script that creates a stored procedure `ComputeAverageScoreForUser` to calculate the average score for a student.
- The procedure takes one input:
  - `user_id`: the `id` value from the `users` table, which is linked to an existing user.
- The `average_score` can be a decimal.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

#### 1. **7-init.sql**: Initialize the database with necessary tables (`users`, `projects`, `corrections`) and insert sample data.

```sql
-- Initial setup for users, projects, and corrections tables
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    average_score FLOAT DEFAULT 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user_id INT NOT NULL,
    project_id INT NOT NULL,
    score INT DEFAULT 0,
    KEY `user_id` (`user_id`),
    KEY `project_id` (`project_id`),
    CONSTRAINT fk_user_id FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT fk_project_id FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
);

-- Insert sample users and projects
INSERT INTO users (name) VALUES ("Bob");
INSERT INTO users (name) VALUES ("Jeanne");

INSERT INTO projects (name) VALUES ("C is fun");
INSERT INTO projects (name) VALUES ("Python is cool");

-- Insert corrections (scores) for users
INSERT INTO corrections (user_id, project_id, score) VALUES (1, 1, 80);
INSERT INTO corrections (user_id, project_id, score) VALUES (1, 2, 96);

INSERT INTO corrections (user_id, project_id, score) VALUES (2, 1, 91);
INSERT INTO corrections (user_id, project_id, score) VALUES (2, 2, 73);
```

- **Role**: This script sets up the initial tables and inserts sample data for testing the `ComputeAverageScoreForUser` procedure.

#### 2. **7-average_score.sql**: Create the stored procedure `ComputeAverageScoreForUser`.

```sql
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN input_user_id INT)
BEGIN
    DECLARE avg_score FLOAT;

    -- Calculate the average score for the given user
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = input_user_id;

    -- Update the user's average_score field
    UPDATE users
    SET average_score = avg_score
    WHERE id = input_user_id;
END //

DELIMITER ;
```

- **Role**: This procedure calculates the average score for a user based on their scores in the `corrections` table and updates the `average_score` field in the `users` table.
- **How It Works**:
  - The procedure takes `input_user_id` as input, calculates the average score from the `corrections` table for that user, and updates their `average_score` in the `users` table.
  - If a user has multiple corrections (scores), the procedure will average them, allowing for decimal values in the `average_score`.

#### 3. **7-main.sql**: Test the procedure by calculating the average score for a user and verifying the result.

```sql
-- Show and compute average score for a user
SELECT * FROM users;
SELECT * FROM corrections;

-- Calculate the average score for Jeanne
CALL ComputeAverageScoreForUser((SELECT id FROM users WHERE name = "Jeanne"));

-- Display the updated average score
SELECT "--";
SELECT * FROM users;
```

- **Role**: This script tests the functionality of the stored procedure by calculating and displaying the average score for a specific user (in this case, Jeanne).

</details>

<details>
  <summary><strong>Testing and Usage</strong></summary>

1. **Run the Initialization Script**:
   Create the `users`, `projects`, and `corrections` tables and insert some initial data by running the `7-init.sql` script:

   ```bash
   cat 7-init.sql | mysql -uroot -p holberton
   ```

   Verify that the data has been inserted:

   ```bash
   echo "SELECT * FROM users;" | mysql -uroot -p holberton
   echo "SELECT * FROM corrections;" | mysql -uroot -p holberton
   ```

   **Expected Output**:
   ```
   id      name    average_score
   1       Bob     0
   2       Jeanne  0

   user_id project_id      score
   1       1       80
   1       2       96
   2       1       91
   2       2       73
   ```

2. **Create the Stored Procedure**:
   Run the `7-average_score.sql` script to create the `ComputeAverageScoreForUser` procedure:

   ```bash
   cat 7-average_score.sql | mysql -uroot -p holberton
   ```

3. **Compute Average Score**:
   Run the `7-main.sql` script to calculate the average score for a user and verify the update:

   ```bash
   cat 7-main.sql | mysql -uroot -p holberton
   ```

   **Expected Output** (before and after calculating the average):
   ```
   id      name    average_score
   1       Bob     0
   2       Jeanne  0

   user_id project_id      score
   1       1       80
   1       2       96
   2       1       91
   2       2       73

   --

   id      name    average_score
   1       Bob     0
   2       Jeanne  82
   ```

   The average score for Jeanne is calculated as `(91 + 73) / 2 = 82`.

</details>

<details>
  <summary><strong>Troubleshooting</strong></summary>

#### Issue: **Average Score Not Updating**

At first, we encountered an issue where the average score was not being updated in the `users` table. This was due to an ambiguity between the input parameter `user_id` and the column `user_id` in the `corrections` table.

**Solution**: We renamed the input parameter from `user_id` to `input_user_id` to avoid confusion and ensure the correct column was referenced in the SQL query.

**Updated Code**:
```sql
CREATE PROCEDURE ComputeAverageScoreForUser(IN input_user_id INT)
BEGIN
    DECLARE avg_score FLOAT;

    -- Calculate the average score for the given user
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = input_user_id;

    -- Update the user's average_score field
    UPDATE users
    SET average_score = avg_score
    WHERE id = input_user_id;
END;
```

This resolved the issue, and the procedure now correctly updates the `average_score` for each user.

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: We created a stored procedure that calculates and updates the average score for a user based on their corrections.
- **Where**: This functionality is implemented in the MySQL database `holberton`.
- **Why**: Automatically calculating and updating average scores reduces manual data processing and ensures accuracy.
- **How**: The procedure calculates the average score by averaging the user's corrections in the `corrections` table, then updates the user's `average_score` field in the `users` table.
- **Who**: The procedure takes `input_user_id` as input and computes the average score for that user.
- **When**: The procedure is executed whenever you need to compute or update a user's average score.

</details>


### Task 8: Optimize Simple Search

In this task, we optimize a search query on a large dataset by creating an index on the first letter of the `name` column in the `names` table. This improves the performance of queries filtering by the first letter of the name, particularly for queries like `WHERE name LIKE 'a%'`.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a SQL script that creates an index on the table `names` for the first letter of the `name` column.
- This index should target only the first letter of each name, improving search performance for queries that search based on the first letter.
- Context: An index, when used appropriately, can significantly improve the performance of search queries.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

#### 1. **names.sql**: Import the large dataset

First, we need to import the provided `names.sql` dump into the MySQL database. This file contains a large dataset of names.

```bash
cat names.sql | mysql -uroot -p holberton
```

You can verify that the data was successfully loaded by counting the number of rows in the `names` table:

```bash
mysql -uroot -p holberton -e "SELECT COUNT(*) FROM names;"
```

**Expected Output**:
```
+----------+
| COUNT(*) |
+----------+
|  7894483 |
+----------+
```

#### 2. **Test search performance before adding the index**

In the MySQL prompt, run a query to count names starting with the letter 'a'. This will allow you to see the performance before adding the index:

```sql
SELECT COUNT(name) FROM names WHERE name LIKE 'a%';
```

**Expected Output** (This may take some time to execute):
```
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
```

**Time Taken**: Before indexing, the query could take around 2.8 seconds.

#### 3. **8-index_my_names.sql**: Create the index on the first letter of the `name` column

After testing the initial search performance, create an index that targets only the first letter of the `name` column to optimize the search query.

```bash
cat 8-index_my_names.sql | mysql -uroot -p holberton
```

The `8-index_my_names.sql` file should contain the following code:

```sql
-- In the vast sea of names, searching through every single one can feel like navigating without a map.
-- This index acts as our compass, pointing directly to names starting with the same letter.
-- By indexing only the first letter of the name column, we can swiftly narrow down the search,
-- making sure that queries no longer have to traverse the entire ocean of names.
-- It's like charting a course through the stars, efficient, quick, and focused on the first sign.
CREATE INDEX idx_name_first ON names (name(1));
```

#### 4. **Verify that the index was created**

After creating the index, verify its existence by running the following command in the MySQL prompt:

```sql
SHOW INDEX FROM names;
```

**Expected Output**:
```
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name       | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names |          1 | idx_name_first |            1 | name        | A         |          24 |        1 |   NULL | YES  | BTREE      |         |               |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
```

#### 5. **Test the search performance after adding the index**

Now that the index is in place, run the same query again to count the names starting with 'a' and observe the improvement in search time:

```sql
SELECT COUNT(name) FROM names WHERE name LIKE 'a%';
```

**Expected Output**:
```
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
```

**Time Taken**: The query should now execute much faster (in about 0.87 seconds, as opposed to the original 2.80 seconds).

#### 6. **Exit the MySQL prompt**

After completing the necessary steps, exit the MySQL shell:

```sql
exit;
```

</details>

<details>
  <summary><strong>Testing and Usage</strong></summary>

1. **Import the Dataset**:
   Import the `names.sql` file into the database to create the `names` table:

   ```bash
   cat names.sql | mysql -uroot -p holberton
   ```

   Verify the import by checking the number of rows in the `names` table:

   ```bash
   echo "SELECT COUNT(*) FROM names;" | mysql -uroot -p holberton
   ```

2. **Test Performance Without Index**:
   Before creating the index, run the search query to check how long it takes:

   ```bash
   mysql -uroot -p holberton -e "SELECT COUNT(name) FROM names WHERE name LIKE 'a%';"
   ```

   **Expected Output**:
   ```
   +-------------+
   | COUNT(name) |
   +-------------+
   |      302936 |
   +-------------+
   ```

   **Time Taken**: Approximately 2.8 seconds.

3. **Create the Index**:
   Run the `8-index_my_names.sql` script to create the index on the first letter of the `name` column:

   ```bash
   cat 8-index_my_names.sql | mysql -uroot -p holberton
   ```

4. **Test Performance with Index**:
   After creating the index, re-run the query to check for improved performance:

   ```bash
   mysql -uroot -p holberton -e "SELECT COUNT(name) FROM names WHERE name LIKE 'a%';"
   ```

   **Expected Output**:
   ```
   +-------------+
   | COUNT(name) |
   +-------------+
   |      302936 |
   +-------------+
   ```

   **Time Taken**: Approximately 0.87 seconds.

</details>

<details>
  <summary><strong>Troubleshooting</strong></summary>

#### Issue 1: **Running SQL commands in bash instead of MySQL**

- **Problem**: If you mistakenly run SQL commands like `CREATE INDEX` in the bash shell instead of the MySQL shell, you'll encounter errors like `bash: syntax error near unexpected token '('`.
- **Solution**: Make sure you're inside the MySQL interactive shell (`mysql -uroot -p holberton`) before running any SQL commands.

#### Issue 2: **Slow query performance due to large dataset**

- **Problem**: The dataset in `names.sql` is large, and searches for names using the `LIKE 'a%'` query are slow.
- **Solution**: By creating an index on the first letter of the `name` column, we optimize this search, reducing the query time significantly.

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: We created an index on the first letter of the `name` column in the `names` table to optimize search performance.
- **Where**: This optimization is implemented in the `names` table in the MySQL database `holberton`.
- **Why**: When searching large datasets, creating an index on commonly filtered columns can dramatically speed up query performance, making the process of finding specific data faster and more efficient.
- **How**: We created an index on the first letter of the `name` column using the `CREATE INDEX` statement, reducing the need for a full table scan during queries.
- **Who**: The `names` table stores the data, and the index improves the performance of queries run against this table.
- **When**: The index is created before performing search queries that filter by the first letter of the name, allowing for much faster query execution.

</details>

### Task 9: Optimize Search and Score

In this task, we create a composite index on the table `names` that indexes both the first letter of the `name` and the `score` column. This allows us to optimize search queries that filter by both the first letter of the name and the score.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a SQL script that creates an index `idx_name_first_score` on the table `names` based on the first letter of the `name` and the `score`.
- The goal is to optimize search queries that filter by both `name` (starting with a specific letter) and `score`.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

#### 1. **9-index_name_score.sql**: Create a composite index on the first letter of `name` and the `score`.

```sql
-- In a world full of names and numbers, searching through millions can be daunting.
-- This composite index is like a dual-filter: first, we narrow down by the initial letter,
-- and then, like a second lens, we refine the search by score.
-- By indexing both the first letter of the name and the score, we optimize our query,
-- allowing us to glide swiftly through the data and arrive at the desired results faster.
-- It's like zooming in with a high-powered telescope: focused and precise, no time wasted!
CREATE INDEX idx_name_first_score ON names (name(1), score);



```

- **Role**: This script creates a composite index on the `names` table, indexing both the first letter of `name` and the `score`.
- **How It Works**:
  - The index optimizes queries that filter based on both `name` (starting with a specific letter) and `score`.
  - It ensures that searches that involve filtering by both the first letter of the name and score run more efficiently.

</details>

<details>
  <summary><strong>Testing and Usage</strong></summary>

1. **Import the Database**:
   First, you need to import the table dump `names.sql`. This populates the `names` table with a large dataset:

   ```bash
   cat names.sql | mysql -uroot -p holberton
   ```

   After importing, you can verify the data by checking the table contents:

   ```bash
   mysql -uroot -p holberton
   ```

   Then, run:

   ```sql
   SELECT COUNT(*) FROM names;
   ```

   **Expected Output**:
   ```
   COUNT(*)
   7894483
   ```

2. **Create the Composite Index**:
   Run the `9-index_name_score.sql` script to create the index on the first letter of `name` and `score`:

   ```bash
   cat 9-index_name_score.sql | mysql -uroot -p holberton
   ```

3. **Verify the Index**:
   You can verify that the index has been created using the following MySQL command:

   ```sql
   SHOW INDEX FROM names;
   ```

   **Expected Output**:
   ```
   Table   Non_unique   Key_name             Seq_in_index   Column_name   Collation   Cardinality   Sub_part   Index_type
   names   1            idx_name_first_score 1              name          A           25            1          BTREE
   names   1            idx_name_first_score 2              score         A           3901          NULL       BTREE
   ```

4. **Test the Search Performance**:
   Now test a search query before and after creating the index:

   ```sql
   SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score < 80;
   ```

   **Before Creating the Index**:
   - The query took around **2.97 seconds** to run without the index.

   **After Creating the Index**:
   - The query runs much faster, reducing the time to around **0.36 seconds**.

   This demonstrates the significant performance improvement after creating the composite index.

</details>


<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: We created a composite index that optimizes queries filtering by both the first letter of the `name` and the `score`.
- **Where**: This functionality is implemented in the MySQL database `holberton`, on the `names` table.
- **Why**: Queries that filter by both name (starting with a letter) and score can be slow on large datasets. Creating this index drastically improves performance.
- **How**: The index optimizes the query by allowing MySQL to look up names by the first letter and score simultaneously, rather than searching the entire table.
- **Who**: The `names` table stores the `name` and `score` data, which is indexed by this composite index.
- **When**: The composite index is used every time a query searches for names starting with a specific letter and a specific score range.

</details>



### Task 10: Safe Divide

In this task, we create a function `SafeDiv` that safely divides two numbers, returning 0 if the divisor (`b`) is 0. This prevents any potential division-by-zero errors, which would result in `NULL` values in MySQL.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a SQL script that creates a function `SafeDiv` to divide two numbers safely.
- The function should take two arguments:
  - `a`: an integer (numerator).
  - `b`: an integer (denominator).
- If `b == 0`, the function should return 0. Otherwise, it should return `a / b`.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

#### 1. **10-init.sql**: Initialize the database with the necessary `numbers` table and insert sample data.

```sql
-- Initial setup for numbers table with sample data
DROP TABLE IF EXISTS numbers;

CREATE TABLE IF NOT EXISTS numbers (
    a INT DEFAULT 0,
    b INT DEFAULT 0
);

-- Insert sample data
INSERT INTO numbers (a, b) VALUES (10, 2), (4, 5), (2, 3), (6, 3), (7, 0), (6, 8);
```

- **Role**: This script sets up the initial table with pairs of numbers (`a`, `b`) to test the `SafeDiv` function.

#### 2. **10-div.sql**: Create the `SafeDiv` function.

```sql
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
```

- **Role**: This function safely divides two numbers and returns 0 if the denominator is 0. We declare it as `DETERMINISTIC` because for the same inputs, the result will always be the same.
- **How It Works**:
  - The function checks if `b` is 0. If true, it returns 0 to prevent division by zero.
  - Otherwise, it performs the division and returns the result.

#### 3. **10-main.sql**: Test the function by selecting the results of `SafeDiv` on the `numbers` table.

```sql
-- Show the results of the SafeDiv function on the numbers table
SELECT SafeDiv(a, b) FROM numbers;
```

- **Role**: This script tests the `SafeDiv` function by applying it to the values in the `numbers` table.

</details>

<details>
  <summary><strong>Testing and Usage</strong></summary>

1. **Run the Initialization Script**:
   Set up the `numbers` table and insert sample data by running the `10-init.sql` script:

   ```bash
   cat 10-init.sql | mysql -uroot -p holberton
   ```

   Verify the data has been inserted:

   ```bash
   echo "SELECT * FROM numbers;" | mysql -uroot -p holberton
   ```

   **Expected Output**:
   ```
   a       b
   10      2
   4       5
   2       3
   6       3
   7       0
   6       8
   ```

2. **Create the Function**:
   Run the `10-div.sql` script to create the `SafeDiv` function:

   ```bash
   cat 10-div.sql | mysql -uroot -p holberton
   ```

3. **Test SafeDiv Function**:
   Run the following query to test the function on the `numbers` table:

   ```bash
   echo "SELECT SafeDiv(a, b) FROM numbers;" | mysql -uroot -p holberton
   ```

   **Expected Output**:
   ```
   SafeDiv(a, b)
   5
   0.8
   0.666667
   2
   0
   0.75
   ```

</details>

 
<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: We created a function to safely divide two numbers, returning 0 if the divisor is 0.
- **Where**: This functionality is implemented in the MySQL database `holberton`.
- **Why**: Division by zero leads to `NULL` results, which can cause issues in queries and calculations.
- **How**: The function checks whether the divisor is 0 and returns 0 if so; otherwise, it performs the division and returns the result.
- **Who**: The function takes two arguments (`a` and `b`), which represent the numerator and the denominator.
- **When**: The function is executed whenever you need to divide two numbers safely.

</details>

### Task 11: No Table for a Meeting

In this task, we create a SQL view `need_meeting` that lists students who need a meeting based on two criteria:
1. Their score is strictly under 80.
2. They have either no `last_meeting` date or their last meeting was more than a month ago.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a SQL script that creates a view `need_meeting` listing students who need a meeting.
- The criteria for being listed are:
  1. Their `score` is below 80.
  2. Their `last_meeting` date is either `NULL` or more than one month old.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

#### 1. **11-init.sql**: Set up the students table and insert initial data.

```sql
-- Initial setup for the students table
DROP TABLE IF EXISTS students;

CREATE TABLE IF NOT EXISTS students (
    name VARCHAR(255) NOT NULL,
    score INT DEFAULT 0,
    last_meeting DATE NULL
);

-- Insert sample students
INSERT INTO students (name, score) VALUES ('Bob', 80);
INSERT INTO students (name, score) VALUES ('Sylvia', 120);
INSERT INTO students (name, score) VALUES ('Jean', 60);
INSERT INTO students (name, score) VALUES ('Steeve', 50);
INSERT INTO students (name, score) VALUES ('Camilia', 80);
INSERT INTO students (name, score) VALUES ('Alexa', 130);
```

- **Role**: This script creates the `students` table and populates it with sample student data, including `name`, `score`, and `last_meeting` date.

#### 2. **11-need_meeting.sql**: Create the `need_meeting` view.

```sql
-- Create the view need_meeting to identify students who need a meeting
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < ADDDATE(CURDATE(), INTERVAL -1 MONTH));
```

- **Role**: This view selects students whose `score` is under 80 and either have no `last_meeting` date or had a meeting more than a month ago.
- **How It Works**: The `WHERE` clause filters students based on the score and the time since their last meeting. If the `last_meeting` is `NULL` or more than a month old, the student will be included in the `need_meeting` view.

#### 3. **11-main.sql**: Test the view to ensure it works as expected.

```sql
-- Test the need_meeting view
SELECT * FROM need_meeting;

-- Adjust the score of Bob to fall below 80
UPDATE students SET score = 40 WHERE name = 'Bob';
SELECT * FROM need_meeting;

-- Adjust Steeve's score to 80, so he should be excluded
UPDATE students SET score = 80 WHERE name = 'Steeve';
SELECT * FROM need_meeting;

-- Update Jean's last meeting date to today, so he should be excluded
UPDATE students SET last_meeting = CURDATE() WHERE name = 'Jean';
SELECT * FROM need_meeting;

-- Set Jean's last meeting to more than 1 month ago, so he should be included again
UPDATE students SET last_meeting = ADDDATE(CURDATE(), INTERVAL -2 MONTH) WHERE name = 'Jean';
SELECT * FROM need_meeting;

-- Show the view's definition
SHOW CREATE VIEW need_meeting;

-- Show the students table structure
SHOW CREATE TABLE students;
```

- **Role**: This script tests the `need_meeting` view by selecting data, modifying student scores, and adjusting `last_meeting` dates to verify the correct functionality of the view.

</details>

<details>
  <summary><strong>Testing and Usage</strong></summary>

1. **Run the Initialization Script**:
   First, create the `students` table and insert the initial data by running the `11-init.sql` script:

   ```bash
   cat 11-init.sql | mysql -uroot -p holberton
   ```

   Verify the data:

   ```bash
   echo "SELECT * FROM students;" | mysql -uroot -p holberton
   ```

   **Expected Output**:
   ```
   name    score   last_meeting
   Bob     80      NULL
   Sylvia  120     NULL
   Jean    60      NULL
   Steeve  50      NULL
   Camilia 80      NULL
   Alexa   130     NULL
   ```

2. **Create the View**:
   Run the `11-need_meeting.sql` script to create the view:

   ```bash
   cat 11-need_meeting.sql | mysql -uroot -p holberton
   ```

3. **Test the View**:
   Run the `11-main.sql` script to test the view:

   ```bash
   cat 11-main.sql | mysql -uroot -p holberton
   ```

   **Expected Output**:
   The view will return the list of students meeting the criteria at different stages:
   ```
   name
   Jean
   Steeve

   --

   name
   Bob
   Jean
   Steeve

   --

   name
   Bob
   Jean

   --

   name
   Bob
   ```

4. **Verify View and Table Definitions**:
   The view and table definitions can be viewed using:

   ```bash
   SHOW CREATE VIEW need_meeting;
   SHOW CREATE TABLE students;
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: We created a view to list students who need a meeting based on their scores and last meeting dates.
- **Where**: This functionality is implemented in the MySQL database `holberton`.
- **Why**: Regular meetings help keep students on track, especially those with lower scores or those who haven't met with their instructors recently.
- **How**: The `need_meeting` view filters students whose scores are below 80 and either have no recent meeting or no meeting at all.
- **Who**: The `students` table holds data on each student's name, score, and the date of their last meeting.
- **When**: The view will be updated dynamically whenever the students' scores or meeting dates change.

</details>

### Task 12: Average Weighted Score

In this task, we create a stored procedure `ComputeAverageWeightedScoreForUser` that calculates and stores the average weighted score for a given user. The weighted average is calculated by taking into account both the score for each project and the weight assigned to the project.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a SQL script that creates a stored procedure `ComputeAverageWeightedScoreForUser` to calculate the average weighted score for a student.
- The procedure takes one input:
  - `user_id`: the `id` value from the `users` table, which is linked to an existing user.
- The weighted average is calculated by multiplying each project's score by its weight, summing the results, and dividing by the total weight.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

#### 1. **100-init.sql**: Initialize the database with necessary tables (`users`, `projects`, `corrections`) and insert sample data.

```sql
-- Initial setup for users, projects, and corrections tables
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    average_score FLOAT DEFAULT 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    weight INT DEFAULT 1,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user_id INT NOT NULL,
    project_id INT NOT NULL,
    score FLOAT DEFAULT 0,
    KEY `user_id` (`user_id`),
    KEY `project_id` (`project_id`),
    CONSTRAINT fk_user_id FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT fk_project_id FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
);

-- Insert sample users and projects
INSERT INTO users (name) VALUES ("Bob");
INSERT INTO users (name) VALUES ("Jeanne");

-- Insert sample projects with weights
INSERT INTO projects (name, weight) VALUES ("C is fun", 1);
INSERT INTO projects (name, weight) VALUES ("Python is cool", 2);

-- Insert corrections (scores) for users
INSERT INTO corrections (user_id, project_id, score) VALUES (1, 1, 80);
INSERT INTO corrections (user_id, project_id, score) VALUES (1, 2, 96);

INSERT INTO corrections (user_id, project_id, score) VALUES (2, 1, 91);
INSERT INTO corrections (user_id, project_id, score) VALUES (2, 2, 73);
```

- **Role**: This script sets up the initial tables and inserts sample data for testing the `ComputeAverageWeightedScoreForUser` procedure.

#### 2. **100-average_weighted_score.sql**: Create the stored procedure `ComputeAverageWeightedScoreForUser`.

```sql
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
```

- **Role**: This procedure calculates the average weighted score for a user based on their scores in the `corrections` table and the weight of each project in the `projects` table.
- **How It Works**:
  - The procedure takes `input_user_id` as input, multiplies each project's score with its weight, sums them up, and divides by the total weight of the projects. The result is then used to update the user's `average_score` in the `users` table.

#### 3. **100-main.sql**: Test the procedure by calculating the average weighted score for a user and verifying the result.

```sql
-- Show and compute average weighted score for a user
SELECT * FROM users;
SELECT * FROM projects;
SELECT * FROM corrections;

-- Calculate the average weighted score for Jeanne
CALL ComputeAverageWeightedScoreForUser((SELECT id FROM users WHERE name = "Jeanne"));

-- Display the updated average weighted score
SELECT "--";
SELECT * FROM users;
```

- **Role**: This script tests the functionality of the stored procedure by calculating and displaying the weighted average score for a specific user (in this case, Jeanne).

</details>

<details>
  <summary><strong>Testing and Usage</strong></summary>

1. **Run the Initialization Script**:
   Create the `users`, `projects`, and `corrections` tables and insert some initial data by running the `100-init.sql` script:

   ```bash
   cat 100-init.sql | mysql -uroot -p holberton
   ```

   Verify that the data has been inserted:

   ```bash
   echo "SELECT * FROM users;" | mysql -uroot -p holberton
   echo "SELECT * FROM projects;" | mysql -uroot -p holberton
   echo "SELECT * FROM corrections;" | mysql -uroot -p holberton
   ```

   **Expected Output**:
   ```
   id      name    average_score
   1       Bob     0
   2       Jeanne  0

   id      name    weight
   1       C is fun        1
   2       Python is cool  2

   user_id project_id      score
   1       1       80
   1       2       96
   2       1       91
   2       2       73
   ```

2. **Create the Stored Procedure**:
   Run the `100-average_weighted_score.sql` script to create the `ComputeAverageWeightedScoreForUser` procedure:

   ```bash
   cat 100-average_weighted_score.sql | mysql -uroot -p holberton
   ```

3. **Compute Average Weighted Score**:
   Run the `100-main.sql` script to calculate the weighted average score for a user and verify the update:

   ```bash
   cat 100-main.sql | mysql -uroot -p holberton
   ```

   **Expected Output** (before and after calculating the weighted average):
   ```
   id      name    average_score
   1       Bob     0
   2       Jeanne  0

   user_id project_id      score
   1       1       80
   1       2       96
   2       1       91
   2       2       73

   --

   id      name    average_score
   1       Bob     0
   2       Jeanne  79
   ```

   The weighted average score for Jeanne is calculated as:
   - (91 * 1 + 73 * 2) / (1 + 2) = (91 + 146) / 3 = 237 / 3 = 79

</details>


<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: We created a stored procedure that calculates and updates the average weighted score for a user based on their project scores and the weight of each project.
- **Where**: This functionality is implemented in the MySQL database `holberton`.
- **Why**: Weighted scores provide a more accurate representation of a user's performance by considering the relative importance (weight) of each project.
- **How**: The procedure calculates the weighted average by multiplying each score with the project’s weight, summing the results, and dividing by the total weight of the projects.
- **Who**: The procedure takes `input_user_id` as input and computes the weighted average score for that user.
- **When**: The procedure is executed whenever you need to compute or update a user's weighted average score.

</details>

### Task 13: Average Weighted Score for All

In this task, we create a stored procedure `ComputeAverageWeightedScoreForUsers` that calculates and stores the average weighted score for all users. The weighted average is calculated by taking into account both the score for each project and the weight assigned to the project, for every user in the `users` table.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a SQL script that creates a stored procedure `ComputeAverageWeightedScoreForUsers` to calculate the average weighted score for all students.
- The procedure does not take any input.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

#### 1. **101-init.sql**: Initialize the database with necessary tables (`users`, `projects`, `corrections`) and insert sample data.

```sql
-- Initial setup for users, projects, and corrections tables
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    average_score FLOAT DEFAULT 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    weight INT DEFAULT 1,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user_id INT NOT NULL,
    project_id INT NOT NULL,
    score FLOAT DEFAULT 0,
    KEY `user_id` (`user_id`),
    KEY `project_id` (`project_id`),
    CONSTRAINT fk_user_id FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT fk_project_id FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
);

-- Insert sample users and projects
INSERT INTO users (name) VALUES ("Bob");
INSERT INTO users (name) VALUES ("Jeanne");

-- Insert sample projects with weights
INSERT INTO projects (name, weight) VALUES ("C is fun", 1);
INSERT INTO projects (name, weight) VALUES ("Python is cool", 2);

-- Insert corrections (scores) for users
INSERT INTO corrections (user_id, project_id, score) VALUES (1, 1, 80);
INSERT INTO corrections (user_id, project_id, score) VALUES (1, 2, 96);

INSERT INTO corrections (user_id, project_id, score) VALUES (2, 1, 91);
INSERT INTO corrections (user_id, project_id, score) VALUES (2, 2, 73);
```

- **Role**: This script sets up the initial tables and inserts sample data for testing the `ComputeAverageWeightedScoreForUsers` procedure.

#### 2. **101-average_weighted_score.sql**: Create the stored procedure `ComputeAverageWeightedScoreForUsers`.

```sql
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
```

- **Role**: This procedure iterates over all users, calculating the average weighted score for each user and updating their `average_score` field in the `users` table.
- **How It Works**:
  - The procedure uses a cursor to loop through each user in the `users` table.
  - For each user, the `ComputeAverageWeightedScoreForUser` procedure is called to calculate their weighted average score.

#### 3. **101-main.sql**: Test the procedure by calculating the average weighted score for all users and verifying the result.

```sql
-- Show and compute average weighted score for all users
SELECT * FROM users;
SELECT * FROM projects;
SELECT * FROM corrections;

-- Calculate the average weighted score for all users
CALL ComputeAverageWeightedScoreForUsers();

-- Display the updated average weighted scores
SELECT "--";
SELECT * FROM users;
```

- **Role**: This script tests the functionality of the stored procedure by calculating and displaying the weighted average scores for all users.

</details>

<details>
  <summary><strong>Testing and Usage</strong></summary>

1. **Run the Initialization Script**:
   Create the `users`, `projects`, and `corrections` tables and insert some initial data by running the `101-init.sql` script:

   ```bash
   cat 101-init.sql | mysql -uroot -p holberton
   ```

   Verify that the data has been inserted:

   ```bash
   echo "SELECT * FROM users;" | mysql -uroot -p holberton
   echo "SELECT * FROM projects;" | mysql -uroot -p holberton
   echo "SELECT * FROM corrections;" | mysql -uroot -p holberton
   ```

   **Expected Output**:
   ```
   id      name    average_score
   1       Bob     0
   2       Jeanne  0

   id      name    weight
   1       C is fun        1
   2       Python is cool  2

   user_id project_id      score
   1       1       80
   1       2       96
   2       1       91
   2       2       73
   ```

2. **Create the Stored Procedure**:
   Run the `101-average_weighted_score.sql` script to create the `ComputeAverageWeightedScoreForUsers` procedure:

   ```bash
   cat 101-average_weighted_score.sql | mysql -uroot -p holberton
   ```

3. **Compute Average Weighted Score for All Users**:
   Run the `101-main.sql` script to calculate the weighted average scores for all users and verify the update:

   ```bash
   cat 101-main.sql | mysql -uroot -p holberton
   ```

   **Expected Output** (before and after calculating the weighted average):
   ```
   id      name    average_score
   1       Bob     0
   2       Jeanne  0

   user_id project_id      score
   1       1       80
   1       2       96
   2       1       91
   2       2       73

   --

   id      name    average_score
   1       Bob     90.6667
   2       Jeanne  79
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: We created a stored procedure that calculates and updates the average weighted score for all users.
- **Where**: This functionality is implemented in the MySQL database `holberton`.
- **Why**: It automates the calculation of average weighted scores for all users, ensuring data accuracy across all users.
- **How**: The procedure loops through each user in the `users` table, calculates their weighted average score using their project scores and project weights, and updates their `average_score` field.
- **Who**: The procedure does not take any input, as it calculates the weighted average for every user.
- **When**: The procedure is executed whenever you need to compute or update all users' weighted average scores.

</details>
