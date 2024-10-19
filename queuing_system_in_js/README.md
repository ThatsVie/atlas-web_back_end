# Queuing System in JS
This project focuses on building a queue system using Redis, Kue, and Express in Node.js. We will cover topics such as running Redis, performing operations with Redis clients, handling async tasks, and building an Express app that interacts with Redis and a queue system.

## Learning Objectives
<details>
  <summary><strong>How to run a Redis server on your machine</strong></summary>

  Redis is essential for queuing and caching in real-time applications. We will install and run Redis as the first step in this project.
  
  Example:
  ```bash
  redis-server
  ```
</details>

<details>
  <summary><strong>How to run simple operations with the Redis client</strong></summary>

  Using the Redis client in Node.js, you can perform simple operations like setting and getting key-value pairs.
  
</details>

<details>
  <summary><strong>How to store hash values in Redis</strong></summary>

  Redis supports storing and retrieving hash values, which can represent objects or data structures.
  
</details>

<details>
  <summary><strong>How to deal with async operations with Redis</strong></summary>

  Redis operations in Node.js are asynchronous by default. We will use callbacks, promises, or async/await to handle them effectively.
  

</details>

<details>
  <summary><strong>How to use Kue as a queue system</strong></summary>

  Kue is a priority job queue backed by Redis. We will implement job processing and management in later tasks using Kue.
  
</details>

<details>
  <summary><strong>How to build a basic Express app interacting with Redis and Kue</strong></summary>

  In this project, we will create an Express app that interacts with Redis and queues tasks using Kue.
  

</details>

## Resources
- [Redis Quick Start](https://redis.io/docs/latest/integrate/)
- [Redis Client for Node.js](https://github.com/redis/node-redis)
- [Kue Documentation](https://github.com/Automattic/kue)
- [Express Documentation](https://expressjs.com/)

## Requirements
- **Node Version:** Node 12.x.x
- **Operating System:** Ubuntu 18.04
- **Editors:** Visual Studio Code, Vim, Emacs
- **Mandatory Files:** All code files must end with a new line and use the `.js` extension.


## Tasks and Usage

### Task 0: Install a Redis instance

This task involves downloading, compiling, and running Redis 6.0.10 locally. We set up Redis to store key-value pairs and saved the database to a file called `dump.rdb` to ensure persistence across server restarts.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Download and install Redis 6.0.10.
- Start the Redis server.
- Set a key-value pair in the Redis database using the Redis CLI.
- Save the database to an `.rdb` file.
- Copy the `dump.rdb` file into the root of the project folder.
- Verify that calling `get Holberton` returns `"School"`.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Download and Extract Redis:**

   Begin by downloading and extracting Redis 6.0.10:

   ```bash
   wget http://download.redis.io/releases/redis-6.0.10.tar.gz
   tar xzf redis-6.0.10.tar.gz
   cd redis-6.0.10
   ```

2. **Compile Redis:**

   After extracting, compile the Redis source code using the `make` command:

   ```bash
   make
   ```

   This command compiles the Redis binaries, including the Redis server and Redis CLI.

3. **Start the Redis Server:**

   Once compiled, run the Redis server:

   ```bash
   src/redis-server
   ```

4. **Open the Redis CLI and Set Key-Value Pairs:**

   Open another terminal, navigate to the Redis directory, and start the Redis CLI:

   ```bash
   src/redis-cli
   ```

   Set a key-value pair in the database:

   ```bash
   set Holberton School
   ```

   Retrieve the value:

   ```bash
   get Holberton
   ```

   **Expected Output:**

   ```bash
   "School"
   ```

5. **Save the Redis State to `dump.rdb`:**

   Save the current state of the Redis database to a file called `dump.rdb`:

   ```bash
   src/redis-cli save
   ```

   The `dump.rdb` file will be generated in Redis’s default working directory, which you can check using:

   ```bash
   src/redis-cli CONFIG GET dir
   ```

6. **Move the `dump.rdb` File:**

   After saving, move the `dump.rdb` file to the root of the project:

   ```bash
   cp /var/lib/redis/dump.rdb ~/source/atlas-web_back_end/queuing_system_in_js/
   ```

7. **Stop the Redis Server:**

   Once the dump file has been saved and moved, you can stop the Redis server:

   ```bash
   src/redis-cli shutdown
   ```

8. **Verify the `dump.rdb` File in the Root Directory:**

   Ensure that the `dump.rdb` file is correctly located in the project root:

   ```bash
   ls -la ~/source/atlas-web_back_end/queuing_system_in_js/
   ```

9. **Restart Redis and Verify Persistence:**

   Start Redis again:

   ```bash
   src/redis-server
   ```

   Then check that Redis persisted the key-value pair by running the following in the Redis CLI:

   ```bash
   src/redis-cli get Holberton
   ```

   **Expected Output:**

   ```bash
   "School"
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What:** This task involved downloading, installing, and configuring Redis 6.0.10. Redis stores key-value pairs in-memory but can persist data using `.rdb` snapshots. We set a key-value pair `Holberton: School` and ensured it was persisted across server restarts by saving it to a `dump.rdb` file.
- **Where:** Redis is installed in the `redis-6.0.10/` folder, and the persistent data is stored in the `dump.rdb` file located in the project root.
- **Why:** Redis is used for storing and managing data efficiently in-memory. In this task, the goal was to configure Redis to persist the database state, ensuring that the data is available after a restart.
- **How:** Redis saves the database state to a `dump.rdb` file using the `SAVE` command. This file can be loaded when the Redis server restarts, ensuring persistence of the key-value pairs.
- **Who:** This setup is important for developers who use Redis to store temporary data but also require occasional persistence of data across server restarts.
- **When:** The process is required anytime you want to verify that Redis data is properly persisted between server restarts, or when a Redis database needs to be transferred between environments.

</details>

<details>
  <summary><strong>Troubleshooting</strong></summary>

- **Issue:** Permission denied when copying `dump.rdb` to the project root.
  
  - **Solution:** If you encounter a permission error, change the file ownership to the current user:

    ```bash
    sudo chown $USER:$USER dump.rdb
    ```

- **Issue:** The Redis server reports "Address already in use."
  
  - **Solution:** This happens if another Redis instance is running. Find and kill the process:

    ```bash
    ps aux | grep redis
    sudo kill <pid>
    ```

- **Issue:** The `dump.rdb` file doesn't appear in the expected directory.
  
  - **Solution:** Verify the current Redis working directory using:

    ```bash
    src/redis-cli CONFIG GET dir
    ```

    The `dump.rdb` file will be saved to the directory returned by this command.

</details>
