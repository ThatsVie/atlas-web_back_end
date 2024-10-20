
<p align="center">
  <img src="https://github.com/user-attachments/assets/ce881c39-ff92-4947-bf57-7996f99bb8b1" alt="puginalley" />
</p>

<h1 align="center">Queuing System in JS</h1>

<p align="center">
  This project demonstrates the integration of Redis and Node.js to build a scalable queuing system using Kue, alongside a basic Express API that manages product stock. The system handles Redis-based job creation and processing, supports async operations, and tracks job progress with real-time updates. It showcases how Redis can be used for both data storage and queue management in modern web applications.
</p>


## Learning Objectives
<details>
  <summary><strong>How to run a Redis server on your machine</strong></summary>

- **Answer:**
  To run a Redis server on your machine:
  1. Install Redis by downloading and extracting it from [redis.io](https://redis.io/download).
  2. Start the Redis server using the command:
     ```bash
     redis-server
     ```
  3. Ensure Redis is running by using:
     ```bash
     redis-cli ping
     ```
     The response should be `PONG`.

- **Tasks Covered:** Task 0, Task 1, Task 12.

</details>



<details>
  <summary><strong>How to run simple operations with the Redis client</strong></summary>

- **Answer:**
  Redis clients, such as `redis-cli` or Node.js Redis client, allow you to run simple operations:
  - **Set a value**:
    ```bash
    set key value
    ```
  - **Get a value**:
    ```bash
    get key
    ```
  In Node.js, you can use:
  ```javascript
  client.set('key', 'value');
  client.get('key', (err, reply) => console.log(reply));
  ```

- **Tasks Covered:** Task 0, Task 2, Task 12.

</details>



<details>
  <summary><strong>How to use a Redis client with Node JS for basic operations</strong></summary>

- **Answer:**
  In Node.js, you can use the `redis` package to interact with Redis:
  ```javascript
  const client = createClient();
  client.set('key', 'value', redis.print);
  client.get('key', (err, reply) => console.log(reply));
  ```

  This allows you to perform basic operations like setting and retrieving data from Redis.

- **Tasks Covered:** Task 1, Task 2.

</details>


<details>
  <summary><strong>How to store hash values in Redis</strong></summary>

- **Answer:**
  To store hash values in Redis using Node.js:
  ```javascript
  client.hset('hashName', 'key', 'value', redis.print);
  client.hgetall('hashName', (err, object) => console.log(object));
  ```
  This allows you to store and retrieve multiple key-value pairs under a single Redis hash.

- **Tasks Covered:** Task 4.

</details>


<details>
  <summary><strong>How to deal with async operations with Redis</strong></summary>

- **Answer:**
  You can deal with async operations in Redis by using `promisify` in Node.js:
  ```javascript
  const { promisify } = require('util');
  const getAsync = promisify(client.get).bind(client);
  const result = await getAsync('key');
  ```
  This enables using `async/await` with Redis operations.

- **Tasks Covered:** Task 3, Task 12.

</details>



<details>
  <summary><strong>How to use Kue as a queue system</strong></summary>

- **Answer:**
  Kue is a priority job queue backed by Redis. You can use Kue as follows:
  ```javascript
  const queue = kue.createQueue();
  queue.create('job_type', { data }).save();
  queue.process('job_type', (job, done) => {
    console.log(`Processing job: ${job.id}`);
    done();
  });
  ```
  This allows you to create, process, and track jobs.

- **Tasks Covered:** Task 6, Task 7, Task 8, Task 9.

</details>



<details>
  <summary><strong>How to build a basic Express app interacting with a Redis server</strong></summary>

- **Answer:**
  In an Express app, you can interact with Redis by using the `redis` package:
  ```javascript
  const client = createClient();
  app.get('/route', async (req, res) => {
    const value = await getAsync('key');
    res.json({ value });
  });
  ```
  This enables you to build an API that can retrieve and modify data in Redis.

- **Tasks Covered:** Task 12.

</details>


<details>
  <summary><strong>How to build a basic Express app interacting with a Redis server and queue</strong></summary>

- **Answer:**
  You can combine Express, Redis, and Kue by setting up routes that process jobs:
  ```javascript
  const queue = kue.createQueue();
  app.get('/route', (req, res) => {
    const job = queue.create('job_type', { data }).save();
    res.json({ job_id: job.id });
  });
  ```
  This allows the app to interact with both Redis for data storage and Kue for job processing.

- **Tasks Covered:** Task 12 (Redis), Task 6-9 (Kue).

</details>


## Resources
- [Redis Quick Start](https://redis.io/docs/latest/integrate/)
- [Redis Client for Node.js](https://github.com/redis/node-redis)
- [Kue Documentation](https://github.com/Automattic/kue)
- [Express Documentation](https://expressjs.com/)

- **MDN - ES6 Modules:**
   This page covers the basics of importing and exporting modules in JavaScript:
   - [JavaScript Modules - Import and Export](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)

- **MDN - Named and Default Exports:**
   This page explains named exports (using `{}`) and default exports in detail:
   - [MDN - Export](https://developer.mozilla.org/en-US/docs/web/javascript/reference/statements/export)
   - [MDN - Import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)


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

### Task 1: Node Redis Client

This task involves creating a Redis client using the `node_redis` package. The script connects to the Redis server and logs messages indicating whether the connection is successful or fails.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Install the `redis` package using npm.
- Write a script named `0-redis_client.js` to connect to the Redis server.
- Log a message when the connection is successful or when it fails.
- Use Babel and ES6 features for the implementation.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Ensure Redis Server is Running:**

   Check if the Redis server is running by executing:

   ```bash
   ps aux | grep redis-server
   ```

   If it is not running, start the Redis server using:

   ```bash
   sudo service redis-server start
   ```

2. **Install Redis Client for Node.js:**

   Install the `node_redis` package using npm:

   From the root of your project (`~/source/atlas-web_back_end/queuing_system_in_js`), run:

   ```bash
   npm install redis
   ```

   This will install the `redis` package required for interacting with the Redis server.

3. **Install Babel and Nodemon:**

   If Babel and Nodemon are not already installed (they should be from Task 0), you can install them with:

   ```bash
   npm install @babel/core @babel/cli @babel/preset-env @babel/node nodemon --save-dev
   ```

4. **Create `0-redis_client.js`:**

   Create a new script named `0-redis_client.js` that connects to the Redis server and logs a message based on the connection status:

   ```javascript
   import { createClient } from 'redis';

   const client = createClient();

   client.on('connect', () => {
     console.log('Redis client connected to the server');
   });

   client.on('error', (err) => {
     console.log(`Redis client not connected to the server: ${err.message}`);
   });
   ```

5. **Run the Script:**

   Run the script using the following command from the root of your project:

   ```bash
   npm run dev 0-redis_client.js
   ```

   **Expected Output:**

   - If the Redis server is running and the client connects successfully, the following message will appear:

     ```
     Redis client connected to the server
     ```

   - If the connection fails (e.g., Redis server is not running), you will see an error message like this:

     ```
     Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
     ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What:** In this task, we create a Redis client using `node_redis`. The script connects to the Redis server and logs connection status.
- **Where:** The script is located in `0-redis_client.js`, and it interacts with the Redis server running on your local machine (127.0.0.1:6379).
- **Why:** Connecting to Redis allows Node.js applications to perform operations on the Redis database, such as storing and retrieving data.
- **How:** The Redis client connects to the server using the `createClient()` method. The connection status is monitored via `client.on('connect')` and `client.on('error')` events.
- **Who:** This task is for developers looking to interact with Redis in Node.js applications.
- **When:** This script should be run whenever you need to verify that the Node.js client can connect to the Redis server.

</details>


### Task 2: Node Redis Client and Basic Operations

In this task, we extend the functionality of the Redis client by adding two key operations for setting and retrieving values from Redis using callbacks:

- **`setNewSchool(schoolName, value)`**: Sets a new key-value pair in Redis and displays a confirmation message using `redis.print`.
- **`displaySchoolValue(schoolName)`**: Retrieves and logs the value for the given key from Redis.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Create a new file `1-redis_op.js` and copy the code from `0-redis_client.js`.
- Add two functions:
  1. **`setNewSchool(schoolName, value)`**: Sets a key-value pair in Redis and logs a confirmation using `redis.print`.
  2. **`displaySchoolValue(schoolName)`**: Logs the value of a key `schoolName` from Redis.
- At the end of the file, call:
  - `displaySchoolValue('Holberton')`
  - `setNewSchool('HolbertonSanFrancisco', '100')`
  - `displaySchoolValue('HolbertonSanFrancisco')`
- Use callbacks for all Redis operations.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Set up the Redis client and connect to the server:**

   The first part of the code sets up the Redis client and handles connection events:

   ```javascript
   import { createClient, print } from 'redis'; 

   const client = createClient();

   client.on('connect', () => {
     console.log('Redis client connected to the server');
   });

   client.on('error', (err) => {
     console.log(`Redis client not connected to the server: ${err.message}`);
   });
   ```

2. **Create `setNewSchool` function to add key-value pairs to Redis:**

   This function adds a key-value pair to the Redis store using `client.set` and logs the result:

   ```javascript
   function setNewSchool(schoolName, value) {
     client.set(schoolName, value, print);  // Use redis.print to log the result
   }
   ```

3. **Create `displaySchoolValue` function to retrieve key values from Redis:**

   This function retrieves and logs the value of a key in Redis using `client.get`:

   ```javascript
   function displaySchoolValue(schoolName) {
     client.get(schoolName, (err, reply) => {
       if (err) {
         console.error(`Error retrieving value for ${schoolName}:`, err);
       } else {
         console.log(reply);  // Log the retrieved value
       }
     });
   }
   ```

4. **Call the functions to test the Redis operations:**

   Finally, we call the functions to display existing values and set new key-value pairs:

   ```javascript
   displaySchoolValue('Holberton');  // Retrieve 'Holberton' key from Redis
   setNewSchool('HolbertonSanFrancisco', '100');  // Add 'HolbertonSanFrancisco' key with value '100'
   displaySchoolValue('HolbertonSanFrancisco');  // Retrieve the newly added key
   ```

5. **Run the code:**

   To run the Redis operations, use the following command:

   ```bash
   npm run dev 1-redis_op.js
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What:** This task demonstrates how to use Redis to set and retrieve key-value pairs using callbacks.
- **Where:** The code is located in the `1-redis_op.js` file.
- **Why:** Redis is widely used for in-memory data storage, and knowing how to interact with it is critical for developers.
- **How:** The functions `setNewSchool` and `displaySchoolValue` use Redis commands (`set` and `get`) to manage data. The values are retrieved and logged using callbacks.
- **Who:** This task is relevant for developers who need to use Redis to store and manage key-value data.
- **When:** This code can be used when a new key-value pair needs to be added or when retrieving values from Redis.

</details>

### Task 3: Node Redis Client and Async Operations

This task involves refactoring the `displaySchoolValue` function from Task 2 to use `async/await` for asynchronous operations. The `promisify` function from the `util` module is used to convert the Redis client’s callback-based `get` method into a Promise-based function, enabling the use of `async/await` for cleaner and more readable code.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Create a new file `2-redis_op_async.js` and copy the code from `1-redis_op.js`.
- Modify the function `displaySchoolValue` to use ES6 `async/await` and the `promisify` function to handle Redis operations asynchronously.
- Use the same operations as in Task 2 (setting and getting values) but with async/await for the `get` method.
- You should see the same result as Task 2 but now leveraging Promises and async/await.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Set up the Redis client and connect to the server:**

   We initialize the Redis client and listen for connection events, as in Task 2:

   ```javascript
   import { createClient, print } from 'redis'; 
   import { promisify } from 'util'; // Import promisify for async operations

   const client = createClient();

   client.on('connect', () => {
     console.log('Redis client connected to the server');
   });

   client.on('error', (err) => {
     console.log(`Redis client not connected to the server: ${err.message}`);
   });
   ```

2. **Modify `displaySchoolValue` to use async/await:**

   We use the `promisify` function to convert the callback-based Redis client `get` method into a Promise-based one, enabling the use of `async/await`:

   ```javascript
   async function displaySchoolValue(schoolName) {
     const getAsync = promisify(client.get).bind(client);  // Promisify the client.get method
     try {
       const reply = await getAsync(schoolName);  // Use async/await for the Redis operation
       console.log(reply);  // Log the value retrieved from Redis
     } catch (err) {
       console.error(`Error retrieving value for ${schoolName}:`, err);
     }
   }
   ```

3. **Reuse the `setNewSchool` function from Task 2:**

   The `setNewSchool` function remains the same as in Task 2, using `client.set` to add key-value pairs:

   ```javascript
   function setNewSchool(schoolName, value) {
     client.set(schoolName, value, print);  // Use redis.print to log the result of the SET operation
   }
   ```

4. **Call the functions to test the async Redis operations:**

   The same functions are called as in Task 2, but now the `displaySchoolValue` function uses `async/await`:

   ```javascript
   displaySchoolValue('Holberton');  // Retrieve 'Holberton' key from Redis using async/await
   setNewSchool('HolbertonSanFrancisco', '100');  // Add 'HolbertonSanFrancisco' key with value '100'
   displaySchoolValue('HolbertonSanFrancisco');  // Retrieve the newly added key using async/await
   ```

5. **Run the code:**

   To run the Redis operations with async/await, use the following command from the project root:

   ```bash
   npm run dev 2-redis_op_async.js
   ```

   **Expected Output:**

   ```bash
   Redis client connected to the server
   Reply: OK
   School
   100
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What:** This task involves refactoring the `displaySchoolValue` function to use `async/await` for Redis operations.
- **Where:** The code is located in the `2-redis_op_async.js` file.
- **Why:** Using `async/await` simplifies asynchronous code and makes it easier to read and maintain, especially for complex operations.
- **How:** The `promisify` function is used to convert the callback-based Redis client methods into Promise-based ones. This allows us to use `async/await` to handle the results more cleanly.
- **Who:** This task is relevant for developers working with asynchronous operations in Node.js, especially when interacting with external services like Redis.
- **When:** This refactor is useful when handling Redis operations that involve asynchronous workflows, making the code more readable and efficient.

</details>



### Task 4: Node Redis Client and Advanced Operations

In this task, we are using Redis to store and retrieve a hash value using the `hset` and `hgetall` commands. The goal is to set up a hash containing key-value pairs representing different school locations and their associated numbers, then retrieve and display the entire hash from Redis.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Use the Redis client to store a hash value.
- Create a hash using `hset`, and store the following key-value pairs:
  - Portland = 50
  - Seattle = 80
  - New York = 20
  - Bogota = 20
  - Cali = 40
  - Paris = 2
- Use `redis.print` to confirm each `hset` operation.
- Use `hgetall` to retrieve and display the entire hash object from Redis.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>


1. **Set Up the Redis Client:**

   Set up the Redis client and add event handlers to listen for connection and error events:

   ```javascript
   import { createClient, print } from 'redis'; // Import Redis client and print function

   const client = createClient(); // Create Redis client

   client.on('connect', () => {
     console.log('Redis client connected to the server');
   });

   client.on('error', (err) => {
     console.log(`Redis client not connected to the server: ${err.message}`);
   });
   ```

2. **Create Hash:**

   Use the `hset` command to set multiple key-value pairs in the Redis hash. The key of the hash is `HolbertonSchools`, and each `hset` command uses `redis.print` to log a confirmation message:

   ```javascript
   client.hset('HolbertonSchools', 'Portland', 50, print);
   client.hset('HolbertonSchools', 'Seattle', 80, print);
   client.hset('HolbertonSchools', 'New York', 20, print);
   client.hset('HolbertonSchools', 'Bogota', 20, print);
   client.hset('HolbertonSchools', 'Cali', 40, print);
   client.hset('HolbertonSchools', 'Paris', 2, print);
   ```

3. **Retrieve and Display Hash:**

   To retrieve the entire hash, use the `hgetall` command, which returns all key-value pairs associated with the specified key (`HolbertonSchools`). The retrieved data is logged to the console:

   ```javascript
   client.hgetall('HolbertonSchools', (err, reply) => {
     if (err) {
       console.error('Error retrieving hash:', err);
     } else {
       console.log(reply); // Log the full hash object
     }
   });
   ```

4. **Complete Code:**

   Here's the complete code for `4-redis_advanced_op.js`:

   ```javascript
   import { createClient, print } from 'redis'; // Import Redis client and print function

   const client = createClient(); // Create Redis client

   client.on('connect', () => {
     console.log('Redis client connected to the server');
   });

   client.on('error', (err) => {
     console.log(`Redis client not connected to the server: ${err.message}`);
   });

   // Store key-value pairs in a Redis hash
   client.hset('HolbertonSchools', 'Portland', 50, print);
   client.hset('HolbertonSchools', 'Seattle', 80, print);
   client.hset('HolbertonSchools', 'New York', 20, print);
   client.hset('HolbertonSchools', 'Bogota', 20, print);
   client.hset('HolbertonSchools', 'Cali', 40, print);
   client.hset('HolbertonSchools', 'Paris', 2, print);

   // Retrieve and display the entire hash
   client.hgetall('HolbertonSchools', (err, reply) => {
     if (err) {
       console.error('Error retrieving hash:', err);
     } else {
       console.log(reply);
     }
   });
   ```

6. **Run the Script:**

   After implementing the above code, run the script using the following command:

   ```bash
   npm run dev 4-redis_advanced_op.js
   ```

7. **Expected Output:**

   ```bash
   Redis client connected to the server
   Reply: 1
   Reply: 1
   Reply: 1
   Reply: 1
   Reply: 1
   Reply: 1
   {
     Portland: '50',
     Seattle: '80',
     'New York': '20',
     Bogota: '20',
     Cali: '40',
     Paris: '2'
   }
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What:** This task demonstrates how to create a Redis hash using `hset` and retrieve the entire hash using `hgetall`.
- **Where:** The Redis hash is stored under the key `HolbertonSchools` in the Redis database.
- **Why:** Hashes in Redis are useful for storing key-value pairs under a single key, making them efficient for representing objects.
- **How:** We used the `hset` command to store key-value pairs in the hash, and the `hgetall` command to retrieve all key-value pairs.
- **Who:** This task is important for developers working with Redis to store complex data structures.
- **When:** The Redis client will automatically handle the storage and retrieval of the hash whenever `hset` or `hgetall` is called.

</details>


### Task 5: Node Redis client publisher and subscriber

This task involves creating two separate Redis clients: one for subscribing to messages (the subscriber) and one for publishing messages (the publisher). The subscriber listens for messages on a Redis channel and responds to the `KILL_SERVER` message by unsubscribing and quitting. The publisher sends a series of messages to the Redis channel after a specified delay.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- In `5-subscriber.js`, create a Redis client:
  - On connection, log the message: `Redis client connected to the server`.
  - On error, log: `Redis client not connected to the server: ERROR MESSAGE`.
  - Subscribe to the channel `holberton school channel`.
  - When a message is received on the channel, log it.
  - If the message is `KILL_SERVER`, unsubscribe and quit the client.

- In `5-publisher.js`, create a Redis client:
  - On connection, log: `Redis client connected to the server`.
  - On error, log: `Redis client not connected to the server: ERROR MESSAGE`.
  - Create a function `publishMessage` that:
    - Accepts two arguments: `message` (string) and `time` (in ms).
    - Logs: `About to send MESSAGE` after the time delay.
    - Publishes the message to the `holberton school channel` after the time delay.

- At the end of `5-publisher.js`, call:
  - `publishMessage("Holberton Student #1 starts course", 100);`
  - `publishMessage("Holberton Student #2 starts course", 200);`
  - `publishMessage("KILL_SERVER", 300);`
  - `publishMessage("Holberton Student #3 starts course", 400);`

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create `5-subscriber.js`:**

   ```javascript
   import { createClient } from 'redis';

   const client = createClient();

   client.on('connect', () => {
     console.log('Redis client connected to the server');
   });

   client.on('error', (err) => {
     console.log(`Redis client not connected to the server: ${err.message}`);
   });

   client.subscribe('holberton school channel');

   client.on('message', (channel, message) => {
     console.log(message);
     if (message === 'KILL_SERVER') {
       client.unsubscribe();
       client.quit();
     }
   });
   ```

2. **Create `5-publisher.js`:**

   ```javascript
   import { createClient } from 'redis';

   const client = createClient();

   client.on('connect', () => {
     console.log('Redis client connected to the server');
   });

   client.on('error', (err) => {
     console.log(`Redis client not connected to the server: ${err.message}`);
   });

   function publishMessage(message, time) {
     setTimeout(() => {
       console.log(`About to send ${message}`);
       client.publish('holberton school channel', message);
     }, time);
   }

   publishMessage("Holberton Student #1 starts course", 100);
   publishMessage("Holberton Student #2 starts course", 200);
   publishMessage("KILL_SERVER", 300);
   publishMessage("Holberton Student #3 starts course", 400);
   ```

3. **Running the Publisher and Subscriber:**

   - **In Terminal 1 (Subscriber):**

     ```bash
     npm run dev 5-subscriber.js
     ```

     **Expected Output in Terminal 1 (Subscriber):**

     ```bash
     [nodemon] 2.0.22
     [nodemon] to restart at any time, enter `rs`
     [nodemon] watching path(s): *.*
     [nodemon] watching extensions: js,mjs,json
     [nodemon] starting `babel-node --presets @babel/preset-env 5-subscriber.js`
     Redis client connected to the server
     Holberton Student #1 starts course
     Holberton Student #2 starts course
     KILL_SERVER
     [nodemon] clean exit - waiting for changes before restart
     ```

   - **In Terminal 2 (Publisher):**

     ```bash
     npm run dev 5-publisher.js
     ```

     **Expected Output in Terminal 2 (Publisher):**

     ```bash
     [nodemon] 2.0.22
     [nodemon] to restart at any time, enter `rs`
     [nodemon] watching path(s): *.*
     [nodemon] watching extensions: js,mjs,json
     [nodemon] starting `babel-node --presets @babel/preset-env 5-publisher.js`
     Redis client connected to the server
     About to send Holberton Student #1 starts course
     About to send Holberton Student #2 starts course
     About to send KILL_SERVER
     About to send Holberton Student #3 starts course
     ```

   - **Explanation of the Output:**
     - The publisher sends four messages to the `holberton school channel`. After 100 ms, it sends "Holberton Student #1 starts course," after 200 ms, it sends "Holberton Student #2 starts course," and so on.
     - The subscriber receives the messages and logs them as they are published.
     - When the message "KILL_SERVER" is sent, the subscriber logs the message, unsubscribes from the channel, and quits the connection. At this point, the subscriber stops listening for any new messages.

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What:** We implemented two Redis clients. One subscribes to a channel and listens for messages, and the other publishes messages at timed intervals.
- **Where:** The code is split into two files:
  - `5-subscriber.js`: Sets up the subscriber client.
  - `5-publisher.js`: Sets up the publisher client and publishes messages to the Redis channel.
- **Why:** This task demonstrates how to implement basic Redis pub/sub operations in Node.js, simulating a simple messaging system where one process sends messages and another process listens for them.
- **How:** The subscriber listens for messages on the `holberton school channel`. The publisher sends a message to this channel after a specified delay.
- **Who:** Developers who want to implement a simple messaging system using Redis pub/sub functionality.
- **When:** Whenever messages need to be passed between different processes or services asynchronously.

</details>

### Task 6: Create the Job Creator

In this task, we create a job using Kue and simulate a push notification system. The job data consists of a phone number and a message, and we will add the job to a queue named `push_notification_code`.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Create a new queue named `push_notification_code`.
- Create a job with the following data format:
  
  ```json
  {
   phoneNumber: string,
  message: string,
  }
  ```

- Once the job is created, log `Notification job created: JOB_ID`.
- Handle job completion by logging `Notification job completed`.
- Handle job failure by logging `Notification job failed`.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Install Kue (If not already installed):**
   
   You can install Kue via npm:

   ```bash
   npm install kue --save
   ```

2. **Create the Job Creator:**

   Write the job creation logic in `6-job_creator.js`:

   ```javascript
   import kue from 'kue';

   // Create a queue
   const queue = kue.createQueue();

   // Create a job data object
   const jobData = {
     phoneNumber: '(555) 555-5555',  // Placeholder phone number
     message: 'you are loved',  // Placeholder message
   };

   // Create a job and add it to the queue
   const job = queue.create('push_notification_code', jobData)
     .save((err) => {
       if (!err) console.log(`Notification job created: ${job.id}`);
     });

   // Handle job completion
   job.on('complete', () => {
     console.log('Notification job completed');
   });

   // Handle job failure
   job.on('failed', () => {
     console.log('Notification job failed');
   });
   ```

3. **Run the Job Creator:**

   To run the job creator, use the following command in the terminal:

   ```bash
   npm run dev 6-job_creator.js
   ```

   **Expected Output:**

   ```bash
   Notification job created: 1
   ```

   Each time you run this command, a new job will be added to the queue, and the job ID will increment.

</details>


### Task 7: Create the Job Processor

In this task, we set up a job processor to handle jobs from the Redis queue using Kue. The processor listens for new jobs and processes them by sending notifications.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Create a file `6-job_processor.js` to process jobs from the `push_notification_code` queue.
- Write a function `sendNotification` that takes two arguments:
  - `phoneNumber`: The phone number to send the notification to.
  - `message`: The message to include in the notification.
- Ensure the job processor listens for new jobs and calls `sendNotification` for each job.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>


1. **Create the `6-job_processor.js` file:**

   Add the following code:

   ```javascript
   import kue from 'kue';

   // Create a queue
   const queue = kue.createQueue();

   /**
    * Function to send a notification.
    * @param {string} phoneNumber - The phone number to send the notification to.
    * @param {string} message - The message to include in the notification.
    */
   function sendNotification(phoneNumber, message) {
     console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
   }

   // Process jobs from the push_notification_code queue
   queue.process('push_notification_code', (job, done) => {
     const { phoneNumber, message } = job.data;
     sendNotification(phoneNumber, message);
     done();
   });
   ```

2. **Run the Job Processor:**

   In **Terminal 1**, run the job processor:

   ```bash
   npm run dev 6-job_processor.js
   ```

3. **Create Jobs in Another Terminal:**

   Open **Terminal 2** and run the job creator:

   ```bash
   npm run dev 6-job_creator.js
   ```

4. **Expected Output:**

   - In **Terminal 2**, the job creator will queue a new job:

     ```bash
     Notification job created: 5
     Notification job completed
     ```

   - In **Terminal 1**, the job processor will pick up the job and send a notification:

     ```bash
     Sending notification to (555) 555-5555, with message: you are loved
     ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What:** The job processor listens for jobs in the Redis queue and processes them by sending notifications.
- **Where:** The processor is set up in `6-job_processor.js`, while job creation is done in `6-job_creator.js`.
- **Why:** We want to handle jobs in an asynchronous manner by processing them in the background.
- **How:** Using Kue, the processor listens for jobs and sends notifications based on the job data.
- **Who:** This pattern is useful for developers managing background tasks in distributed systems.
- **When:** Each time a new job is created, the job processor handles it immediately.

</details>

### Task 8: Track Progress and Errors with Kue - Create the Job Creator

In this task, we create multiple jobs using the Kue library. The jobs are queued and tracked for progress, completion, and errors. Each job simulates sending a message to verify an account.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Create an array `jobs` with data that includes phone numbers and messages.
- For each job, create a new job in the Redis queue named `push_notification_code_2`.
- Log the following events:
  - Job creation.
  - Job completion.
  - Job failure (if any).
  - Job progress (in percentage).

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>


1. **Create the `7-job_creator.js` file:**

   Write the following code to create the jobs and track their progress:

   ```javascript
   import kue from 'kue';

   // Create an array of jobs with phone numbers and messages
   const jobs = [
     {
       phoneNumber: '4153518780',
       message: 'This is the code 1234 to verify your account'
     },
     {
       phoneNumber: '4153518781',
       message: 'This is the code 4562 to verify your account'
     },
     {
       phoneNumber: '4153518743',
       message: 'This is the code 4321 to verify your account'
     },
     {
       phoneNumber: '4153538781',
       message: 'This is the code 4562 to verify your account'
     },
     {
       phoneNumber: '4153118782',
       message: 'This is the code 4321 to verify your account'
     },
     {
       phoneNumber: '4153718781',
       message: 'This is the code 4562 to verify your account'
     },
     {
       phoneNumber: '4159518782',
       message: 'This is the code 4321 to verify your account'
     },
     {
       phoneNumber: '4158718781',
       message: 'This is the code 4562 to verify your account'
     },
     {
       phoneNumber: '4153818782',
       message: 'This is the code 4321 to verify your account'
     },
     {
       phoneNumber: '4154318781',
       message: 'This is the code 4562 to verify your account'
     },
     {
       phoneNumber: '4151218782',
       message: 'This is the code 4321 to verify your account'
     }
   ];

   // Create a Kue queue
   const queue = kue.createQueue();

   // Loop through the jobs array and create a job for each item
   jobs.forEach((jobData) => {
     const job = queue.create('push_notification_code_2', jobData)
       .save((err) => {
         if (!err) {
           console.log(`Notification job created: ${job.id}`);
         }
       });

     // Event listener for job completion
     job.on('complete', () => {
       console.log(`Notification job ${job.id} completed`);
     });

     // Event listener for job failure
     job.on('failed', (err) => {
       console.log(`Notification job ${job.id} failed: ${err}`);
     });

     // Event listener for job progress
     job.on('progress', (progress) => {
       console.log(`Notification job ${job.id} ${progress}% complete`);
     });
   });
   ```

2. **Run the Job Creator:**

   To execute the job creator, use the following command in your terminal:

   ```bash
   npm run dev 7-job_creator.js
   ```

3. **Expected Output:**

   After running the script, you should see output similar to the following in your terminal:

   ```bash
   Notification job created: 8
   Notification job created: 9
   Notification job created: 10
   Notification job created: 11
   Notification job created: 12
   Notification job created: 13
   Notification job created: 14
   Notification job created: 15
   Notification job created: 16
   Notification job created: 17
   Notification job created: 48
  ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What:** This task creates multiple jobs to send notifications, tracks their progress, and logs completion, failure, and progress.
- **Where:** The job creation is done in the `7-job_creator.js` file.
- **Why:** The purpose is to demonstrate how to track job creation, progress, completion, and failure using Kue for job management.
- **How:** We use Kue to manage a queue of jobs that handle asynchronous tasks, such as sending notifications.
- **Who:** This pattern is beneficial for developers working with background job queues in distributed systems.
- **When:** This process is executed whenever the job creator script is run, generating new jobs for the queue.

</details>


### Task 9: Track Progress and Errors with Kue - Create the Job Processor

This task involves creating a job processor that handles notification jobs, tracks their progress, and processes errors (blacklisted phone numbers) using Kue. The processor works alongside a job creator that sends notification jobs to a Redis queue.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Create an array containing blacklisted phone numbers (`4153518780`, `4153518781`).
- Create a `sendNotification` function that takes four arguments: `phoneNumber`, `message`, `job`, and `done`.
  - When called, track the job progress from 0 out of 100.
  - If the phone number is blacklisted, fail the job with an `Error` object and a message indicating the blacklisting.
  - Otherwise, track the job progress to 50% and log the notification being sent.
- Create a Kue queue that processes jobs from the `push_notification_code_2` queue with two jobs at a time.
- Use Redis and Kue to manage the queue and job handling.
- Run two Node processes to simulate job creation and job processing.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Set Up Blacklisted Numbers:**

   Create an array with blacklisted phone numbers:

   ```javascript
   const blacklistedNumbers = ['4153518780', '4153518781'];
   ```

2. **Create the `sendNotification` Function:**

   Define the function that processes notification jobs and tracks job progress:

   ```javascript
   function sendNotification(phoneNumber, message, job, done) {
     job.progress(0, 100);
     
     // Check if the phone number is blacklisted
     if (blacklistedNumbers.includes(phoneNumber)) {
       return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
     }
     
     // Simulate sending a notification and update progress
     job.progress(50, 100);
     console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
     
     done(); // Complete the job
   }
   ```

3. **Create the Queue with Kue:**

   Use Kue to create a queue that processes jobs from the `push_notification_code_2` queue. The queue processes two jobs at a time:

   ```javascript
   const queue = kue.createQueue();
   
   queue.process('push_notification_code_2', 2, (job, done) => {
     const { phoneNumber, message } = job.data;
     sendNotification(phoneNumber, message, job, done);
   });
   ```

4. **Start the Processor:**

   The job processor listens for new jobs on the `push_notification_code_2` queue and processes them. To run the job processor:

   ```bash
   npm run dev 7-job_processor.js
   ```

5. **Create Jobs for the Queue:**

   To test the job processor, create jobs using the job creator script. Each job contains a phone number and a message. To run the job creator:

   ```bash
   npm run dev 7-job_creator.js
   ```

6. **Example of Output in Terminal 1 (Processor):**

   The job processor receives and processes jobs, logging notifications and handling blacklisted numbers:

   ```
   Sending notification to 4153518743, with message: This is the code 4321 to verify your account
   Sending notification to 4153538781, with message: This is the code 4562 to verify your account
   Sending notification to 4153118782, with message: This is the code 4321 to verify your account
   Sending notification to 4153718781, with message: This is the code 4562 to verify your account
   Sending notification to 4159518782, with message: This is the code 4321 to verify your account
   Sending notification to 4158718781, with message: This is the code 4562 to verify your account
   Sending notification to 4153818782, with message: This is the code 4321 to verify your account
   Sending notification to 4154318781, with message: This is the code 4562 to verify your account
   Sending notification to 4151218782, with message: This is the code 4321 to verify your account
   ```

7. **Example of Output in Terminal 2 (Job Creator):**

   The job creator generates jobs and sends them to the queue:

   ```
   Notification job created: 19
   Notification job created: 20
   Notification job created: 21
   Notification job created: 22
   Notification job created: 23
   Notification job created: 24
   Notification job created: 25
   Notification job created: 26
   Notification job created: 27
   Notification job created: 28
   Notification job created: 29
   ```

   Additionally, the job creator tracks the progress and failures of jobs:

   ```
   Notification job 19 0% complete
   Notification job 20 0% complete
   Notification job 19 failed: Phone number 4153518780 is blacklisted
   Notification job 20 failed: Phone number 4153518781 is blacklisted
   Notification job 21 0% complete
   Notification job 21 50% complete
   Notification job 22 0% complete
   Notification job 22 50% complete
   Notification job 21 completed
   Notification job 22 completed
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What:** This task creates a job processor that handles notification jobs, tracks job progress, and processes errors (blacklisted phone numbers) using Kue.
- **Where:** The job processor (`7-job_processor.js`) runs in one terminal, while the job creator (`7-job_creator.js`) runs in another. Both scripts interact with the same Redis queue.
- **Why:** The goal is to simulate real-world job queues with progress tracking and error handling.
- **How:** Jobs are added to the queue with `kue.createQueue`, and the processor listens for new jobs and processes them in parallel.
- **Who:** This is important for developers working on backend systems involving queuing and job management.
- **When:** This is useful in scenarios where asynchronous job processing and error tracking are required, such as handling notifications, emails, or other background tasks.

</details>

### Task 10: Writing the Job Creation Function

This task involves writing a function that takes an array of jobs and a Kue queue as input and creates notification jobs in the `push_notification_code_3` queue. It handles job creation, completion, failure, and progress tracking.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Create a function named `createPushNotificationsJobs` that takes two arguments:
  - `jobs`: an array of job objects (each containing `phoneNumber` and `message`).
  - `queue`: a Kue queue.
- If `jobs` is not an array, throw an error with the message: `Jobs is not an array`.
- For each job in `jobs`, create a new job in the `push_notification_code_3` queue.
- When a job is created, log `Notification job created: JOB_ID`.
- When a job is completed, log `Notification job JOB_ID completed`.
- When a job fails, log `Notification job JOB_ID failed: ERROR`.
- When a job is making progress, log `Notification job JOB_ID PERCENT% complete`.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create the `createPushNotificationsJobs` Function:**

   Write the function to create jobs in the queue and handle events for job creation, completion, failure, and progress:

   ```javascript
   import kue from 'kue';

   /**
    * Function to create push notification jobs.
    * @param {Array} jobs - Array of job objects (with phoneNumber and message).
    * @param {Object} queue - Kue queue instance.
    */
   export default function createPushNotificationsJobs(jobs, queue) {
     if (!Array.isArray(jobs)) {
       throw new Error('Jobs is not an array');
     }

     // Loop through each job in the jobs array and add it to the queue
     jobs.forEach((jobData) => {
       const job = queue.create('push_notification_code_3', jobData);

       // Event listeners for job creation, completion, failure, and progress
       job
         .on('enqueue', () => {
           console.log(`Notification job created: ${job.id}`);
         })
         .on('complete', () => {
           console.log(`Notification job ${job.id} completed`);
         })
         .on('failed', (err) => {
           console.log(`Notification job ${job.id} failed: ${err}`);
         })
         .on('progress', (progress) => {
           console.log(`Notification job ${job.id} ${progress}% complete`);
         });

       // Save the job to the queue
       job.save();
     });
   }
   ```

2. **Create the `8-job-main.js` File:**

   The `8-job-main.js` file is responsible for creating the queue and calling the `createPushNotificationsJobs` function:

   ```javascript
   import kue from 'kue';
   import createPushNotificationsJobs from './8-job.js';

   const queue = kue.createQueue();

   const list = [
     {
       phoneNumber: '(555) 555-5555',
       message: 'This is the code 1234 to verify your account'
     }
   ];

   createPushNotificationsJobs(list, queue);
   ```

3. **Run the Job Processor and Creator:**

   To run the job creator function in `8-job-main.js`, use the following command:

   ```bash
   npm run dev 8-job-main.js
   ```

4. **Example of Output:**

   When the job creation function is executed, it logs the creation, completion, or failure of each job and tracks progress:

   **Terminal Output:**

   ```
   Notification job created: 30
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What:** This task creates a function to generate jobs from an array and send them to a Kue queue.
- **Where:** The function is located in the `8-job.js` file, and the jobs are processed using the Kue queue system.
- **Why:** This setup helps manage notification jobs efficiently, with real-time feedback on job creation, completion, failure, and progress.
- **How:** The function creates a new job for each entry in the `jobs` array, adds it to the `push_notification_code_3` queue, and uses event listeners to log the job's status.
- **Who:** This task is essential for backend developers working with job queuing systems to manage notifications and tasks asynchronously.
- **When:** This is useful when you need to track the status of long-running jobs or notifications, especially when dealing with high volumes of tasks.

</details>


### Task 11: Writing the test for job creation

This task involves writing tests for the `createPushNotificationsJobs` function to ensure its behavior is correctly implemented. The tests should cover various scenarios, including validation and job creation using Kue.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Import the function `createPushNotificationsJobs`.
- Create a queue with Kue.
- Write a test suite to validate the following:
  - Enter the test mode without processing the jobs before executing the tests.
  - Clear the queue and exit the test mode after executing the tests.
  - Validate which jobs are inside the queue.
  - Ensure the queue behaves correctly for different input scenarios.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Set up the test environment:**

   You will need to install the necessary testing dependencies. Ensure Mocha and Chai are installed as development dependencies in your project. You can do this by running:

   ```bash
   npm install mocha chai --save-dev
   ```

   You should also ensure that the test script is set up in your `package.json` file:

   ```json
   {
     "scripts": {
       "test": "./node_modules/.bin/mocha --require @babel/register --exit 8-job.test.js"
     }
   }
   ```

2. **Write the test cases in `8-job.test.js`:**

   Below is the full code for the test suite that verifies different behaviors for the `createPushNotificationsJobs` function.

   ```javascript
   import { expect } from 'chai';
   import kue from 'kue';
   import createPushNotificationsJobs from './8-job.js';

   describe('createPushNotificationsJobs', () => {
     let queue;

     beforeEach(() => {
       queue = kue.createQueue();
       queue.testMode.enter(); // Enter test mode to avoid actual job processing
     });

     afterEach(() => {
       queue.testMode.clear(); // Clear the test queue after each test
       queue.testMode.exit();  // Exit test mode
     });

     it('should display an error message if jobs is not an array', () => {
       expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
     });

     it('should create two new jobs in the queue', () => {
       const jobs = [
         { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
         { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' }
       ];

       createPushNotificationsJobs(jobs, queue);
       expect(queue.testMode.jobs.length).to.equal(2);
       expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
       expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
     });

     it('should not create jobs when an empty array is passed', () => {
       const jobs = [];
       createPushNotificationsJobs(jobs, queue);
       expect(queue.testMode.jobs.length).to.equal(0);
     });
   });
   ```

3. **Run the tests:**

   To run the tests, use the following command:

   ```bash
   npm test 8-job.test.js
   ```

   **Expected Output:**

   ```bash
    queuing_system_in_js@1.0.0 test
    ./node_modules/.bin/mocha --require @babel/register --exit 8-job.test.js

    createPushNotificationsJobs
      ✓ should display an error message if jobs is not an array
      ✓ should create two new jobs in the queue
      ✓ should not create jobs when an empty array is passed

    3 passing (21ms)
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What:** This task involves testing the behavior of the `createPushNotificationsJobs` function. The function is responsible for creating new jobs in the Kue queue based on the input.
- **Where:** The test file is located in `8-job.test.js`, and the function `createPushNotificationsJobs` is in `8-job.js`.
- **Why:** Testing ensures that the function behaves correctly for different input scenarios, including error handling and job creation.
- **How:** The tests use Mocha, Chai, and Kue's `testMode` to simulate job creation in the queue and validate the results without actually processing the jobs.
- **Who:** This task is useful for developers who want to verify that their job creation logic in the queue works as expected, including validation and job handling.
- **When:** The tests are executed every time `npm test 8-job.test.js` is run, ensuring the function behaves correctly before deployment or further development.

</details>

### Task 12: In Stock?

This task involves creating a product reservation system using Express and Redis. Users can check product availability, reserve products, and track stock using HTTP requests. Redis is used to manage stock levels.


<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Create an Express server listening on port `1245`.
- Set up a list of products and expose API routes to:
  - Get the list of products (`GET /list_products`).
  - Get details of a product by `itemId` (`GET /list_products/:itemId`).
  - Reserve a product by reducing its stock (`GET /reserve_product/:itemId`).
- Use Redis to store and manage product stock levels.
- Ensure responses are returned in JSON format.
- Use `async/await` with `promisify` for Redis operations.
  
</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Set up the server and dependencies:**
   
   Install Express, Redis, and utilities:
   ```bash
   npm install express redis util
   ```

   Start Redis:
   ```bash
   redis-server
   ```

2. **Create the list of products:**
   
   Define the product list as follows:
   ```javascript
   const listProducts = [
     { itemId: 1, itemName: 'Suitcase 250', price: 50, stock: 4 },
     { itemId: 2, itemName: 'Suitcase 450', price: 100, stock: 10 },
     { itemId: 3, itemName: 'Suitcase 650', price: 350, stock: 2 },
     { itemId: 4, itemName: 'Suitcase 1050', price: 550, stock: 5 },
   ];
   ```

3. **Set up Redis client:**

   Create a Redis client and use `promisify` to handle async Redis operations:
   ```javascript
   const client = createClient();
   const getAsync = promisify(client.get).bind(client);
   const setAsync = promisify(client.set).bind(client);
   ```

4. **Define routes for the API:**

   - **GET `/list_products`:** Return a list of all available products.
   - **GET `/list_products/:itemId`:** Return the details of a specific product, including the current stock from Redis.
   - **GET `/reserve_product/:itemId`:** Reserve a product by reducing its stock.

   Example route for `/list_products`:
   ```javascript
   app.get('/list_products', (req, res) => {
     const products = listProducts.map(({ itemId, itemName, price, stock }) => ({
       itemId,
       itemName,
       price,
       initialAvailableQuantity: stock,
     }));
     res.json(products);
   });
   ```

   Example route for `/reserve_product/:itemId`:
   ```javascript
   app.get('/reserve_product/:itemId', async (req, res) => {
     const itemId = parseInt(req.params.itemId, 10);
     const product = getItemById(itemId);
   
     if (!product) {
       res.json({ status: 'Product not found' });
       return;
     }
   
     let currentStock = await getCurrentReservedStockById(itemId);
     if (currentStock === null) {
       currentStock = product.stock;
     }
   
     if (currentStock <= 0) {
       res.json({ status: 'Not enough stock available', itemId });
     } else {
       await reserveStockById(itemId, currentStock - 1);
       res.json({ status: 'Reservation confirmed', itemId });
     }
   });
   ```

5. **Run the server:**

   Start the server using:
   ```bash
   npm run dev 9-stock.js
   ```

</details>

<details>
  <summary><strong>Usage Instructions (Browser and Curl)</strong></summary>

1. **Get the list of products:**

   - **Curl:**
     ```bash
     curl localhost:1245/list_products
     ```
   - **Browser:**
     Visit [http://localhost:1245/list_products](http://localhost:1245/list_products)

2. **Get details of a specific product:**

   - **Curl:**
     ```bash
     curl localhost:1245/list_products/1
     ```
   - **Browser:**
     Visit [http://localhost:1245/list_products/1](http://localhost:1245/list_products/1)

3. **Reserve a product:**

   - **Curl:**
     ```bash
     curl localhost:1245/reserve_product/1
     ```
   - **Browser:**
     Visit [http://localhost:1245/reserve_product/1](http://localhost:1245/reserve_product/1)

</details>

<details>
  <summary><strong>Troubleshooting</strong></summary>

1. **Port already in use (`EADDRINUSE`):**

   If you see an error about port `1245` being in use:
   - Find the process using the port:
     ```bash
     sudo lsof -i :1245
     ```
   - Kill the process:
     ```bash
     sudo kill <PID>
     ```
   - Restart the server:
     ```bash
     npm run dev 9-stock.js
     ```

2. **Redis connection issues:**
   - Ensure Redis is running:
     ```bash
     redis-cli ping
     ```
   - Response should be `PONG`, indicating the Redis server is connected.

</details>

<details>
  <summary><strong>Sample Outputs</strong></summary>

1. **List products:**
   ```bash
   curl localhost:1245/list_products
   ```
   **Response:**
   ```json
   [
     {"itemId":1,"itemName":"Suitcase 250","price":50,"initialAvailableQuantity":4},
     {"itemId":2,"itemName":"Suitcase 450","price":100,"initialAvailableQuantity":10},
     {"itemId":3,"itemName":"Suitcase 650","price":350,"initialAvailableQuantity":2},
     {"itemId":4,"itemName":"Suitcase 1050","price":550,"initialAvailableQuantity":5}
   ]
   ```

2. **Product details:**
   ```bash
   curl localhost:1245/list_products/1
   ```
   **Response:**
   ```json
   {
     "itemId":1,
     "itemName":"Suitcase 250",
     "price":50,
     "initialAvailableQuantity":4,
     "currentQuantity":4
   }
   ```

3. **Reserve a product:**
   ```bash
   curl localhost:1245/reserve_product/1
   ```
   **Response:**
   ```json
   {"status":"Reservation confirmed","itemId":1}
   ```

4. **Product not found:**
   ```bash
   curl localhost:1245/list_products/12
   ```
   **Response:**
   ```json
   {"status":"Product not found"}
   ```

5. **Not enough stock available:**
   After making enough reservations to deplete stock:
   ```bash
   curl localhost:1245/reserve_product/1
   ```
   **Response:**
   ```json
   {"status":"Not enough stock available","itemId":1}
   ```

</details>


<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What:** This task builds a product reservation system using Express for the API and Redis for stock management.
- **Where:** Products and their stock are managed in Redis, with API routes exposed via Express on port `1245`.
- **Why:** This approach provides a fast and scalable way to manage stock levels using an in-memory database like Redis.
- **How:** Stock levels are stored in Redis, and the Express server exposes API routes to interact with product data.
- **Who:** Developers who need a lightweight, real-time system to manage product stock levels.
- **When:** Whenever an external service needs to manage product availability in an efficient, scalable way.

</details>
