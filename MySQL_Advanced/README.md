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
