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
