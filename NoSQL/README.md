<div align="center">
    <img src="https://github.com/user-attachments/assets/5d3681e0-7f0e-4767-be0b-8b9c3f7a8308" alt="NOSQLPuggy" />
    <p>This project demonstrates the use of MongoDB, a NoSQL database, to perform essential CRUD operations via both the MongoDB shell and Python's pymongo library. It includes scripts for inserting, updating, querying, and analyzing documents in MongoDB collections, such as processing and analyzing Nginx logs. The project showcases practical techniques for integrating Python with MongoDB to manage data efficiently and perform advanced queries.</p>
</div>

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Step-by-Step Walkthrough: Installing MongoDB 4.4 on Ubuntu 20.04 (What Worked for Me)](#step-by-step-walkthrough-installing-mongodb-44-on-ubuntu-2004-what-worked-for-me)
- [Tasks and Usage](#tasks-and-usage)
  - [Task 0: List all databases](#task-0-list-all-databases)
  - [Task 1: Create or Use the Database](#task-1-create-or-use-the-database)
  - [Task 2: Insert Document](#task-2-insert-document)
  - [Task 3: All Documents](#task-3-all-documents)
  - [Task 4: All Matches](#task-4-all-matches)
  - [Task 5: Count Documents](#task-5-count-documents)
  - [Task 6: Update Document](#task-6-update-document)
  - [Task 7: Delete by Match](#task-7-delete-by-match)
  - [Task 8: List All Documents in Python](#task-8-list-all-documents-in-python)
  - [Task 9: Insert a Document in Python](#task-9-insert-a-document-in-python)
  - [Task 10: Change School Topics in Python](#task-10-change-school-topics-in-python)
  - [Task 11: Where can I learn Python?](#task-11-where-can-i-learn-python)
  - [Task 12: Log Stats](#task-12-log-stats)


## Resources

- [NoSQL Databases Explained](https://riak.com/resources/nosql-databases/)
- [What is NoSQL ? (YouTube)](https://www.youtube.com/watch?v=qUV2j3XBRHc)
- [MongoDB with Python Crash Course](https://www.youtube.com/watch?v=E-1xI85Zog8)
- [MongoDB Tutorial 2: Insert, Update, Remove, Query](https://www.youtube.com/watch?v=CB9G5Dvv-EE)
- [Aggregation in MongoDB](https://www.mongodb.com/docs/manual/aggregation/)
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
- [mongo Shell Methods](https://www.mongodb.com/docs/manual/reference/method/)
- [The mongo Shell](https://www.mongodb.com/docs/mongodb-shell/)



## Learning Objectives

<details>
  <summary><strong>What NoSQL means (hint: it's not "not SQL")</strong></summary>

NoSQL stands for "Not Only SQL" and refers to a type of database that is designed to handle large volumes of structured, semi-structured, or unstructured data. Unlike SQL databases that rely on fixed schemas and relational tables, NoSQL databases offer flexibility by using various data models such as document, key-value, graph, and column-based storage. 

**Relevant Tasks**: 
- **Task 0**: The use of MongoDB as a NoSQL database is introduced, showcasing flexibility in storing unstructured data without needing a predefined schema.
</details>



<details>
  <summary><strong>Differences between SQL and NoSQL (the relational chaos vs. the document freedom)</strong></summary>

SQL databases are relational, structured, and use tables with fixed schemas, where JOIN operations are often necessary to retrieve related data across tables. NoSQL databases like MongoDB offer document storage, where data is stored in a more flexible JSON-like format (BSON in MongoDB), making it easier to store and retrieve nested or complex data structures.

**Relevant Tasks**: 
- **Task 3**: Demonstrates querying documents in MongoDB without complex JOIN operations.
- **Task 9**: Shows how a document is inserted into a NoSQL database without predefined schemas, exemplifying document freedom.
</details>



<details>
  <summary><strong>What ACID is and why NoSQL databases sometimes play it fast and loose with those rules</strong></summary>

ACID (Atomicity, Consistency, Isolation, Durability) is a set of properties for reliable database transactions. While SQL databases strictly adhere to ACID, NoSQL databases like MongoDB sometimes trade off certain ACID guarantees (e.g., consistency for availability and partition tolerance in distributed environments) to optimize performance and scalability.

**Relevant Tasks**: 
- **Task 6**: The update operation shows MongoDB’s handling of atomicity and consistency within document-level updates.
- **Task 10**: Involves updating multiple documents, hinting at the trade-offs between consistency and performance in distributed systems.
</details>



<details>
  <summary><strong>What document storage is and why you won’t need 10 different JOINs to find that one piece of data</strong></summary>

Document storage, as seen in MongoDB, allows entire data structures (documents) to be stored in a single collection. This avoids the need for complex JOIN operations that are required in relational databases to gather related information from different tables.

**Relevant Tasks**:
- **Task 4**: Retrieving documents based on a specific field (name), highlighting the ease of document retrieval.
- **Task 7**: Deleting documents based on a condition showcases document-level operations without relying on relational table links.
</details>



<details>
  <summary><strong>Types of NoSQL databases</strong></summary>

There are four primary types of NoSQL databases: 
1. Document databases (e.g., MongoDB)
2. Key-value stores
3. Column-family stores
4. Graph databases

**Relevant Tasks**:
- **Task 0**: Focuses on MongoDB, a document-based NoSQL database.
- **Task 9**: Involves inserting documents into MongoDB, showing the functionality of document stores.
</details>



<details>
  <summary><strong>Benefits of NoSQL databases in a world that increasingly feels like it's spiraling out of control</strong></summary>

NoSQL databases offer flexibility, scalability, and the ability to handle large volumes of unstructured or semi-structured data, making them suitable for modern applications with dynamic and rapidly changing data requirements. They are optimized for horizontal scaling, fault tolerance, and performance in distributed environments.

**Relevant Tasks**:
- **Task 12**: Shows how MongoDB is used to store and analyze large-scale log data, demonstrating its scalability and efficiency.
</details>



<details>
  <summary><strong>How to query, insert, update, and delete data in MongoDB like a responsible adult who doesn't accidentally drop entire databases</strong></summary>

MongoDB allows easy CRUD operations (Create, Read, Update, Delete) on documents in collections, with commands designed to be intuitive yet powerful.

**Relevant Tasks**:
- **Task 1**: Demonstrates creating or using a database.
- **Task 2**: Involves inserting a new document.
- **Task 4**: Involves querying specific documents.
- **Task 6**: Shows how to update documents.
- **Task 7**: Covers deletion of documents.
</details>



<details>
  <summary><strong>How to use MongoDB effectively, even if you’re still wondering whether SQL will ever forgive you</strong></summary>

MongoDB is effective for use cases where structured, unstructured, or semi-structured data must be managed at scale with flexibility. By avoiding rigid schemas and complex JOINs, it allows for rapid development, efficient scaling, and ease of integration with modern applications.

**Relevant Tasks**:
- **Task 0-12**: Cover various MongoDB operations like inserting, updating, deleting, and querying data, as well as handling large datasets like logs (Task 12).
</details>


## Requirements

 <details>
<summary> <strong>MongoDB Command Files</strong></summary>

- Files must be interpreted/compiled on Ubuntu 20.04 LTS using MongoDB (version 4.4).
- Each file should end with a new line (yes, really).
- The first line of every file must be a comment (`// my comment`).
- A `README.md` file, like this one, is mandatory (you’ve come to the right place!).
- The length of files will be tested using `wc`.
</details>

<details>
<summary> <strong>Python Scripts</strong></summary>

- Files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.9 and PyMongo 4.8.0.
- Each file should end with a new line.
- The first line must be `#!/usr/bin/env python3` (so the interpreter knows what’s up).
- Follow `pycodestyle` (version 2.5.*) like a sacred text.
- All functions and modules must be documented.
- Make sure your code doesn’t execute when imported (that’s what `if __name__ == "__main__":` is for).
  </details>

## Step-by-Step Walkthrough: Installing MongoDB 4.4 on Ubuntu 20.04 (What Worked for Me)
<details>
<summary> <strong>This is the detailed process that worked for me while installing MongoDB 4.4 on Ubuntu 20.04, especially resolving issues related to `libssl1.1` dependencies. If you're following along, keep in mind that your system setup may differ, and minor adjustments could be necessary.</strong></summary>

### 1. Install Prerequisites
MongoDB requires `gnupg` and `curl` to manage keys and repositories. Run the following commands to ensure these are installed:

```bash
sudo apt-get install gnupg curl
```

### 2. Import MongoDB Public GPG Key
To verify the MongoDB packages, I imported the public GPG key using the command below:

```bash
curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-4.4.gpg --dearmor
```

### 3. Create the MongoDB Source List
Next, I created a MongoDB source list to add the repository for Ubuntu 20.04:

```bash
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-4.4.gpg ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
```

### 4. Reload Local Package Database
I refreshed the package manager to recognize the newly added MongoDB repository:

```bash
sudo apt-get update
```

### 5. Install `libssl1.1`
MongoDB 4.4 depends on `libssl1.1`, which is no longer in the default repositories. Here's how I manually installed `libssl1.1`:

```bash
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2_amd64.deb
```

### 6. Install MongoDB
Once `libssl1.1` was installed, I proceeded to install MongoDB:

```bash
sudo apt-get install -y mongodb-org
```

### 7. Start MongoDB
After installation, I started MongoDB by running:

```bash
sudo systemctl start mongod
```

### 8. Enable MongoDB to Start on Boot
To ensure MongoDB starts automatically after a reboot, I enabled it with:

```bash
sudo systemctl enable mongod
```

### 9. Verify MongoDB Installation
Finally, I verified that MongoDB was working by running the MongoDB shell:

```bash
mongo
```

This opened the MongoDB shell, confirming the installation was successful.
</details>


## Tasks and Usage

### Task 0: List all databases

In this task, we write a script that lists all the databases in MongoDB using the `show dbs` command.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a script that lists all databases in MongoDB.

**Example Output**:
```bash
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
admin        0.000GB
config       0.000GB
local        0.000GB
logs         0.005GB
bye
```

</details>


<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create the Script**:  
   Inside the `NoSQL` directory, create a new file `0-list_databases` with the following code:

   ```bash
   // Script to list all databases in MongoDB
   show dbs
   ```

2. **Running the Script**:  
   Run the script by executing the following command:

   ```bash
   mongo < 0-list_databases
   ```

3. **Expected Output**:  
   After running the script, MongoDB will return a list of all available databases along with their sizes:

   ```bash
   MongoDB shell version v4.4.29
   connecting to: mongodb://127.0.0.1:27017
   admin        0.000GB
   config       0.000GB
   local        0.000GB
   logs         0.005GB
   bye
   ```

</details>


<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: This task involves writing a MongoDB shell script to list all databases available on the MongoDB server.
- **Where**: The script is executed within the MongoDB shell via the terminal.
- **Why**: It helps the user get a quick overview of all available databases and their sizes.
- **How**: We use the `show dbs` command in MongoDB to list databases.
- **Who**: Anyone connected to the MongoDB server can run this script.
- **When**: This script can be executed anytime MongoDB is running and connected.

</details>



<details>
  <summary><strong>Testing and Usage</strong></summary>

1. **Ensure MongoDB is Running**:  
   Before running the script, make sure the MongoDB service is running:
   
   ```bash
   sudo systemctl start mongod
   ```

2. **Run the Script**:  
   Run the script using:
   
   ```bash
   mongo < 0-list_databases
   ```

3. **Check the Output**:  
   The script will output all databases and their sizes.

</details>

### Task 1: Create or Use the Database

This task creates or switches to the database named `my_db` in MongoDB. If the database does not exist, it will be created.


<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a script that creates or uses the database my_db:
**Example Output**:
```bash
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
switched to db my_db
bye
```

</details>


<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create the Script**:  
   In the `NoSQL` directory, create the file `1-use_or_create_database` with the following content:

   ```bash
   // Script to create or use the database my_db
   use my_db
   ```

2. **Run the Script**:  
   Run the script with the following command:

   ```bash
   mongo < 1-use_or_create_database
   ```

3. **Expected Output**:  
   MongoDB will either switch to the `my_db` database or create it if it doesn't exist:

   ```bash
   MongoDB shell version v4.4.29
   connecting to: mongodb://127.0.0.1:27017
   switched to db my_db
   bye
   ```

</details>


<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: The task involves creating or switching to the database `my_db`.
- **Where**: It’s executed within the MongoDB shell.
- **Why**: The `use` command allows you to create or switch to a specific database, and if the database doesn’t exist, MongoDB creates it automatically.
- **How**: By running `use my_db`, MongoDB either switches to the database or creates it if it's not present.
- **Who**: Any user with access to the MongoDB instance can run this script.
- **When**: This script is used whenever the database `my_db` is needed or if you want to create it.

</details>


<details>
  <summary><strong>Testing and Usage</strong></summary>

1. **Ensure MongoDB is Running**:  
   Ensure MongoDB is running before executing the script:
   
   ```bash
   sudo systemctl start mongod
   ```

2. **Run the Script**:  
   Run the script using:
   
   ```bash
   mongo < 1-use_or_create_database
   ```

3. **Check the Output**:  
   MongoDB will switch to `my_db` or create it if it doesn’t exist.

</details>


### Task 2: Insert Document

This task involves writing a script that inserts a document into the `school` collection. The document must have one attribute `name` with the value `"Holberton school"`. The database name will be passed as an option when running the script.


<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a script that inserts a document into the collection `school`.
- The document must contain an attribute `name` with the value `"Holberton school"`.
- The database name will be passed as an option to the MongoDB command.

**Example Output**:
```bash
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
WriteResult({ "nInserted" : 1 })
bye
```

</details>


<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create the Script**:  
   Inside the `NoSQL` directory, create a new file `2-insert` with the following content:

   ```bash
   // Script to insert a document into the collection "school"
   db.school.insert({
       name: "Holberton school"
   })
   ```

2. **Run the Script**:  
   To execute the script and insert the document into the `school` collection, run:

   ```bash
   mongo my_db < 2-insert
   ```

3. **Expected Output**:  
   You should see the following output confirming the insertion of the document:

   ```bash
   MongoDB shell version v4.4.29
   connecting to: mongodb://127.0.0.1:27017/my_db
   WriteResult({ "nInserted" : 1 })
   bye
   ```

</details>


<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: This task involves inserting a document into the `school` collection with an attribute `name` set to `"Holberton school"`.
- **Where**: The script is executed in the MongoDB shell via the terminal.
- **Why**: Inserting a document into a collection is a fundamental operation in MongoDB to store data.
- **How**: The `db.school.insert()` command inserts a document into the `school` collection. If the collection does not exist, MongoDB creates it.
- **Who**: Any user with access to the MongoDB server can run this script.
- **When**: This script can be executed anytime MongoDB is running and connected to the local server.

</details>


<details>
  <summary><strong>Testing and Usage</strong></summary>

1. **Ensure MongoDB is Running**:  
   Make sure MongoDB is running by checking the service status or starting it with:
   
   ```bash
   sudo systemctl start mongod
   ```

2. **Run the Script**:  
   Run the script using:
   
   ```bash
   mongo my_db < 2-insert
   ```

3. **Verify the Insertion**:  
   To verify the insertion, you can run the following command in the MongoDB shell to see if the document was inserted:
   
   ```bash
   mongo my_db
   db.school.find()
   ```

</details>

### Task 3: All Documents

This task involves writing a script that lists all documents in the `school` collection. The database name will be passed as an option when running the script.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a script that lists all documents in the `school` collection.
- The database name will be passed as an option to the MongoDB command.

**Example Output**:
```bash
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
{ "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school" }
bye
```

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create the Script**:  
   Inside the `NoSQL` directory, create a new file `3-all` with the following content:

   ```bash
   // Script to list all documents in the collection "school"
   db.school.find().pretty()
   ```

2. **Run the Script**:  
   To execute the script and list all documents in the `school` collection, run:

   ```bash
   mongo my_db < 3-all
   ```

3. **Expected Output**:  
   You should see the following output showing all documents in the `school` collection:

   ```bash
   MongoDB shell version v4.4.29
   connecting to: mongodb://127.0.0.1:27017/my_db
   { "_id" : ObjectId("66fc82c5704aecaa129d2b2e"), "name" : "Holberton school" }
   { "_id" : ObjectId("66fc89283a5f1925aeab1436"), "name" : "Holberton school" }
   bye
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: This task involves listing all documents from the `school` collection using a script.
- **Where**: The script is executed in the MongoDB shell via the terminal.
- **Why**: Listing documents from a collection is a common query operation in MongoDB to view stored data.
- **How**: The `db.school.find().pretty()` command lists all documents in the `school` collection in a formatted output for readability.
- **Who**: Any user with access to the MongoDB server can run this script.
- **When**: This script can be executed anytime MongoDB is running and connected to the local server.

</details>

<details>
  <summary><strong>Testing and Usage</strong></summary>

1. **Ensure MongoDB is Running**:  
   Make sure MongoDB is running by checking the service status or starting it with:
   
   ```bash
   sudo systemctl start mongod
   ```

2. **Run the Script**:  
   Run the script using:
   
   ```bash
   mongo my_db < 3-all
   ```

3. **Verify the Output**:  
   To verify that all documents in the `school` collection were retrieved, you can also run the following command in the MongoDB shell:

   ```bash
   mongo my_db
   db.school.find().pretty()
   ```

</details>

<details>
  <summary><strong>Troubleshooting</strong></summary>

- **Duplicate Documents**:  
   If multiple documents with the same data are found (e.g., multiple `"Holberton school"` entries), you may want to delete one of them. Use the following command:
   
   ```bash
   db.school.deleteOne({ _id: ObjectId("66fc82c5704aecaa129d2b2e") })
   ```

- **Deleting Extra Entries**:  
   After deleting the duplicate entries, use the `find()` method again to confirm that only the correct documents remain.

</details>


### Task 4: All Matches

This task involves writing a script that lists all documents with `name="Holberton school"` in the `school` collection. The database name will be passed as an option when running the script.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a script that lists all documents with `name="Holberton school"` in the `school` collection.
- The database name will be passed as an option to the MongoDB command.

**Example Output**:
```bash
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
{ "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school" }
bye
```

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create the Script**:  
   Inside the `NoSQL` directory, create a new file `4-match` with the following content:

   ```bash
   // find all documents with name="Holberton school"
   db.school.find({ name: "Holberton school" })
   ```

2. **Run the Script**:  
   To execute the script and list all documents with the matching name, run:

   ```bash
   mongo my_db < 4-match
   ```

3. **Expected Output**:  
   You should see the following output listing all documents with the name `"Holberton school"`:

   ```bash
   MongoDB shell version v4.4.29
   connecting to: mongodb://127.0.0.1:27017/my_db
   { "_id" : ObjectId("66fc89283a5f1925aeab1436"), "name" : "Holberton school" }
   bye
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: This task lists all documents in the `school` collection where the `name` is `"Holberton school"`.
- **Where**: The script is executed in the MongoDB shell via the terminal.
- **Why**: Filtering documents based on specific attributes is a core feature of querying in MongoDB.
- **How**: The `db.school.find()` command filters documents by the `name` field.
- **Who**: Any user with access to the MongoDB server can run this script.
- **When**: This script can be executed anytime MongoDB is running and connected to the local server.

</details>

<details>
  <summary><strong>Testing and Usage</strong></summary>

1. **Ensure MongoDB is Running**:  
   Make sure MongoDB is running by checking the service status or starting it with:
   
   ```bash
   sudo systemctl start mongod
   ```

2. **Run the Script**:  
   Run the script using:
   
   ```bash
   mongo my_db < 4-match
   ```

3. **Verify the Output**:  
   The output should list all documents in the `school` collection where the `name` is `"Holberton school"`. You can verify the contents using:
   
   ```bash
   mongo my_db
   db.school.find({ name: "Holberton school" })
   ```

</details>

### Task 5: Count Documents

This task involves writing a script to count the number of documents in the `school` collection. The database name will be passed as an option when running the script.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a script to display the number of documents in the collection `school`.
- The database name will be passed as an option to the MongoDB command.

**Example Output**:
```bash
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
1
bye
```

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create the Script**:  
   Inside the `NoSQL` directory, create a new file `5-count` with the following content:

   ```bash
   // Script to count all documents in the "school" collection
   db.school.count()
   ```

2. **Run the Script**:  
   To count the documents in the `school` collection, execute the following command:

   ```bash
   mongo my_db < 5-count
   ```

3. **Expected Output**:  
   You should see the number of documents in the `school` collection, like this:

   ```bash
   MongoDB shell version v4.4.29
   connecting to: mongodb://127.0.0.1:27017/my_db
   1
   bye
   ```

</details>

<details>
  <summary><strong>Troubleshooting and Change Explanation</strong></summary>

1. **Original Code and Error**:  
   Initially, the script used the `countDocuments()` method:
   ```bash
   db.school.countDocuments()
   ```
   This resulted in the following error:
   ```bash
   Error: the match filter must be an expression in an object
   ```

2. **Issue**:  
   The `countDocuments()` method is used in newer versions of MongoDB and expects a match expression, which may not be compatible with certain setups or MongoDB versions (like 4.4 or below).

3. **Fix**:  
   Switching to the more widely compatible `db.school.count()` command resolved the issue. This method works across MongoDB versions and counts the total number of documents in the collection.

4. **Why This Worked**:  
   The `count()` method does not require a match filter and simply returns the total document count, which is sufficient for this task. The switch to `db.school.count()` ensures the script runs without issues in MongoDB versions 4.4 and below.

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: This task involves counting the documents in the `school` collection.
- **Where**: The script runs in the MongoDB shell via the terminal.
- **Why**: Counting documents is a common database operation to track the number of entries.
- **How**: The `db.school.count()` method returns the total number of documents in the collection. The `count()` method is widely supported and works with MongoDB 4.4 and below.
- **Who**: Any user with access to the MongoDB server can run this script.
- **When**: This script can be executed anytime MongoDB is running and connected to the local server.

</details>

<details>
  <summary><strong>Testing and Usage</strong></summary>

1. **Ensure MongoDB is Running**:  
   Make sure MongoDB is running by checking the service status or starting it with:
   
   ```bash
   sudo systemctl start mongod
   ```

2. **Run the Script**:  
   Run the script using:
   
   ```bash
   mongo my_db < 5-count
   ```

3. **Verify the Count**:  
   The output will display the number of documents in the `school` collection.

</details>


### Task 6: Update Document

This task involves writing a script that updates all documents in the `school` collection with the name `"Holberton school"` by adding an attribute `address` with the value `"972 Mission street"`. The database name will be passed as an option when running the script.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a script that updates all documents with `name="Holberton school"` in the `school` collection.
- The update should add a new attribute `address` with the value `"972 Mission street"`.
- The database name will be passed as an option to the MongoDB command.

**Example Output**:
```bash
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
bye
```

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create the Script**:  
   Inside the `NoSQL` directory, create a new file `6-update` with the following content:

   ```bash
   // Update all documents with name="Holberton school" to add address
   db.school.update({name: "Holberton school"}, {$set: {address: "972 Mission street"}}, {multi: true})
   ```

   > Note: The `update()` method is used with the `multi: true` option to update all matching documents.

2. **Run the Script**:  
   To execute the script and update the document(s) in the `school` collection, run:

   ```bash
   mongo my_db < 6-update
   ```

3. **Expected Output**:  
   You should see the following output confirming the update of the document(s):

   ```bash
   MongoDB shell version v4.4.29
   connecting to: mongodb://127.0.0.1:27017/my_db
   WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
   bye
   ```

4. **Verification**:  
   After running the script, you can verify that the document(s) were updated by running the following in the MongoDB shell:

   ```bash
   mongo my_db
   db.school.find({ name: "Holberton school" })
   ```

   The output should now show the `address` attribute added:

   ```bash
   { "_id" : ObjectId("..."), "name" : "Holberton school", "address" : "972 Mission street" }
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: This task involves updating all documents in the `school` collection where `name="Holberton school"` to add an `address` attribute.
- **Where**: The script is executed in the MongoDB shell via the terminal.
- **Why**: Updating a document is a fundamental operation in MongoDB, allowing for the modification of existing records.
- **How**: The `db.school.update()` command updates the matched document(s) by adding the `address` field.
- **Who**: Any user with access to the MongoDB server can run this script.
- **When**: This script can be executed anytime MongoDB is running and connected to the local server.

</details>

<details>
  <summary><strong>Troubleshooting: Using update() vs updateMany()</strong></summary>

- **Issue**: In some versions of MongoDB, the `update()` function is deprecated. The curriculum example used an older MongoDB version where `update()` was standard. In newer versions, `updateMany()` is used to ensure compatibility.
  
- **Fix**: If you're using a newer version of MongoDB, switching to `updateMany()` might be more appropriate:
  
  ```bash
  db.school.updateMany({name: "Holberton school"}, {$set: {address: "972 Mission street"}})
  ```

  However, the script using `update()` worked in this instance.

</details>

<details>
  <summary><strong>Testing and Usage</strong></summary>

1. **Ensure MongoDB is Running**:  
   Make sure MongoDB is running by checking the service status or starting it with:
   
   ```bash
   sudo systemctl start mongod
   ```

2. **Run the Script**:  
   Run the script using:
   
   ```bash
   mongo my_db < 6-update
   ```

3. **Verify the Update**:  
   To verify the update, you can run the following command in the MongoDB shell to see if the `address` was added:
   
   ```bash
   mongo my_db
   db.school.find({ name: "Holberton school" })
   ```

</details>

### Task 7: Delete by Match

In this task, the goal is to delete all documents from the `school` collection where the name attribute is `"Holberton school"`. The database name will be passed as an option when running the script.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a script that deletes all documents with `name="Holberton school"` in the collection `school`.
- The database name will be passed as an option to the MongoDB command.

**Example Output**:
```bash
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
{ "acknowledged" : true, "deletedCount" : 1 }
bye
```

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create the Script**:  
   Inside the `NoSQL` directory, create a new file `7-delete` with the following content:
   ```bash
   // Delete all documents with name="Holberton school"
   db.school.deleteMany({name: "Holberton school"})
   ```

2. **Run the Script**:  
   To execute the script and delete the documents, run the following command:
   ```bash
   mongo my_db < 7-delete
   ```

3. **Expected Output**:  
   You should see the following output confirming the deletion of the documents:
   ```bash
   MongoDB shell version v4.4.29
   connecting to: mongodb://127.0.0.1:27017/my_db
   { "acknowledged" : true, "deletedCount" : 1 }
   bye
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: This task involves deleting all documents in the `school` collection where the name attribute is `"Holberton school"`.
- **Where**: The script is executed in the MongoDB shell via the terminal.
- **Why**: Deleting documents based on criteria is a common operation in MongoDB, allowing for clean database management.
- **How**: The `db.school.deleteMany()` command deletes all matching documents in the collection based on the specified filter.
- **Who**: Any user with access to the MongoDB server can run this script.
- **When**: This script can be executed anytime MongoDB is running and connected to the local server.

</details>

<details>
  <summary><strong>Testing and Usage</strong></summary>

1. **Ensure MongoDB is Running**:  
   Make sure MongoDB is running by checking the service status or starting it with:
   ```bash
   sudo systemctl start mongod
   ```

2. **Run the Script**:  
   Run the script using:
   ```bash
   mongo my_db < 7-delete
   ```

3. **Verify the Deletion**:  
   To verify that the document has been deleted, run:
   ```bash
   mongo my_db
   db.school.find({name: "Holberton school"})
   ```
   The command should return no results if the deletion was successful.

</details>

### Task 8: List All Documents in Python

This task involves writing a Python function that lists all documents in a MongoDB collection using `pymongo`. The function will return an empty list if no documents exist in the collection.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a Python function that lists all documents in a MongoDB collection.
- The function should return an empty list if no documents exist.
- The `mongo_collection` argument will be a `pymongo` collection object.

**Prototype**:
```python
def list_all(mongo_collection):
```

**Example Output**:
```bash
[5a8f60cfd4321e1403ba7ab9] Holberton school
[5a8f60cfd4321e1403ba7aba] UCSD
```

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create the Python Script**:  
   Inside the `NoSQL` directory, create a new file `8-all.py` with the following content:

   ```python
   #!/usr/bin/env python3
   '''
   This module contains a function that lists all documents in a MongoDB collection.
   '''
   def list_all(mongo_collection):
       '''
       List all documents in a MongoDB collection.
       '''
       if mongo_collection is None:
           return []
       return list(mongo_collection.find())
   ```

2. **Create the Main Test File**:  
   Inside the same directory, create a test file `8-main.py` to run the function:

   ```python
   #!/usr/bin/env python3
   ''' Test script for listing documents in MongoDB '''
   from pymongo import MongoClient
   list_all = __import__('8-all').list_all

   if __name__ == "__main__":
       client = MongoClient('mongodb://127.0.0.1:27017')
       school_collection = client.my_db.school
       schools = list_all(school_collection)
       for school in schools:
           print("[{}] {}".format(school.get('_id'), school.get('name')))
   ```

3. **Install Required Packages**:  
   Make sure you have `pymongo` installed by running:

   ```bash
   pip install pymongo
   ```

4. **Run the Script**:  
   To test the Python script, first ensure MongoDB is running, and then execute:

   ```bash
   ./8-main.py
   ```

   **Expected Output** (based on your data):
   ```bash
   [66fc89283a5f1925aeab1436] Holberton school
   ```

   If you insert another document, such as "UCSD", you will see both documents listed:
   ```bash
   [66fc89283a5f1925aeab1436] Holberton school
   [new_object_id] UCSD
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: This task involves creating a Python function to list all documents in a MongoDB collection.
- **Where**: The Python script is executed locally and connects to a MongoDB database instance running on your system.
- **Why**: This demonstrates how to use Python and `pymongo` to interact with MongoDB and retrieve data.
- **How**: The `list_all()` function uses `mongo_collection.find()` to return all documents as a list.
- **Who**: Any Python developer using `pymongo` to interact with MongoDB can run this script.
- **When**: This script can be executed whenever MongoDB is running and accessible.

</details>

<details>
  <summary><strong>Troubleshooting</strong></summary>

- **Error Handling**: Initially, the script encountered an issue where MongoDB collections raised a `NotImplementedError` when checked for truthiness (`if not mongo_collection`). This was resolved by using `mongo_collection is None` to check for the collection's validity.

  
  The function was also validated to work by inserting additional documents, ensuring it outputs all relevant entries from the MongoDB collection.

</details>

### Task 9: Insert a Document in Python

This task involves writing a Python function that inserts a new document into a MongoDB collection based on keyword arguments (`kwargs`). The function should return the `_id` of the newly inserted document.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a Python function `insert_school(mongo_collection, **kwargs)` that inserts a new document into the collection `school` using keyword arguments (`kwargs`).
- Return the `_id` of the newly inserted document.

**Prototype**:
```python
def insert_school(mongo_collection, **kwargs):
```

**Example Output**:
```bash
New school created: 5a8f60cfd4321e1403ba7abb
[5a8f60cfd4321e1403ba7ab9] Holberton school
[5a8f60cfd4321e1403ba7aba] UCSD
[5a8f60cfd4321e1403ba7abb] UCSF 505 Parnassus Ave
```

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create the Python Script**:  
   Inside the `NoSQL` directory, create a new file `9-insert_school.py` with the following content:

   ```python
   #!/usr/bin/env python3
   '''
   This module contains a function to insert a document into a MongoDB collection.
   '''

   def insert_school(mongo_collection, **kwargs):
       '''
       Inserts a new document into the MongoDB collection using kwargs.
       Returns the new _id of the inserted document.
       '''
       result = mongo_collection.insert_one(kwargs)
       return result.inserted_id
   ```

2. **Create the Main Test File**:  
   Inside the same directory, create a test file `9-main.py` to run the function:

   ```python
   #!/usr/bin/env python3
   ''' Test script for inserting a document in MongoDB '''
   from pymongo import MongoClient
   list_all = __import__('8-all').list_all
   insert_school = __import__('9-insert_school').insert_school

   if __name__ == "__main__":
       client = MongoClient('mongodb://127.0.0.1:27017')
       school_collection = client.my_db.school

       # Insert a new school
       new_school_id = insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
       print("New school created: {}".format(new_school_id))

       # List all schools
       schools = list_all(school_collection)
       for school in schools:
           print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('address', "")))
   ```

3. **Install Required Packages**:  
   Ensure you have `pymongo` installed by running:

   ```bash
   pip install pymongo
   ```

4. **Run the Script**:  
   To test the Python script, first ensure MongoDB is running, and then execute:

   ```bash
   ./9-main.py
   ```

   **Expected Output**:
   ```bash
   New school created: 66fd9e1197175eaf004d3ec5
   [66fc89283a5f1925aeab1436] Holberton school 972 Mission street
   [66fd9e1197175eaf004d3ec5] UCSF 505 Parnassus Ave
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: This task involves creating a Python function to insert a new document into a MongoDB collection using `kwargs`.
- **Where**: The Python script is executed locally and connects to a MongoDB database instance running on your system.
- **Why**: This demonstrates how to use Python and `pymongo` to insert data into a MongoDB collection.
- **How**: The `insert_school()` function uses `mongo_collection.insert_one()` to add a document to the collection, and it returns the `_id` of the newly inserted document.
- **Who**: Any Python developer using `pymongo` to interact with MongoDB can run this script.
- **When**: This script can be executed whenever MongoDB is running and accessible.

</details>

### Task 10: Change School Topics in Python

This task involves writing a Python function that updates the topics of a school document in a MongoDB collection based on the school's name.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a Python function that updates all topics of a school document in a MongoDB collection.
- The function will use the provided school `name` to locate the document and replace the `topics` field with a new list of topics.
- The `mongo_collection` will be a `pymongo` collection object.

**Prototype**:
```python
def update_topics(mongo_collection, name, topics):
```

**Example Output**:
```bash
[5a8f60cfd4321e1403ba7ab9] Holberton school ['Sys admin', 'AI', 'Algorithm']
[5a8f60cfd4321e1403ba7abb] UCSF 
[5a8f60cfd4321e1403ba7ab9] Holberton school ['iOS']
```

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create the Python Script**:  
   Inside the `NoSQL` directory, create a new file `10-update_topics.py` with the following content:

   ```python
   #!/usr/bin/env python3
   '''
   This module contains a function to update the topics of a document
   in the MongoDB collection based on the name of the school.
   '''


   def update_topics(mongo_collection, name, topics):
       '''
       Update all topics of the school document with the given name.
       '''
       mongo_collection.update_many(
           {"name": name},
           {"$set": {"topics": topics}}
       )
   ```

2. **Create the Main Test File**:  
   Inside the same directory, create a test file `10-main.py` to test the function:

   ```python
   #!/usr/bin/env python3
   ''' Test script for updating school topics in MongoDB '''
   from pymongo import MongoClient
   list_all = __import__('8-all').list_all
   update_topics = __import__('10-update_topics').update_topics

   if __name__ == "__main__":
       client = MongoClient('mongodb://127.0.0.1:27017')
       school_collection = client.my_db.school

       # Update topics for "Holberton school"
       update_topics(school_collection, "Holberton school", ["Sys admin", "AI", "Algorithm"])

       schools = list_all(school_collection)
       for school in schools:
           print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))

       # Update topics for "Holberton school" again
       update_topics(school_collection, "Holberton school", ["iOS"])

       schools = list_all(school_collection)
       for school in schools:
           print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))
   ```

3. **Run the Script**:  
   To test the function, execute the following command in your terminal:

   ```bash
   ./10-main.py
   ```

   **Expected Output**:
   ```bash
   [66fc89283a5f1925aeab1436] Holberton school ['Sys admin', 'AI', 'Algorithm']
   [66fd9e1197175eaf004d3ec5] UCSF 
   [66fc89283a5f1925aeab1436] Holberton school ['iOS']
   [66fd9e1197175eaf004d3ec5] UCSF 
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: This task involves updating the `topics` field of a school document based on its name.
- **Where**: The Python script is executed locally and connects to a MongoDB database instance running on your system.
- **Why**: This demonstrates how to update a specific field in a MongoDB document using Python and `pymongo`.
- **How**: The `update_topics()` function uses `mongo_collection.update_many()` to update all documents that match the provided name.
- **Who**: Any Python developer using `pymongo` to interact with MongoDB can run this script.
- **When**: This script can be executed whenever MongoDB is running and accessible.

</details>


### Task 11: Where can I learn Python?

This task involves writing a Python function that returns a list of schools that cover a specific topic. The function will search the `topics` field for the given topic and return all matching schools.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a Python function that returns all schools that teach a specific topic.
- The `mongo_collection` argument will be a `pymongo` collection object.
- The `topic` argument will be a string representing the topic to search for.

**Prototype**:
```python
def schools_by_topic(mongo_collection, topic):
```

**Example Output**:
```bash
[5a90731fd4321e1e5a3f53e3] Holberton school ['Algo', 'C', 'Python', 'React']
[5a90731fd4321e1e5a3f53e5] UCLA ['C', 'Python']
```

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create the Python Script**:  
   Inside the `NoSQL` directory, create a new file `11-schools_by_topic.py` with the following content:

   ```python
   #!/usr/bin/env python3
   '''
   This module contains a function to retrieve all schools with a specific topic.
   '''

   def schools_by_topic(mongo_collection, topic):
       '''
       Retrieves a list of all schools with the specified topic.
       '''
       return list(mongo_collection.find({"topics": topic}))
   ```

2. **Create the Main Test File**:  
   Inside the same directory, create a test file `11-main.py` to run the function:

   ```python
   #!/usr/bin/env python3
   """ Test script for searching schools by topic """
   from pymongo import MongoClient
   insert_school = __import__('9-insert_school').insert_school
   schools_by_topic = __import__('11-schools_by_topic').schools_by_topic

   if __name__ == "__main__":
       client = MongoClient('mongodb://127.0.0.1:27017')
       school_collection = client.my_db.school

       # Inserting sample data
       j_schools = [
           { 'name': "Holberton school", 'topics': ["Algo", "C", "Python", "React"]},
           { 'name': "UCSF", 'topics': ["Algo", "MongoDB"]},
           { 'name': "UCLA", 'topics': ["C", "Python"]},
           { 'name': "UCSD", 'topics': ["Cassandra"]},
           { 'name': "Stanford", 'topics': ["C", "React", "Javascript"]}
       ]
       for j_school in j_schools:
           insert_school(school_collection, **j_school)

       # Searching schools with 'Python' as a topic
       schools = schools_by_topic(school_collection, "Python")
       for school in schools:
           print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))
   ```

3. **Run the Script**:  
   To test the Python script, first ensure MongoDB is running, and then execute:

   ```bash
   ./11-main.py
   ```

   **Expected Output** (based on your data):
   ```bash
   [66fda4a96ee91cd8371ec5c4] Holberton school ['Algo', 'C', 'Python', 'React']
   [66fda4a96ee91cd8371ec5c6] UCLA ['C', 'Python']
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: This task involves creating a Python function that retrieves all schools that teach a specific topic.
- **Where**: The Python script is executed locally and connects to a MongoDB database instance running on your system.
- **Why**: This demonstrates how to use Python and `pymongo` to query a MongoDB collection based on a specific field.
- **How**: The `schools_by_topic()` function uses `mongo_collection.find()` to search for schools that include the given topic in their `topics` field.
- **Who**: Any Python developer using `pymongo` to interact with MongoDB can run this script.
- **When**: This script can be executed whenever MongoDB is running and accessible.

</details>

### Task 12: Log Stats

This task involves writing a Python script that provides statistics on Nginx logs stored in MongoDB, displaying the total count of logs, counts of HTTP methods used, and the number of status checks.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Write a Python script that provides statistics on Nginx logs stored in MongoDB.
- The script should:
  - Display the total number of logs in the collection.
  - Display the count for each HTTP method (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`).
  - Display the count for `GET` requests with `path=/status`.
- The MongoDB database is `logs`, and the collection is `nginx`.

**Example Output**:
```bash
94778 logs
Methods:
    method GET: 93842
    method POST: 229
    method PUT: 0
    method PATCH: 0
    method DELETE: 0
47415 status check
```

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Download the Log Data**:  
   First, download and extract the provided log data to be restored into MongoDB:
   ```bash
   curl -o dump.zip -s "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-webstack/411/dump.zip"
   unzip dump.zip
   ```

2. **Restore the Logs into MongoDB**:  
   Restore the data to your MongoDB instance:
   ```bash
   mongorestore dump
   ```

3. **Create the Python Script**:  
   Inside the `NoSQL` directory, create a new file `12-log_stats.py` with the following content:
   
   ```python
   #!/usr/bin/env python3
   '''
   This script provides some statistics about Nginx logs stored in MongoDB.
   It displays the total number of logs, the counts of each HTTP method, and
   the count of status checks.
   '''

   from pymongo import MongoClient

   def log_stats():
       '''
       Connect to MongoDB, retrieve statistics on Nginx logs, and print them.
       '''
       client = MongoClient('mongodb://127.0.0.1:27017')
       db = client.logs
       collection = db.nginx

       total_logs = collection.count_documents({})
       get_count = collection.count_documents({"method": "GET"})
       post_count = collection.count_documents({"method": "POST"})
       put_count = collection.count_documents({"method": "PUT"})
       patch_count = collection.count_documents({"method": "PATCH"})
       delete_count = collection.count_documents({"method": "DELETE"})
       status_check = collection.count_documents({"method": "GET", "path": "/status"})

       print(f"{total_logs} logs")
       print("Methods:")
       print(f"\tmethod GET: {get_count}")
       print(f"\tmethod POST: {post_count}")
       print(f"\tmethod PUT: {put_count}")
       print(f"\tmethod PATCH: {patch_count}")
       print(f"\tmethod DELETE: {delete_count}")
       print(f"{status_check} status check")

   if __name__ == "__main__":
       log_stats()
   ```

4. **Run the Script**:  
   Ensure MongoDB is running and then execute:
   ```bash
   ./12-log_stats.py
   ```

   **Expected Output**:
   ```bash
   94778 logs
   Methods:
       method GET: 93842
       method POST: 229
       method PUT: 0
       method PATCH: 0
       method DELETE: 0
   47415 status check
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: This task involves writing a Python script that analyzes Nginx logs stored in MongoDB and displays statistics.
- **Where**: The Python script is executed locally and connects to a MongoDB instance that contains Nginx log data.
- **Why**: The script provides insights into the types of HTTP requests made and how often status checks occur, which is useful for log analysis.
- **How**: The script uses `pymongo` to connect to MongoDB, queries the `nginx` collection for counts of logs and specific methods, and outputs the results to the console.
- **Who**: This script can be used by developers, system administrators, or anyone responsible for analyzing server logs.
- **When**: The script can be executed anytime the logs are available in MongoDB.

</details>
