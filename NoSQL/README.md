# NoSQL


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


- What NoSQL means (hint: it's not "not SQL").
- Differences between SQL and NoSQL (the relational chaos vs. the document freedom).
- What ACID is and why NoSQL databases sometimes play it fast and loose with those rules.
- What document storage is and why you won’t need 10 different JOINs to find that one piece of data.
- Types of NoSQL databases.
- Benefits of NoSQL databases in a world that increasingly feels like it's spiraling out of control.
- How to query, insert, update, and delete data in MongoDB like a responsible adult who doesn't accidentally drop entire databases.
- How to use MongoDB effectively, even if you’re still wondering whether SQL will ever forgive you.


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
