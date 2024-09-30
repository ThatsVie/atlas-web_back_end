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

### Explanation: Who, What, Where, When, Why, How

- **What**: We created a `users` table with three fields: `id`, `email`, and `name`. Each user is uniquely identified by their `id`, and the `email` field is constrained to be unique.
- **Where**: This is performed in a MySQL database (`holberton`).
- **Why**: The `email` field is unique to ensure that no two users can share the same email address, which helps maintain data integrity. The `id` field is the primary key to uniquely identify each user.
- **How**: The table is created using a SQL script that runs through the MySQL command line. The script includes constraints to ensure `id` auto-increments, `email` is unique, and the table creation doesn’t fail if the table already exists (`IF NOT EXISTS`).
- **Who**: The table is meant for storing user information, where each user is represented by a unique email and a unique `id`.
- **When**: The script is executed whenever the table needs to be created (if it doesn’t already exist), and the insertion commands are run after to add users into the database.

</details>
